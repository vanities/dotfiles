Vim�UnDo� 4/'���_"[Z�d�\i:�<�9�b��N����          def _get_cpu_info(self):            A       A   A   A    ^`!    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ^`^     �                   �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^`_     �                  5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^`c     �         7      class Lspci:5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             ^`j     �      
   7              self.base_cmd = "lspci"5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             ^`\     �   	      7      <        self.detailed_cmd = "{} -mmvv".format(self.base_cmd)5�_�                    
   )    ����                                                                                                                                                                                                                                                                                                                                                             ^``    �   
      7    �   
      7    �   	      7      @        self.detailed_cpu_cmd = "{} -mmvv".format(self.base_cmd)5�_�                            ����                                                                                                                                                                                                                                                                                                                                          "       v   "    ^`~     �         8    �         8    5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                       P          V       ^`�     �             2   class Lscpu:       def __init__(self):           self.base_cmd = "lscpu"   ;        self.detailed_cpu_cmd = "{} ".format(self.base_cmd)   0lscpu --json --extended=CPU,SOCKET,MAXMHZ,MINMHZ   4        self.supported_gpus = ["RX", "Vega", "6fdf"]       0    def check_integrated_graphics_enabled(self):           vgas = self.find_vgas()           for vga in vgas:   +            supported_graphics_card = False   +            for gpu in self.supported_gpus:                   if gpu in vga:   2                    supported_graphics_card = True   +            if not supported_graphics_card:   J                logger.info("Integrated Graphics detected={}".format(vga))                   return True           return False           def find_vgas(self):           vgas = []   3        lspci = self._get_base_output().split("\n")           for pci in lspci:   ;            if "VGA" in pci or "Display controller" in pci:                    vgas.append(pci)           return vgas       #    def get_wifi_device_info(self):   ,        output = self._get_detailed_output()           matches = re.findall(   +            r"Class:.*Network controller\n"               "Vendor:\t(.*)\n"               "Device:\t(.*)\n"               "SVendor:\t(.*)\n"               "SDevice:\t(.*)",               output,               re.MULTILINE,   	        )           return {   $            "vendor": matches[0][0],   $            "device": matches[0][1],   (            "sub_vendor": matches[0][2],   (            "sub_device": matches[0][3],   	        }           def _get_base_output(self):   6        return Converters.cmd_to_string(self.base_cmd)       #    def _get_detailed_output(self):   :        return Converters.cmd_to_string(self.detailed_cmd)5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                 V       ^`�     �               class Lsblk:5�_�   	              
   	       ����                                                                                                                                                                                                                                                                                                                                                 V       ^`�     �      
                 self.base_cmd = "lsblk"5�_�   
                 
       ����                                                                                                                                                                                                                                                                                                                                                 V       ^`�     �   	                     args = "--json --output"5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V       ^`�     �   
                    output_columns = (5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V       ^`�     �   
                    cpu_output_columns = (5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V       ^`�     �               P            "NAME,UUID,TYPE,SIZE,MOUNTPOINT,SERIAL,MODEL,VENDOR,PARTUUID,FSUSE%"5�_�                       0    ����                                                                                                                                                                                                                                                                                                                                                 V       ^`�     �               s            "--extended=CPU,SOCKET,MAXMHZ,MINMHZNAME,UUID,TYPE,SIZE,MOUNTPOINT,SERIAL,MODEL,VENDOR,PARTUUID,FSUSE%"5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                 V       ^`�    �   	                     = "--json --output"5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                 V       ^`�     �   	                     = "--json"5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                 V       ^`�     �   	                    self. = "--json"5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V       ^`
     �             �             5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                   V       ^`     �   	   
          (        self.detailed_cpu_cmd = "--json"5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                 V       ^`     �               (        self.detailed_cpu_cmd = "--json"5�_�                       *    ����                                                                                                                                                                                                                                                                                                                                                 V       ^`     �               +        self.detailed_cpu_cmd = "{} --json"5�_�                       .    ����                                                                                                                                                                                                                                                                                                                                                 V       ^`     �               .        self.detailed_cpu_cmd = "{} --json {}"5�_�                       T    ����                                                                                                                                                                                                                                                                                                                                                 V       ^`&    �                  	import re   ,from utils import CoinmineLogger, Converters       !logger = CoinmineLogger(__name__)           class Lscpu:       def __init__(self):           self.base_cmd = "lscpu"           cpu_columns = (   1            "--extended=CPU,SOCKET,MAXMHZ,MINMHZ"   	        )   V        self.detailed_cpu_cmd = "{} --json {}".format(self.base_cmd, self.cpu_columns)   I        self.cmd = "{} {} {}".format(self.base_cmd, args, output_columns)       $    def get_block_device_info(self):   7        block_devices = Converters.json_string_to_dict(   .            Converters.cmd_to_string(self.cmd)           )["blockdevices"]            for bd in block_devices:               del bd["fsuse%"]                del bd["mountpoint"]               del bd["uuid"]               del bd["partuuid"]   ,            for partition in bd["children"]:   &                del partition["model"]   '                del partition["serial"]   '                del partition["vendor"]   C                partition["percent_used"] = partition.pop("fsuse%")           return block_devices5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V       ^`)    �                I        self.cmd = "{} {} {}".format(self.base_cmd, args, output_columns)5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                 V       ^`2     �      
                 self.base_cmd = "lscpu"5�_�                       J    ����                                                                                                                                                                                                                                                                                                                                                 V       ^`@     �   
            V        self.detailed_cpu_cmd = "{} --json {}".format(self.base_cmd, self.cpu_columns)5�_�                       ;    ����                                                                                                                                                                                                                                                                                                                                                 V       ^`B    �   
            Q        self.detailed_cpu_cmd = "{} --json {}".format(self.base_cmd, cpu_columns)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V       ^`u    �               $    def get_block_device_info(self):5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V       ^`�    �                 	import re5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V       ^`�     �                     �               5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                                 V       ^`�     �               �                     def _get_cpu_info(self)5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �              �             5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �                7        block_devices = Converters.json_string_to_dict(5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �                *         = Converters.json_string_to_dict(5�_�   #   %           $      *    ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �                .            Converters.cmd_to_string(self.cmd)5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �                         )["blockdevices"]5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �                         )["cpu"]5�_�   &   (           '          ����                                                                                                                                                                                                                                                                                                                                                V       ^`�   	 �                   ,from utils import CoinmineLogger, Converters       !logger = CoinmineLogger(__name__)           class Lscpu:       def __init__(self):           base_cmd = "lscpu"   ;        cpu_columns = "--extended=CPU,SOCKET,MAXMHZ,MINMHZ"   L        self.detailed_cpu_cmd = "{} --json {}".format(base_cmd, cpu_columns)           def get_cpu_info(self):   7        block_devices = Converters.json_string_to_dict(   .            Converters.cmd_to_string(self.cmd)           )["blockdevices"]            for bd in block_devices:               del bd["fsuse%"]                del bd["mountpoint"]               del bd["uuid"]               del bd["partuuid"]   ,            for partition in bd["children"]:   &                del partition["model"]   '                del partition["serial"]   '                del partition["vendor"]   C                partition["percent_used"] = partition.pop("fsuse%")           return block_devices           def _get_cpu_info(self):   .        info = Converters.json_string_to_dict(   ;            Converters.cmd_to_string(self.detailed_cpu_cmd)           )["cpus"]    5�_�   '   )           (           ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �             
            for bd in block_devices:               del bd["fsuse%"]                del bd["mountpoint"]               del bd["uuid"]               del bd["partuuid"]   ,            for partition in bd["children"]:   &                del partition["model"]   '                del partition["serial"]   '                del partition["vendor"]   C                partition["percent_used"] = partition.pop("fsuse%")5�_�   (   *           )          ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �                       )["blockdevices"]5�_�   )   +           *          ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �                       )[""]5�_�   *   ,           +          ����                                                                                                                                                                                                                                                                                                                                                V       ^`     �                         �               5�_�   +   -           ,          ����                                                                                                                                                                                                                                                                                                                                                V       ^`"     �               .        info = Converters.json_string_to_dict(5�_�   ,   .           -          ����                                                                                                                                                                                                                                                                                                                                                V       ^`'     �                         for cpus5�_�   -   /           .           ����                                                                                                                                                                                                                                                                                                                                                V       ^`.     �                  5�_�   .   0           /          ����                                                                                                                                                                                                                                                                                                                                                V       ^`�   
 �                           �             5�_�   /   1           0          ����                                                                                                                                                                                                                                                                                                                                                V       ^`e     �                           �             5�_�   0   2           1          ����                                                                                                                                                                                                                                                                                                                                                V       ^`x     �                           cpu["core"]5�_�   1   3           2      $    ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �               $            cpu["core"] = cpu["cpu"]5�_�   2   4           3      %    ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �             �             5�_�   3   5           4          ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �               (            cpu["core"] = cpu.pop("cpu")5�_�   4   6           5          ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �               ,            cpu["max_mhzx"] = cpu.pop("cpu")5�_�   5   7           6      )    ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �               +            cpu["max_mhz"] = cpu.pop("cpu")5�_�   6   8           7      +    ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �             �             5�_�   7   9           8          ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �               .            cpu["max_mhz"] = cpu.pop("maxmhz")5�_�   8   :           9      )    ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �               .            cpu["min_mhz"] = cpu.pop("maxmhz")5�_�   9   ;           :      (    ����                                                                                                                                                                                                                                                                                                                                                V       ^`�     �             �             5�_�   :   =           ;          ����                                                                                                                                                                                                                                                                                                                                                V       ^`      �               .            cpu["min_mhz"] = cpu.pop("minmhz")5�_�   ;   >   <       =          ����                                                                                                                                                                                                                                                                                                                                                V       ^`    �                '            cpu[""] = cpu.pop("minmhz")5�_�   =   ?           >          ����                                                                                                                                                                                                                                                                                                                                                V       ^`     �                            print(cpu)5�_�   >   @           ?          ����                                                                                                                                                                                                                                                                                                                                                V       ^`     �                (            cpu["core"] = cpu.pop("cpu")5�_�   ?   A           @           ����                                                                                                                                                                                                                                                                                                                                                 V       ^`!     �   
                     def get_cpu_info(self):   7        block_devices = Converters.json_string_to_dict(   .            Converters.cmd_to_string(self.cmd)           )["cpus"]           return block_devices5�_�   @               A          ����                                                                                                                                                                                                                                                                                                                                                 V       ^`!    �                   def _get_cpu_info(self):5�_�   ;           =   <          ����                                                                                                                                                                                                                                                                                                                                                V       ^`     �                5��