Vim�UnDo� Ji������H5��\��@�ExG�7��   :           P      E       E   E   E    \��   * _�                     9       ����                                                                                                                                                                                                                                                                                                                                                             \���    �   9                      �   9            5�_�                    3   $    ����                                                                                                                                                                                                                                                                                                                                                             \���     �   2   4   :      $                gpu_info["amd_type"]5�_�                   6   '    ����                                                                                                                                                                                                                                                                                                                                                             \��    �   5   7   :      '                gpu_info["memory_type"]5�_�                    5   *    ����                                                                                                                                                                                                                                                                                                                                                             \���    �   4   6   :      :            if re.search(gpu, memory_types, re.MULTILINE):5�_�                    8   S    ����                                                                                                                                                                                                                                                                                                                                                             \���     �   7   9   :      V            re.findall(r"Memory Model.*", amdmeminfo, re.MULTILINE).strip().split()[3]5�_�                    8   B    ����                                                                                                                                                                                                                                                                                                                                                             \���    �               :   	import re   import shlex   import subprocess        from utils import CoinmineLogger       !logger = CoinmineLogger(__name__)           class AmdMemInfo:   (    def __init__(self, amdmeminfo_path):   .        self.amdmeminfo_path = amdmeminfo_path           def get_all_gpu_info(self):           all_gpu_info = []           try:   1            amdmeminfo = subprocess.check_output(   J                shlex.split("{} --no-opencl".format(self.amdmeminfo_path))               ).decode("utf-8")   P            split_info = amdmeminfo.split("-----------------------------------")                   adapter_num = 0   #            for line in split_info:   9                gpu_info = AmdMemInfo._get_gpu_info(line)                   if gpu_info:                        logger.info(   F                        "AMD GPU found adapter_num={} type={}".format(   1                            adapter_num, gpu_info                           )                       )   1                    all_gpu_info.append(gpu_info)           except Exception as e:   D            logger.error("could not run amdmeminfo! e={}".format(e))               if not all_gpu_info:   ,            logger.warn("No AMD GPUs found")           return all_gpu_info       %    def get_num_of_amd_devices(self):   +        return len(self.get_all_gpu_info())           # helpers       @staticmethod   "    def _get_gpu_info(amdmeminfo):           gpu_info = {}   (        amd_types = ["RX 580", "RX 570"]   ?        memory_types = ["Hynix", "Samsung", "Micron", "Elpida"]               for gpu in amd_types:   8            if re.search(gpu, amdmeminfo, re.MULTILINE):   *                gpu_info["amd_type"] = gpu            for gpu in memory_types:   8            if re.search(gpu, amdmeminfo, re.MULTILINE):   -                gpu_info["memory_type"] = gpu   %        gpu_info["memory_serial"] = (   F            re.findall(r"Memory Model.*", amdmeminfo, re.MULTILINE)[3]   	        )           return gpu_info5�_�      	              9   	    ����                                                                                                                                                                                                                                                                                                                                                             \��    �   8   :   :              )[3]5�_�      
           	   9       ����                                                                                                                                                                                                                                                                                                                                                             \��2    �   8   :   :              )[0].split()[3]5�_�   	              
   (   *    ����                                                                                                                                                                                                                                                                                                                                                             \��     �   '   )   :      +        return len(self.get_all_gpu_info())5�_�   
                 (   0    ����                                                                                                                                                                                                                                                                                                                                                             \��    �   '   )   :      1        return len(self.get_all_gpu_info.items())5�_�                    '       ����                                                                                                                                                                                                                                                                                                                                                             \���     �   &   (   :      %    def get_num_of_amd_devices(self):5�_�                    '       ����                                                                                                                                                                                                                                                                                                                                                             \���    �   &   (   :      !    def get_num_of_devices(self):5�_�                    9       ����                                                                                                                                                                                                                                                                                                                                                             \��   	 �   8   :   :              )[0].split()[4]5�_�                   6       ����                                                                                                                                                                                                                                                                                                                            7          9          v       \��     �   6   8   ;       �   6   8   :    5�_�                    7       ����                                                                                                                                                                                                                                                                                                                            8          :          v       \���     �   6   :   ;      		print(�   7   8   ;    5�_�                    9       ����                                                                                                                                                                                                                                                                                                                            :          <          v       \���    �   8   :   =              )[0].split()5�_�                    7       ����                                                                                                                                                                                                                                                                                                                            :          <          v       \���     �   6   8   =      /		print(gpu_info["memory_serial"] = re.findall(   7            r"Memory Model.*", amdmeminfo, re.MULTILINE5�_�                    7   0    ����                                                                                                                                                                                                                                                                                                                            9          ;          v       \���     �   6   8   <      [		print(gpu_info["memory_serial"] = re.findall( r"Memory Model.*", amdmeminfo, re.MULTILINE5�_�                   7        ����                                                                                                                                                                                                                                                                                                                            9          ;          v       \���     �   6   8   <      Z		print(gpu_info["memory_serial"] = re.findall(r"Memory Model.*", amdmeminfo, re.MULTILINE           )[0].split())5�_�                    7   g    ����                                                                                                                                                                                                                                                                                                                            8          :          v       \���     �   6   8   ;      g		print(gpu_info["memory_serial"] = re.findall(r"Memory Model.*", amdmeminfo, re.MULTILINE)[0].split())5�_�                    7   $    ����                                                                                                                                                                                                                                                                                                                            8          :          v       \���    �   6   8   ;      h		print(gpu_info["memory_serial"] = re.findall(r"Memory Model.*", amdmeminfo, re.MULTILINE)[0].split()))5�_�                    7   L    ����                                                                                                                                                                                                                                                                                                                            8          :          v       \���    �   6   8   ;      L		print(re.findall(r"Memory Model.*", amdmeminfo, re.MULTILINE)[0].split()))5�_�                    6   ,    ����                                                                                                                                                                                                                                                                                                                            8          :          v       \���     �   5   7   ;      -                gpu_info["memory_type"] = gpu   K		print(re.findall(r"Memory Model.*", amdmeminfo, re.MULTILINE)[0].split())5�_�                    6   .    ����                                                                                                                                                                                                                                                                                                                            7          9          v       \���    �   5   8   :      w                gpu_info["memory_type"] = gpu print(re.findall(r"Memory Model.*", amdmeminfo, re.MULTILINE)[0].split())5�_�                    7        ����                                                                                                                                                                                                                                                                                                                            8          :          v       \��    �   6   8   ;      Iprint(re.findall(r"Memory Model.*", amdmeminfo, re.MULTILINE)[0].split())5�_�                    7       ����                                                                                                                                                                                                                                                                                                                            8          :          v       \��     �   6   8   ;      K		print(re.findall(r"Memory Model.*", amdmeminfo, re.MULTILINE)[0].split())5�_�                     7   	    ����                                                                                                                                                                                                                                                                                                                            8          :          v       \��    �   6   8   ;      R         print(re.findall(r"Memory Model.*", amdmeminfo, re.MULTILINE)[0].split())5�_�      !               7       ����                                                                                                                                                                                                                                                                                                                            8          :          v       \��X    �   6   7          Q        print(re.findall(r"Memory Model.*", amdmeminfo, re.MULTILINE)[0].split())5�_�       "           !   9       ����                                                                                                                                                                                                                                                                                                                            7          9          v       \��[     �   9   ;   ;       �   9   ;   :    5�_�   !   #           "   :       ����                                                                                                                                                                                                                                                                                                                            7          9          v       \��d    �   9   ;   ;      		print(gpu_info)5�_�   "   $           #   $       ����                                                                                                                                                                                                                                                                                                                            7          9          v       \��f     �   $   &   <       �   $   &   ;    5�_�   #   %           $   %       ����                                                                                                                                                                                                                                                                                                                            8          :          v       \��l     �   $   &   <      		print(all5�_�   $   &           %   ;       ����                                                                                                                                                                                                                                                                                                                            8          :          v       \��o    �   :   ;                  print(gpu_info)5�_�   %   '           &   %       ����                                                                                                                                                                                                                                                                                                                            8          :          v       \��r     �   $   &   ;      		print(all_gpu_info)5�_�   &   (           '   %       ����                                                                                                                                                                                                                                                                                                                            8          :          v       \��t    �   $   &   ;             print(all_gpu_info)5�_�   '   -           (          ����                                                                                                                                                                                                                                                                                                                                                             \���    �      !   <                          �      !   ;    5�_�   (   .   )       -          ����                                                                                                                                                                                                                                                                                                                                                             \��v    �         =                      �         <    5�_�   -   /           .           ����                                                                                                                                                                                                                                                                                                                                                             \��|    �         =      !                print(split_info)5�_�   .   0           /          ����                                                                                                                                                                                                                                                                                                                                                             \��b    �         >                  �         =    5�_�   /   1           0   =       ����                                                                                                                                                                                                                                                                                                                                                             \���     �   =   ?   ?              �   =   ?   >    5�_�   0   2           1   >       ����                                                                                                                                                                                                                                                                                                                                                             \���     �   =   ?   ?              print(gpu_ifno)5�_�   1   3           2   :       ����                                                                                                                                                                                                                                                                                                                                                             \���     �   :   <   ?    �   :   ;   ?    5�_�   2   4           3   7       ����                                                                                                                                                                                                                                                                                                                                                             \���     �   7   9   @    �   7   8   @    5�_�   3   5           4   4        ����                                                                                                                                                                                                                                                                                                                                                             \���    �   4   6   A    �   4   5   A    5�_�   4   6           5           ����                                                                                                                                                                                                                                                                                                                                                             \��     �       "   B    �       !   B    5�_�   5   7           6   !       ����                                                                                                                                                                                                                                                                                                                                                             \��     �       !          #                    print(gpu_info)5�_�   6   8           7          ����                                                                                                                                                                                                                                                                                                                                                             \��     �         B    �         B    5�_�   7   9           8           ����                                                                                                                                                                                                                                                                                                                                                V       \��   ! �         C      #                    print(gpu_info)5�_�   8   :           9          ����                                                                                                                                                                                                                                                                                                                                                V       \���   % �         C                  ).decode("utf-8")5�_�   9   ;           :      "    ����                                                                                                                                                                                                                                                                                                                                                V       \� �   & �         C      #            ).decode("utf-8")[0:-1]5�_�   :   <           ;          ����                                                                                                                                                                                                                                                                                                                                                V       \� �     �                                print(gpu_info)5�_�   ;   =           <          ����                                                                                                                                                                                                                                                                                                                                                V       \� �     �                                print(line)5�_�   <   >           =   !       ����                                                                                                                                                                                                                                                                                                                                                V       \� �   ' �       !          #                    print(gpu_info)5�_�   =   ?           >          ����                                                                                                                                                                                                                                                                                                                                                V       \�     �         @      !            ).decode("utf-8")[1:]5�_�   >   @           ?      P    ����                                                                                                                                                                                                                                                                                                                                                V       \�   ( �         @      P            split_info = amdmeminfo.split("-----------------------------------")�         @    5�_�   ?   A           @          ����                                                                                                                                                                                                                                                                                                                                                V       \�8   ) �                            print(split_info)5�_�   @   B           A   %       ����                                                                                                                                                                                                                                                                                                                                                V       \�~     �   $   %                  print(all_gpu_info)5�_�   A   C           B   =       ����                                                                                                                                                                                                                                                                                                                                                V       \��     �   <   =                  print(gpu_info)5�_�   B   D           C   9       ����                                                                                                                                                                                                                                                                                                                                                V       \��     �   8   9                  print(gpu_info)5�_�   C   E           D   5       ����                                                                                                                                                                                                                                                                                                                                                V       \��     �   4   5                  print(gpu_info)5�_�   D               E   1       ����                                                                                                                                                                                                                                                                                                                                                V       \��   * �   0   1                  print(gpu_info)5�_�   (   *       -   )   ;       ����                                                                                                                                                                                                                                                                                                                                                             \���    �   ;   <   <              �   ;   =   =              print(gpu_info)5�_�   )   +           *   8       ����                                                                                                                                                                                                                                                                                                                                                             \��    �   8   9   =    �   8   9   =              print(gpu_info)5�_�   *   ,           +   5       ����                                                                                                                                                                                                                                                                                                                                                             \��$    �   5   6   >    �   5   6   >              print(gpu_info)5�_�   +               ,   2        ����                                                                                                                                                                                                                                                                                                                                                             \��T    �   2   3   ?    �   2   3   ?              print(gpu_info)5�_�                   7   .    ����                                                                                                                                                                                                                                                                                                                            8          :          v       \���     �   6   9   <      g		print(gpu_info["memory_serial"] = re.findall(r"Memory Model.*", amdmeminfo, re.MULTILINE)[0].split())5�_�                     7   g    ����                                                                                                                                                                                                                                                                                                                            8          :          v       \���    �   6   8   ;      f		print(gpu_info["memory_serial"] = re.findall(r"Memory Model.*", amdmeminfo, re.MULTILINE)[0].split()5�_�                    6       ����                                                                                                                                                                                                                                                                                                                            9          ;          v       \��     �   6   7   :    �   5   7   :      0         gpu_info["memory_serial"] = re.findall(   7            r"Memory Model.*", amdmeminfo, re.MULTILINE   8        )[0].split()       gpu_info["memory_type"] = gpu5�_�                    6   &    ����                                                                                                                                                                                                                                                                                                                                                             \��     �   6   7   :    �   6   7   :      a5��