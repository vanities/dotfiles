Vim�UnDo� jU��'��`a�+
�_eG�u���'���	>��U   G   D            logger.error("could not run amdmeminfo! e={}".format(e))            +       +   +   +    ^�{�    _�                     .        ����                                                                                                                                                                                                                                                                                                                                                             ]Mܟ     �   -   .          <<<<<<< HEAD5�_�                    .   (    ����                                                                                                                                                                                                                                                                                                                                                             ]Mܧ     �   -   /   E      >        amd_types = ["RX 580", "RX 570", "Vega 56", "Vega 64"]5�_�                    1   9    ����                                                                                                                                                                                                                                                                                                                                                             ]Mܪ     �   0   2   E      ;        amd_types = ["RX 580", "Coinmine RX 580", "RX 570"]�   1   2   E    5�_�                    1   :    ����                                                                                                                                                                                                                                                                                                                                                             ]Mܭ    �   0   2   E      P        amd_types = ["RX 580", "Coinmine RX 580", "RX 570" "Vega 56", "Vega 64"]5�_�                    .        ����                                                                                                                                                                                                                                                                                                                            .   (       /          V   :    ]Mܱ     �   -   .          )        amd_types = ["RX 580", "RX 570",]   =======5�_�                    0        ����                                                                                                                                                                                                                                                                                                                            .   (       .          V   :    ]Mܵ    �   /   0          0>>>>>>> 430daa9af71a140786e15634a6d3ecfb507628c45�_�                    /   P    ����                                                                                                                                                                                                                                                                                                                                                             ]�Xi     �   .   0   B      Q        amd_types = ["RX 580", "Coinmine RX 580", "RX 570", "Vega 56", "Vega 64"]5�_�      	              /   \    ����                                                                                                                                                                                                                                                                                                                                                             ]�Xv    �               B   	import re   import shlex   import subprocess        from utils import CoinmineLogger       !logger = CoinmineLogger(__name__)           class AmdMemInfo:   (    def __init__(self, amdmeminfo_path):   .        self.amdmeminfo_path = amdmeminfo_path           def get_all_gpu_info(self):           all_gpu_info = []           try:   1            amdmeminfo = subprocess.check_output(   G                shlex.split("{} --opencl".format(self.amdmeminfo_path))               ).decode("utf-8")   T            split_info = amdmeminfo.split("-----------------------------------")[1:]                   adapter_num = 0   #            for line in split_info:   9                gpu_info = AmdMemInfo._get_gpu_info(line)                   if gpu_info:                        logger.info(   F                        "AMD GPU found adapter_num={} type={}".format(   1                            adapter_num, gpu_info                           )                       )   1                    all_gpu_info.append(gpu_info)           except Exception as e:   D            logger.error("could not run amdmeminfo! e={}".format(e))               if not all_gpu_info:   -            logger.error("No AMD GPUs found")           return all_gpu_info           def get_num_of_gpus(self):   +        return len(self.get_all_gpu_info())           # helpers       @staticmethod   "    def _get_gpu_info(amdmeminfo):           gpu_info = {}   ,        # least specific to more specific ->   _        amd_types = ["RX 580", "Coinmine RX 580", "RX 570", "Vega 56", "Vega 64", "Radeon VII"]   ?        memory_types = ["Hynix", "Samsung", "Micron", "Elpida"]               for gpu in amd_types:   8            if re.search(gpu, amdmeminfo, re.MULTILINE):   '                gpu_info["model"] = gpu            for gpu in memory_types:   8            if re.search(gpu, amdmeminfo, re.MULTILINE):   -                gpu_info["memory_type"] = gpu   /        gpu_info["memory_serial"] = re.findall(   7            r"Memory Model.*", amdmeminfo, re.MULTILINE           )[0].split()[-1]   W        gpu_info["adapter_num"] = re.findall(r"OpenCL ID.*", amdmeminfo, re.MULTILINE)[               0           ].split()[-1]   .        gpu_info["bios_version"] = re.findall(   7            r"BIOS Version.*", amdmeminfo, re.MULTILINE           )[0].split()[-1]               return gpu_info5�_�      
           	   5       ����                                                                                                                                                                                                                                                                                                                                                             ]��t     �   5   7   I    �   5   6   I    5�_�   	              
   6       ����                                                                                                                                                                                                                                                                                                                                                             ]��v     �   5   7   J                  "Radeon VII",5�_�   
                 6       ����                                                                                                                                                                                                                                                                                                                                                             ]��|     �   5   7   J                  "",5�_�                    6       ����                                                                                                                                                                                                                                                                                                                                                             ]���    �   5   7   J                  "5700 XT",5�_�                    6       ����                                                                                                                                                                                                                                                                                                                                                             ]���     �   6   8   K                  �   6   8   J    5�_�                    7       ����                                                                                                                                                                                                                                                                                                                                                             ]���    �               K   	import re   import shlex   import subprocess        from utils import CoinmineLogger       !logger = CoinmineLogger(__name__)           class AmdMemInfo:   (    def __init__(self, amdmeminfo_path):   .        self.amdmeminfo_path = amdmeminfo_path           def get_all_gpu_info(self):           all_gpu_info = []           try:   1            amdmeminfo = subprocess.check_output(   G                shlex.split("{} --opencl".format(self.amdmeminfo_path))               ).decode("utf-8")   T            split_info = amdmeminfo.split("-----------------------------------")[1:]                   adapter_num = 0   #            for line in split_info:   9                gpu_info = AmdMemInfo._get_gpu_info(line)                   if gpu_info:                        logger.info(   F                        "AMD GPU found adapter_num={} type={}".format(   1                            adapter_num, gpu_info                           )                       )   1                    all_gpu_info.append(gpu_info)           except Exception as e:   D            logger.error("could not run amdmeminfo! e={}".format(e))               if not all_gpu_info:   -            logger.error("No AMD GPUs found")           return all_gpu_info           def get_num_of_gpus(self):   +        return len(self.get_all_gpu_info())           # helpers       @staticmethod   "    def _get_gpu_info(amdmeminfo):           gpu_info = {}   ,        # least specific to more specific ->           amd_types = [               "RX 580",               "Coinmine RX 580",               "RX 570",               "Vega 56",               "Vega 64",               "Radeon VII",               "RX 5700 XT",               "Radeon Rx 5700 XT"   	        ]   ?        memory_types = ["Hynix", "Samsung", "Micron", "Elpida"]               for gpu in amd_types:   8            if re.search(gpu, amdmeminfo, re.MULTILINE):   '                gpu_info["model"] = gpu            for gpu in memory_types:   8            if re.search(gpu, amdmeminfo, re.MULTILINE):   -                gpu_info["memory_type"] = gpu   /        gpu_info["memory_serial"] = re.findall(   7            r"Memory Model.*", amdmeminfo, re.MULTILINE           )[0].split()[-1]   W        gpu_info["adapter_num"] = re.findall(r"OpenCL ID.*", amdmeminfo, re.MULTILINE)[               0           ].split()[-1]   .        gpu_info["bios_version"] = re.findall(   7            r"BIOS Version.*", amdmeminfo, re.MULTILINE           )[0].split()[-1]               return gpu_info5�_�                    7       ����                                                                                                                                                                                                                                                                                                                                                             ]���    �   6   8   K                   "Radeon Rx 5700 XT",5�_�                    6       ����                                                                                                                                                                                                                                                                                                                                                             ]���   	 �   5   6                      "RX 5700 XT",5�_�                   6       ����                                                                                                                                                                                                                                                                                                                                                             ]���    �   5   7   J                  "Rx 5700 XT",5�_�                    8   >    ����                                                                                                                                                                                                                                                                                                                                                             ]�ȧ    �   7   9   J      ?        memory_types = ["Hynix", "Samsung", "Micron", "Elpida"]5�_�                   8   >    ����                                                                                                                                                                                                                                                                                                                            8          8           v        ]�f     �   7   9   J      J        memory_types = ["Hynix", "Samsung", "Micron", "Elpida", "Unknown"]5�_�                    8       ����                                                                                                                                                                                                                                                                                                                            8          8           v        ]�i     �   7   9   J      ?        memory_types = ["Hynix", "Samsung", "Micron", "Elpida"]�   8   9   J    5�_�                    8   #    ����                                                                                                                                                                                                                                                                                                                            8          8           v        ]�j     �   7   9   J      J        memory_types = [, "Unknown""Hynix", "Samsung", "Micron", "Elpida"]5�_�                     8       ����                                                                                                                                                                                                                                                                                                                            8          8           v        ]�l    �   7   9   J      L        memory_types = [, "Unknown", "Hynix", "Samsung", "Micron", "Elpida"]5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                                             ^X!8     �         K                  �         J    5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                                             ^X!>     �         K      G                shlex.split("{} --opencl".format(self.amdmeminfo_path))5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                                                             ^X!?     �         K                  cmd = �         K    5�_�   "   $           #      =    ����                                                                                                                                                                                                                                                                                                                                                             ^X!?    �         K      =            cmd = "{} --opencl".format(self.amdmeminfo_path))5�_�   #   %           $           ����                                                                                                                                                                                                                                                                                                                                                             ^X!H     �         K       from utils import CoinmineLogger5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                                                             ^X!U     �         K      1            amdmeminfo = subprocess.check_output(5�_�   %   '           &      5    ����                                                                                                                                                                                                                                                                                                                                                             ^X!`     �         K      M            amdmeminfo = Converter.cmd_to_string(cmd)subprocess.check_output(5�_�   &   (           '           ����                                                                                                                                                                                                                                                                                                                                                V   4    ^X!a    �                                shlex.split(               ).decode("utf-8")5�_�   '   )           (           ����                                                                                                                                                                                                                                                                                                                                                  V        ^X!d    �                import shlex   import subprocess5�_�   (   *           )      "    ����                                                                                                                                                                                                                                                                                                                                                  V        ^X!i    �         G      5            amdmeminfo = Converter.cmd_to_string(cmd)5�_�   )   +           *   !       ����                                                                                                                                                                                                                                                                                                                                                             ^�{�    �       "   G      -            logger.error("No AMD GPUs found")5�_�   *               +          ����                                                                                                                                                                                                                                                                                                                                                             ^�{�    �         G      D            logger.error("could not run amdmeminfo! e={}".format(e))5�_�                  8   >    ����                                                                                                                                                                                                                                                                                                                            8          8           v        ]�`     �   8   9   J    �   7   9   J      U        memory_types = ["Hynix", "Samsung", "Micron", "Elpida",, "Unknown" "Unknown"]5�_�                     8   I    ����                                                                                                                                                                                                                                                                                                                            8          8           v        ]�`     �   8   9   J    �   7   9   J      `        memory_types = ["Hynix", "Samsung", "Micron", "Elpida",, "Unknown", "Unknown" "Unknown"]5�_�                   8   >    ����                                                                                                                                                                                                                                                                                                                                                             ]�!     �   7   9   J      ?        memory_types = ["Hynix", "Samsung", "Micron", "Elpida"]5�_�                    8       ����                                                                                                                                                                                                                                                                                                                                                             ]�$     �   8   9   J    �   7   9   J      J        memory_types = [, "Unknown""Hynix", "Samsung", "Micron", "Elpida"]5�_�                    8   #    ����                                                                                                                                                                                                                                                                                                                                                             ]�%     �   7   9   J      L        memory_types = [, "Unknown", "Hynix", "Samsung", "Micron", "Elpida"]5�_�                    8       ����                                                                                                                                                                                                                                                                                                                                                             ]�'     �   7   9   J      I        memory_types = "Unknown", "Hynix", "Samsung", "Micron", "Elpida"]5�_�                    8       ����                                                                                                                                                                                                                                                                                                                                                             ]�(     �   7   9   J      K        memory_types = []"Unknown", "Hynix", "Samsung", "Micron", "Elpida"]5�_�                     8       ����                                                                                                                                                                                                                                                                                                                                                             ]�)    �   7   9   J      J        memory_types = ["Unknown", "Hynix", "Samsung", "Micron", "Elpida"]5�_�                    6       ����                                                                                                                                                                                                                                                                                                                                                             ]���     �   5   7   J                  Rx 5700 XT",5��