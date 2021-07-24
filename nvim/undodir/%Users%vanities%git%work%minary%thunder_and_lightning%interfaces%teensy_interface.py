Vim�UnDo� [�'�:��K~|!VE�ڵ_��f�t��Պ��   �   2        logger.debug("running cmd={}".format(cmd))   �                          \���    _�                     +   +    ����                                                                                                                                                                                                                                                                                                                                                             \��3     �   *   ,   �      H        logger.debug("Light & Sound has " "firmware={}".format(fw_hash))5�_�                    +        ����                                                                                                                                                                                                                                                                                                                            +   '       ,   '       V   '    \��;     �   *   +          E        logger.debug("Light & Sound has firmware={}".format(fw_hash))   W        logger.debug("Light & Sound repo has " "firmware={}".format(published_fw_hash))5�_�                    +        ����                                                                                                                                                                                                                                                                                                                            +   '       +   '       V   '    \��<    �   *   +           5�_�                    �   -    ����                                                                                                                                                                                                                                                                                                                            +   '       +   '       V   '    \��P     �   �   �   �      D            chunk_data = result[(chunk * 128) : ((chunk + 1) * 128)]5�_�                    �   -    ����                                                                                                                                                                                                                                                                                                                            +   '       +   '       V   '    \��Q    �               �   import wave   import zlib   import struct   import serial   import time   	import re   import subprocess   import shlex        from utils import CoinmineLogger       !logger = CoinmineLogger(__name__)           class TeensyInterface:   J    def __init__(self, serial_path, script_path=None, serial_baud=115200):   &        self.serial_path = serial_path   &        self.serial_baud = serial_baud       ?        self.firmware_path = "{}/firmware/".format(script_path)   5        self.helpers_path = script_path + "/helpers/"   2        self.asset_path = script_path + "/assets/"           def set_serial_port(self):   )        self.serial_port = serial.Serial(   ;            self.serial_path, self.serial_baud, timeout=0.1   	        )       3    def update_firmware_if_version_different(self):   $        fw_hash = self.get_version()               published_fw_hash = ""           try:   U            version_file = open(self.firmware_path + "thunder-and-lightning.version")   ?            published_fw_hash = version_file.readline().strip()           except IOError:               logger.warn(   A                "Could not open {}thunder-and-lightning.version."   M                "Skipping firmware update checks.".format(self.firmware_path)               )               return       (        if fw_hash != published_fw_hash:               logger.warn(   Q                "Need to update from {} to {}".format(fw_hash, published_fw_hash)               )   #            self._update_firmware()               return True           return False       +    def flash_audio_files_if_changed(self):   :        # Map all of the slots on the flash to audio files           audio_files = [   1            (0, self.asset_path + "PowerOn.wav"),   3            (1, self.asset_path + "PowerDown.wav"),   5            (2, self.asset_path + "WifiConnect.wav"),   8            (3, self.asset_path + "StartedSuccess.wav"),   	        ]       &        for audio_file in audio_files:   5            file_crc = self.calc_crc32(audio_file[1])               device_crc = 0                   try:   ;                device_crc = self.read_crc32(audio_file[0])               except ValueError:                   device_crc = 0                   logger.info(   '                "{} -- File CRC32: {} "   Q                "-- Device CRC32: {}".format(audio_file[1], file_crc, device_crc)               )   &            if file_crc != device_crc:   -                self.store_audio(*audio_file)       ;    def send_packet(self, op_code, argument, data=bytes()):   V        send_data = bytes([0xAA, op_code, argument, len(data)]) + data + bytes([0x55])   )        self.serial_port.write(send_data)           def read_response(self):           ret = []   5        chr = self.serial_port.read().decode("utf-8")           while chr != "\n":               if chr != "\r":                   ret += chr   9            chr = self.serial_port.read().decode("utf-8")           return "".join(ret)       7    def handle_response(self, function_name, response):           """   O        OpCode:[OpCode]::[Return String]::Command [Success|Failed]::[ErrorCode]   6        E.g. OpCode:23::2253080301::Command Success::0           """           try:   #            regex_match = re.match(   -                "OpCode:(?P<opcode>[0-9]+)::"   )                "(?P<return_string>.*)::"   >                "Command (?P<success_string>Success|Failed)::"   )                "(?P<error_code>[0-9]+)",                   response,               )               if regex_match:   B                return_string = regex_match.group("return_string")   J                success = regex_match.group("success_string") == "Success"   ?                err_code = int(regex_match.group("error_code"))                       if not success:   %                    raise ValueError(   ;                        "ThunderAndLightningInterface::{} "   B                        "error {}".format(function_name, err_code)                       )       $                return return_string               else:   !                raise ValueError(   4                    "ThunderAndLightningInterface::"   ?                    "Bad Response Format ({})".format(response)                   )           except Exception:               pass           def get_version(self):           self.send_packet(0, 0)   H        return self.handle_response("get_version", self.read_response())       1    def set_lights(self, state_bin, duration=33):   K        # Keep polling the device until we have a free command slot to fill            while self.query() == 0:               time.sleep(0.1)       8        self.send_packet(0x04, int(duration), state_bin)   @        self.handle_response("set_lights", self.read_response())           def query(self):   $        self.send_packet(0x07, 0x00)   G        return int(self.handle_response("query", self.read_response()))       '    def play_audio(self, sample_index):   )        self.send_packet(1, sample_index)   @        self.handle_response("play_audio", self.read_response())       3    def store_audio(self, sample_index, file_name):   /        wave_reader = wave.open(file_name, "r")   >        chans, res, fs, length, _, _ = wave_reader.getparams()       *        nframes = wave_reader.getnframes()   O        data = struct.unpack("<%dh" % nframes, wave_reader.readframes(nframes))               converted = []           for value in data:   -            converted.append(value + 2 ** 15)       :        result = struct.pack("<%dH" % nframes, *converted)                crc = zlib.crc32(result)       8        # calculate number of chunks to send (fake ceil)   /        chunks = int(len(result) / 128.0 + 0.5)       +        # initiate a sample write operation   S        self.send_packet(2, sample_index, struct.pack("=3I", crc, chunks, nframes))   A        self.handle_response("store_audio", self.read_response())       #        for chunk in range(chunks):   C            chunk_data = result[(chunk * 128): ((chunk + 1) * 128)]   @            packed_bytes = struct.pack("=I", chunk) + chunk_data       H            logger.debug("Sending chunk {} of {}".format(chunk, chunks))   <            self.send_packet(22, sample_index, packed_bytes)   E            self.handle_response("store_audio", self.read_response())       $    def calc_crc32(self, file_name):   /        wave_reader = wave.open(file_name, "r")   >        chans, res, fs, length, _, _ = wave_reader.getparams()       *        nframes = wave_reader.getnframes()   O        data = struct.unpack("<%dh" % nframes, wave_reader.readframes(nframes))               converted = []           for value in data:   -            converted.append(value + 2 ** 15)       :        result = struct.pack("<%dH" % nframes, *converted)       !        return zlib.crc32(result)       '    def read_crc32(self, sample_index):   *        self.send_packet(23, sample_index)   L        return int(self.handle_response("read_crc32", self.read_response()))           def _update_firmware(self):   @        # teensy_loader_cli --mcu=TEENSYLC -s $(HEX_OUTPUT_FILE)           cmd = (   "            "{}teensy_loader_cli "               "--mcu=TEENSYLC "   7            "-s -v {}thunder-and-lightning.hex".format(   5                self.helpers_path, self.firmware_path               )   	        )   2        logger.debug("running cmd={}".format(cmd))   4        subprocess.run(shlex.split(cmd), timeout=10)5�_�                    �   -    ����                                                                                                                                                                                                                                                                                                                               '          '       V   '    \��S     �   �   �   �      D            chunk_data = result[(chunk * 128) : ((chunk + 1) * 128)]5�_�                    �   -    ����                                                                                                                                                                                                                                                                                                                               '          '       V   '    \��T    �               �   import wave   import zlib   import struct   import serial   import time   	import re   import subprocess   import shlex        from utils import CoinmineLogger       !logger = CoinmineLogger(__name__)           class TeensyInterface:   J    def __init__(self, serial_path, script_path=None, serial_baud=115200):   &        self.serial_path = serial_path   &        self.serial_baud = serial_baud       ?        self.firmware_path = "{}/firmware/".format(script_path)   5        self.helpers_path = script_path + "/helpers/"   2        self.asset_path = script_path + "/assets/"           def set_serial_port(self):   )        self.serial_port = serial.Serial(   ;            self.serial_path, self.serial_baud, timeout=0.1   	        )       3    def update_firmware_if_version_different(self):   $        fw_hash = self.get_version()               published_fw_hash = ""           try:   U            version_file = open(self.firmware_path + "thunder-and-lightning.version")   ?            published_fw_hash = version_file.readline().strip()           except IOError:               logger.warn(   A                "Could not open {}thunder-and-lightning.version."   M                "Skipping firmware update checks.".format(self.firmware_path)               )               return       (        if fw_hash != published_fw_hash:               logger.warn(   Q                "Need to update from {} to {}".format(fw_hash, published_fw_hash)               )   #            self._update_firmware()               return True           return False       +    def flash_audio_files_if_changed(self):   :        # Map all of the slots on the flash to audio files           audio_files = [   1            (0, self.asset_path + "PowerOn.wav"),   3            (1, self.asset_path + "PowerDown.wav"),   5            (2, self.asset_path + "WifiConnect.wav"),   8            (3, self.asset_path + "StartedSuccess.wav"),   	        ]       &        for audio_file in audio_files:   5            file_crc = self.calc_crc32(audio_file[1])               device_crc = 0                   try:   ;                device_crc = self.read_crc32(audio_file[0])               except ValueError:                   device_crc = 0                   logger.info(   '                "{} -- File CRC32: {} "   Q                "-- Device CRC32: {}".format(audio_file[1], file_crc, device_crc)               )   &            if file_crc != device_crc:   -                self.store_audio(*audio_file)       ;    def send_packet(self, op_code, argument, data=bytes()):   V        send_data = bytes([0xAA, op_code, argument, len(data)]) + data + bytes([0x55])   )        self.serial_port.write(send_data)           def read_response(self):           ret = []   5        chr = self.serial_port.read().decode("utf-8")           while chr != "\n":               if chr != "\r":                   ret += chr   9            chr = self.serial_port.read().decode("utf-8")           return "".join(ret)       7    def handle_response(self, function_name, response):           """   O        OpCode:[OpCode]::[Return String]::Command [Success|Failed]::[ErrorCode]   6        E.g. OpCode:23::2253080301::Command Success::0           """           try:   #            regex_match = re.match(   -                "OpCode:(?P<opcode>[0-9]+)::"   )                "(?P<return_string>.*)::"   >                "Command (?P<success_string>Success|Failed)::"   )                "(?P<error_code>[0-9]+)",                   response,               )               if regex_match:   B                return_string = regex_match.group("return_string")   J                success = regex_match.group("success_string") == "Success"   ?                err_code = int(regex_match.group("error_code"))                       if not success:   %                    raise ValueError(   ;                        "ThunderAndLightningInterface::{} "   B                        "error {}".format(function_name, err_code)                       )       $                return return_string               else:   !                raise ValueError(   4                    "ThunderAndLightningInterface::"   ?                    "Bad Response Format ({})".format(response)                   )           except Exception:               pass           def get_version(self):           self.send_packet(0, 0)   H        return self.handle_response("get_version", self.read_response())       1    def set_lights(self, state_bin, duration=33):   K        # Keep polling the device until we have a free command slot to fill            while self.query() == 0:               time.sleep(0.1)       8        self.send_packet(0x04, int(duration), state_bin)   @        self.handle_response("set_lights", self.read_response())           def query(self):   $        self.send_packet(0x07, 0x00)   G        return int(self.handle_response("query", self.read_response()))       '    def play_audio(self, sample_index):   )        self.send_packet(1, sample_index)   @        self.handle_response("play_audio", self.read_response())       3    def store_audio(self, sample_index, file_name):   /        wave_reader = wave.open(file_name, "r")   >        chans, res, fs, length, _, _ = wave_reader.getparams()       *        nframes = wave_reader.getnframes()   O        data = struct.unpack("<%dh" % nframes, wave_reader.readframes(nframes))               converted = []           for value in data:   -            converted.append(value + 2 ** 15)       :        result = struct.pack("<%dH" % nframes, *converted)                crc = zlib.crc32(result)       8        # calculate number of chunks to send (fake ceil)   /        chunks = int(len(result) / 128.0 + 0.5)       +        # initiate a sample write operation   S        self.send_packet(2, sample_index, struct.pack("=3I", crc, chunks, nframes))   A        self.handle_response("store_audio", self.read_response())       #        for chunk in range(chunks):   C            chunk_data = result[(chunk * 128): ((chunk + 1) * 128)]   @            packed_bytes = struct.pack("=I", chunk) + chunk_data       H            logger.debug("Sending chunk {} of {}".format(chunk, chunks))   <            self.send_packet(22, sample_index, packed_bytes)   E            self.handle_response("store_audio", self.read_response())       $    def calc_crc32(self, file_name):   /        wave_reader = wave.open(file_name, "r")   >        chans, res, fs, length, _, _ = wave_reader.getparams()       *        nframes = wave_reader.getnframes()   O        data = struct.unpack("<%dh" % nframes, wave_reader.readframes(nframes))               converted = []           for value in data:   -            converted.append(value + 2 ** 15)       :        result = struct.pack("<%dH" % nframes, *converted)       !        return zlib.crc32(result)       '    def read_crc32(self, sample_index):   *        self.send_packet(23, sample_index)   L        return int(self.handle_response("read_crc32", self.read_response()))           def _update_firmware(self):   @        # teensy_loader_cli --mcu=TEENSYLC -s $(HEX_OUTPUT_FILE)           cmd = (   "            "{}teensy_loader_cli "               "--mcu=TEENSYLC "   7            "-s -v {}thunder-and-lightning.hex".format(   5                self.helpers_path, self.firmware_path               )   	        )   2        logger.debug("running cmd={}".format(cmd))   4        subprocess.run(shlex.split(cmd), timeout=10)5�_�      	              �       ����                                                                                                                                                                                                                                                                                                                               '          '       V   '    \���     �   �   �   �      2        logger.debug("running cmd={}".format(cmd))5�_�      
           	   �   .    ����                                                                                                                                                                                                                                                                                                                               '          '       V   '    \���     �   �   �   �      C        logger.debug("running firmware updater cmd={}".format(cmd))5�_�   	              
   �   .    ����                                                                                                                                                                                                                                                                                                                               '          '       V   '    \���     �   �   �   �      C        logger.debug("running firmware update" cmd={}".format(cmd))5�_�   
                 �   .    ����                                                                                                                                                                                                                                                                                                                               '          '       V   '    \���     �   �   �   �      .        logger.debug("running firmware update"5�_�                    �   6    ����                                                                                                                                                                                                                                                                                                                               '          '       V   '    \���     �   �   �   �      7        logger.debug("running firmware update", {"cmd"}5�_�                     �   <    ����                                                                                                                                                                                                                                                                                                                               '          '       V   '    \���    �   �   �   �      <        logger.debug("running firmware update", {"cmd": cmd}5��