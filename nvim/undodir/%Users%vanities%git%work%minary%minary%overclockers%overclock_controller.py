Vim�UnDo� WR��4�^d�Y�l�k���z���WNt�9   &   7                mods = amdgpu_mod_factory.get_mod_list(            F       E   F   F    \�Y    _�                            ����                                                                                                                                                                                                                                                                                                                                                             \��C     �         (      *    def mod_gpus(self, overclocked=False):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \��F     �         (      .    def mod_amd_gpus(self, overclocked=False):5�_�                    %       ����                                                                                                                                                                                                                                                                                                                                                             \��J     �   $   &   (          def _mod_gpu(self, mods):5�_�                    %       ����                                                                                                                                                                                                                                                                                                                                                             \��O    �   $   &   (          def _run_gpu(self, mods):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \��b     �         (      #                self._mod.gpu(mods)5�_�      
                     ����                                                                                                                                                                                                                                                                                                                                                             \��h    �         (      (                self._rub_cnds.gpu(mods)5�_�         	       
      +    ����                                                                                                                                                                                                                                                                                                                                                             \���    �         (      -    def mod_amdgpus(self, overclocked=False):5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             \��      �         (                           overclocked,5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \��     �         (      +                    amdgpu_ind[overclocked,5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \��
     �         (      ,                    amdgpu_info[overclocked,5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                             \��     �         (      -                    amdgpu_info["overclocked,5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \��    �         (      /                    amdgpu_info["overclocked"],5�_�                           ����                                                                                                                                                                                                                                                                                                                                         %       v   %    \��     �         (      !                    memory_clock,�         (    5�_�                          ����                                                                                                                                                                                                                                                                                                                                                       \��4     �         (      "                   memory_voltage,�         (    �         (      #                    memory_voltage,   %                    memory_dpm_level,                       core_clock,   !                    core_voltage,   #                    core_dpm_level,                        fan_percent,5�_�                       3    ����                                                                                                                                                                                                                                                                                                                                         $              \��8     �         (      4                   self.amdgpu_info["memory_voltage,5�_�                       4    ����                                                                                                                                                                                                                                                                                                                                         $              \��9     �         (      5                   self.amdgpu_info["memory_voltage=,5�_�                      2    ����                                                                                                                                                                                                                                                                                                                                         $              \��D     �         (      3                    self.amdgpu_info["memory_clock,5�_�                      4    ����                                                                                                                                                                                                                                                                                                                                         $              \��H     �         (      5                   self.amdgpu_info["memory_voltage],5�_�                       5    ����                                                                                                                                                                                                                                                                                                                                         $              \��L     �         (      6                   self.amdgpu_info["memory_dpm_level,5�_�                      /    ����                                                                                                                                                                                                                                                                                                                                         $              \��O     �         (      0                   self.amdgpu_info["core_clock,5�_�                        1    ����                                                                                                                                                                                                                                                                                                                                         $              \��Q     �         (      2                   self.amdgpu_info["core_voltage,5�_�      "                  3    ����                                                                                                                                                                                                                                                                                                                                         $              \��R     �         (      4                   self.amdgpu_info["core_dpm_level,5�_�       #   !       "      0    ����                                                                                                                                                                                                                                                                                                                                         $              \��T     �         (      1                   self.amdgpu_info["fan_percent,5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                                         $              \��W    �               (   import subprocess        from utils import CoinmineLogger       !logger = CoinmineLogger(__name__)           class OverclockController:   8    def __init__(self, amdgpu_info, amdgpu_mod_factory):   &        self.amdgpu_info = amdgpu_info   4        self.amdgpu_mod_factory = amdgpu_mod_factory           def mod_amdgpus(self):           if self.amdgpu_info:               adapter_num = 0   -            for gpu_info in self.amdgpu_info:   <                mods = self.amdgpu_mod_factory.get_mod_list(                        adapter_num,   4                    self.amdgpu_info["overclocked"],   5                    self.amdgpu_info["memory_clock"],   6                   self.amdgpu_info["memory_voltage"],   8                   self.amdgpu_info["memory_dpm_level"],   2                   self.amdgpu_info["core_clock"],   4                   self.amdgpu_info["core_voltage"],   6                   self.amdgpu_info["core_dpm_level"],   3                   self.amdgpu_info["fan_percent"],                   )   (                self._run_cmds.gpu(mods)                       logger.info(   E                    "modified amd adapter_num={} gpu_info={}".format(   -                        adapter_num, gpu_info                       )                   )                    adapter_num += 1           def _run_cmds(self, mods):           for mod in mods:   +            subprocess.run(mod, shell=True)   5            logger.info("running mod={}".format(mod))5�_�   #   %           $   %       ����                                                                                                                                                                                                                                                                                                                                         $              \��x     �   $   &   (          def _run_cmds(self, mods):5�_�   $   &           %   %       ����                                                                                                                                                                                                                                                                                                                                         $              \��y     �   $   &   (          def _run_cmds(smods):5�_�   %   '           &   $        ����                                                                                                                                                                                                                                                                                                                                         $              \��z     �   $   &   )       �   $   &   (    5�_�   &   (           '   %       ����                                                                                                                                                                                                                                                                                                                                         $              \���    �   $   &   )          @staticmethid5�_�   '   )           (   )   !    ����                                                                                                                                                                                                                                                                                                                                         $              \���    �   (              5            logger.info("running mod={}".format(mod))5�_�   (   *           )          ����                                                                                                                                                                                                                                                                                                                               (          (       V   (    \���     �         )                           adapter_num,5�_�   )   +           *      $    ����                                                                                                                                                                                                                                                                                                                               (          (       V   (    \���     �         )      0                    self.amdgpu_infoadapter_num,5�_�   *   ,           +      1    ����                                                                                                                                                                                                                                                                                                                               (          (       V   (    \���     �         )      2                    self.amdgpu_info["adapter_num,5�_�   +   -           ,          ����                                                                                                                                                                                                                                                                                                                               (          (       V   (    \���     �                            adapter_num = 05�_�   ,   .           -   "       ����                                                                                                                                                                                                                                                                                                                               (          (       V   (    \���     �   !   "                           adapter_num += 15�_�   -   /           .          ����                                                                                                                                                                                                                                                                                                                               (          (       V   (    \���     �          '      -                        adapter_num, gpu_info5�_�   .   0           /      (    ����                                                                                                                                                                                                                                                                                                                               (          (       V   (    \���   	 �          '      2                        self.adapter_num, gpu_info5�_�   /   1           0          ����                                                                                                                                                                                                                                                                                                                               (          (       V   (    \��   
 �         '          def mod_amdgpus(self):5�_�   0   2           1   	   "    ����                                                                                                                                                                                                                                                                                                                               (          (       V   (    \�-     �      
   '      8    def __init__(self, amdgpu_info, amdgpu_mod_factory):5�_�   1   3           2   	   $    ����                                                                                                                                                                                                                                                                                                                               (          (       V   (    \�4     �      
   '      :    def __init__(self, amdgpu_info{}, amdgpu_mod_factory):5�_�   2   4           3   	   9    ����                                                                                                                                                                                                                                                                                                                               (          (       V   (    \�=    �      
   '      ;    def __init__(self, amdgpu_info=[], amdgpu_mod_factory):5�_�   3   5           4          ����                                                                                                                                                                                                                                                                                                                                      	          v       \�    �      	   '      class OverclockController:5�_�   4   6           5          ����                                                                                                                                                                                                                                                                                                                                      	          v       \�)     �         '          def mod_gpus(self):5�_�   5   7           6      !    ����                                                                                                                                                                                                                                                                                                                                      	          v       \�2     �         '      -            for gpu_info in self.amdgpu_info:5�_�   6   8           7   
       ����                                                                                                                                                                                                                                                                                                                                      	          v       \�4     �   	   
          &        self.amdgpu_info = amdgpu_info5�_�   7   9           8   	       ����                                                                                                                                                                                                                                                                                                                                      	          v       \�8     �      
   &      @    def __init__(self, amdgpu_info=[], amdgpu_mod_factory=None):5�_�   8   :           9   	       ����                                                                                                                                                                                                                                                                                                                                      	          v       \�9    �               &   import subprocess        from utils import CoinmineLogger       !logger = CoinmineLogger(__name__)           class GPUModController:   1    def __init__(self,  amdgpu_mod_factory=None):   4        self.amdgpu_mod_factory = amdgpu_mod_factory       $    def mod_gpus(self, amdgpu_info):           if self.amdgpu_info:   (            for gpu_info in amdgpu_info:   <                mods = self.amdgpu_mod_factory.get_mod_list(   4                    self.amdgpu_info["adapter_num"],   4                    self.amdgpu_info["overclocked"],   5                    self.amdgpu_info["memory_clock"],   7                    self.amdgpu_info["memory_voltage"],   9                    self.amdgpu_info["memory_dpm_level"],   3                    self.amdgpu_info["core_clock"],   5                    self.amdgpu_info["core_voltage"],   7                    self.amdgpu_info["core_dpm_level"],   4                    self.amdgpu_info["fan_percent"],                   )   (                self._run_cmds.gpu(mods)                       logger.info(   E                    "modified amd adapter_num={} gpu_info={}".format(   A                        self.amdgpu_info["adapter_num"], gpu_info                       )                   )           @staticmethod       def _run_cmds(mods):           for mod in mods:   +            subprocess.run(mod, shell=True)   =            logger.info("running cmd for mod={}".format(mod))5�_�   9   ;           :          ����                                                                                                                                                                                                                                                                                                                                                v       \�=     �         &      <                mods = self.amdgpu_mod_factory.get_mod_list(5�_�   :   <           ;          ����                                                                                                                                                                                                                                                                                                                                                v       \�?     �         &      4                    self.amdgpu_info["adapter_num"],5�_�   ;   =           <          ����                                                                                                                                                                                                                                                                                                                                                v       \�?     �         &      4                    self.amdgpu_info["overclocked"],5�_�   <   >           =          ����                                                                                                                                                                                                                                                                                                                                                v       \�@     �         &      5                    self.amdgpu_info["memory_clock"],5�_�   =   ?           >          ����                                                                                                                                                                                                                                                                                                                                                v       \�@     �         &      7                    self.amdgpu_info["memory_voltage"],5�_�   >   @           ?          ����                                                                                                                                                                                                                                                                                                                                                v       \�A     �         &      9                    self.amdgpu_info["memory_dpm_level"],5�_�   ?   A           @          ����                                                                                                                                                                                                                                                                                                                                                v       \�A     �         &      3                    self.amdgpu_info["core_clock"],5�_�   @   B           A          ����                                                                                                                                                                                                                                                                                                                                                v       \�B     �         &      5                    self.amdgpu_info["core_voltage"],5�_�   A   C           B          ����                                                                                                                                                                                                                                                                                                                                                v       \�C     �         &      7                    self.amdgpu_info["core_dpm_level"],5�_�   B   D           C          ����                                                                                                                                                                                                                                                                                                                                                v       \�C     �         &      4                    self.amdgpu_info["fan_percent"],5�_�   C   E           D          ����                                                                                                                                                                                                                                                                                                                                                v       \�F     �         &              if self.amdgpu_info:5�_�   D   F           E          ����                                                                                                                                                                                                                                                                                                                                                v       \�I    �         &      A                        self.amdgpu_info["adapter_num"], gpu_info5�_�   E               F          ����                                                                                                                                                                                                                                                                                                                                                v       \�X    �         &      7                mods = amdgpu_mod_factory.get_mod_list(5�_�               "   !      /    ����                                                                                                                                                                                                                                                                                                                                         $              \��S     �         (      3                   self.amdgpu_info["fan_percen"]t,5�_�                       .    ����                                                                                                                                                                                                                                                                                                                                         $              \��N     �         (      2                   self.amdgpu_info["core_cloc"]k,5�_�                       4    ����                                                                                                                                                                                                                                                                                                                                         $              \��G     �         (      7                   self.amdgpu_info["memory_voltage]"],5�_�                      6    ����                                                                                                                                                                                                                                                                                                                                         $              \��=     �         (      6                   self.amdgpu_info["memory_dpm_level]5�_�                       5    ����                                                                                                                                                                                                                                                                                                                                         $              \��<     �         (      6                   self.amdgpu_info["memory_dpm_leve],5�_�                          ����                                                                                                                                                                                                                                                                                                                                                          \��(     �         (      "                   memory_voltage,   $                   memory_dpm_level,                      core_clock,                       core_voltage,   "                   core_dpm_level,                      fan_percent,�         (    �         (      m   m   c   c   c   f5�_�                          ����                                                                                                                                                                                                                                                                                                                                                          \��!     �         (      "                    emory_voltage,   $                    emory_dpm_level,                       ore_clock,                        ore_voltage,   "                    ore_dpm_level,                       an_percent,�         (    �         (                           5�_�                           ����                                                                                                                                                                                                                                                                                                                                         $              \��     �         (      "                   memory_voltage,   6                   self.amdgpu_info["memory_dpm_level,   0                   self.amdgpu_info["core_clock,   2                   self.amdgpu_info["core_voltage,   4                   self.amdgpu_info["core_dpm_level,   1                   self.amdgpu_info["fan_percent,�         (    �         (      4                   self.amdgpu_info["memory_voltage,5�_�             
   	          ����                                                                                                                                                                                                                                                                                                                                                             \���     �         (       5�_�              	             ����                                                                                                                                                                                                                                                                                                                                                             \���     �         (       5��