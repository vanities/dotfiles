Vim�UnDo� Bܲ�����f�oF�i4UڌpK�Q:}bn���f      N        self.overclock_controller.overclock_gpus("ethereum", overclocked=True)      0      ;       ;   ;   ;    \�g�    _�                     
       ����                                                                                                                                                                                                                                                                                                                                                             \ٲ     �   	            ,        self.amd_gpus = ["RX 570", "RX 580"]5�_�                    
   $    ����                                                                                                                                                                                                                                                                                                                                                             \ٲ     �   	            8        self.amd_gpus = [{"amd_type"}"RX 570", "RX 580"]5�_�                    
   $    ����                                                                                                                                                                                                                                                                                                                                                             \ٲ     �   	            /        self.amd_gpus = [{"amd_type", "RX 580"]�   
          5�_�                    
   &    ����                                                                                                                                                                                                                                                                                                                                                             \ٲ     �   	            :        self.amd_gpus = [{"amd_type": }"RX 570", "RX 580"]5�_�                    
   .    ����                                                                                                                                                                                                                                                                                                                                                             \ٲ     �   	            9        self.amd_gpus = [{"amd_type": "RX 570", "RX 580"]5�_�                    
   1    ����                                                                                                                                                                                                                                                                                                                                                             \ٲ     �   	            :        self.amd_gpus = [{"amd_type": "RX 570"}, "RX 580"]5�_�                    
   4    ����                                                                                                                                                                                                                                                                                                                                                             \ٲ      �   	            >        self.amd_gpus = [{"amd_type": "RX 570"}, {""}"RX 580"]5�_�      	              
   4    ����                                                                                                                                                                                                                                                                                                                                                             \ٲ!     �   	            =        self.amd_gpus = [{"amd_type": "RX 570"}, {"}"RX 580"]5�_�      
           	   
   F    ����                                                                                                                                                                                                                                                                                                                                                             \ٲ*    �   	            G        self.amd_gpus = [{"amd_type": "RX 570"}, {"amd_type": "RX 580"]5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                                             \��     �             �             5�_�   
                    :    ����                                                                                                                                                                                                                                                                                                                                                             \��     �               <    @mock.patch("overclockers.AMD_RX500.set_default_clocks")5�_�                       S    ����                                                                                                                                                                                                                                                                                                                                                             \��     �               U    def test_overclock_controller_disabled_overclocks(self, mock_run, mock_defaults):5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                             \�     �               �               5�_�                       %    ����                                                                                                                                                                                                                                                                                                                                                             \�     �                 -        self.assertTrue(mock_defaults.called)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \�    �                  #from unittest import TestCase, mock       >from overclockers import OverclockFactory, OverclockController           (class TestOverclockController(TestCase):       def setUp(self):       O        self.overclock_factory = OverclockFactory(None, None, None, None, None)   H        self.amd_gpus = [{"amd_type": "RX 570"}, {"amd_type": "RX 580"}]   8        self.overclock_controller = OverclockController(   1            self.amd_gpus, self.overclock_factory   	        )       9    @mock.patch("overclockers.OverclockFactory.run_cmds")   K    def test_overclock_gpus_overclocks_mixed_multiple_gpus(self, mock_run):   N        self.overclock_controller.overclock_gpus("ethereum", overclocked=True)   9        mock_run.assert_any_call("ethereum", "RX 570", 0)   9        mock_run.assert_any_call("ethereum", "RX 580", 1)       1    @mock.patch("overclockers.AMD_RX500.set_fan")   <    @mock.patch("overclockers.AMD_RX500.set_default_clocks")   9    @mock.patch("overclockers.OverclockFactory.run_cmds")   _    def test_overclock_controller_disabled_overclocks(self, mock_run, mock_defaults, mock_fan):   3        overclock_controller = OverclockController(   1            self.amd_gpus, self.overclock_factory   	        )   J        overclock_controller.overclock_gpus("ethereum", overclocked=False)   )        self.assertFalse(mock_run.called)   -        self.assertTrue(mock_defaults.called)   (        self.assertTrue(mock_fan.called)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \�     �         !    �         !    5�_�                       I    ����                                                                                                                                                                                                                                                                                                                                                             \�     �         "      K    def test_overclock_gpus_overclocks_mixed_multiple_gpus(self, mock_run):5�_�                       '    ����                                                                                                                                                                                                                                                                                                                                                             \�)    �         "    �         "    5�_�                       3    ����                                                                                                                                                                                                                                                                                                                                                             \��     �         #      9    @mock.patch("overclockers.OverclockFactory.run_cmds")5�_�                       ;    ����                                                                                                                                                                                                                                                                                                                                                             \��    �         #      =    @mock.patch("overclockers.OverclockFactory.run_all_cmds")5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                             \��Z     �         #      9        mock_run.assert_any_call("ethereum", "RX 570", 0)5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                             \��]    �         #      9        mock_run.assert_any_call("ethereum", "RX 580", 1)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \��     �         #    �         #    5�_�                       /    ����                                                                                                                                                                                                                                                                                                                                                             \��     �         $      1    @mock.patch("overclockers.AMD_RX500.set_fan")5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             \��(    �                >    @mock.patch("overclockers.DynamicPowerManagement.set_dpm")5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \��     �                1    @mock.patch("overclockers.AMD_RX500.set_fan")5�_�                       I    ����                                                                                                                                                                                                                                                                                                                                                             \��     �         "      U    def test_overclock_gpus_overclocks_mixed_multiple_gpus(self, mock_run, mock_fan):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \��    �                (        self.assertTrue(mock_fan.called)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \��     �         "              �         !    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \��     �         "              mock_run.assert5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                                             \��    �                "        mock_run.assert_any_call()5�_�       "           !   !        ����                                                                                                                                                                                                                                                                                                                                                             \��     �       !          (        self.assertTrue(mock_fan.called)5�_�   !   #           "      7    ����                                                                                                                                                                                                                                                                                                                                                             \��     �                9    @mock.patch("overclockers.OverclockFactory.run_cmds")5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                                                             \��     �                <    @mock.patch("overclockers.AMD_RX500.set_default_clocks")5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                                                             \��     �                1    @mock.patch("overclockers.AMD_RX500.set_fan")5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                                                             \��     �               /        self, mock_run, mock_defaults, mock_fan5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                                                             \��   	 �                  #from unittest import TestCase, mock       >from overclockers import OverclockFactory, OverclockController           (class TestOverclockController(TestCase):       def setUp(self):       O        self.overclock_factory = OverclockFactory(None, None, None, None, None)   H        self.amd_gpus = [{"amd_type": "RX 570"}, {"amd_type": "RX 580"}]   8        self.overclock_controller = OverclockController(   1            self.amd_gpus, self.overclock_factory   	        )       =    @mock.patch("overclockers.OverclockFactory.run_all_mods")   K    def test_overclock_gpus_overclocks_mixed_multiple_gpus(self, mock_run):   N        self.overclock_controller.overclock_gpus("ethereum", overclocked=True)   ?        mock_run.assert_any_call(True, "ethereum", "RX 570", 0)   ?        mock_run.assert_any_call(True, "ethereum", "RX 580", 1)       =    @mock.patch("overclockers.OverclockFactory.run_all_mods")   6    def test_overclock_controller_disabled_overclocks(           self, mock_run,        ):   3        overclock_controller = OverclockController(   1            self.amd_gpus, self.overclock_factory   	        )   J        overclock_controller.overclock_gpus("ethereum", overclocked=False)   )        self.assertFalse(mock_run.called)   -        self.assertTrue(mock_defaults.called)5�_�   &   (           '          ����                                                                                                                                                                                                                                                                                                                                                             \��!   
 �                -        self.assertTrue(mock_defaults.called)5�_�   '   )           (          ����                                                                                                                                                                                                                                                                                                                                                             \��:     �                         �               5�_�   (   *           )           ����                                                                                                                                                                                                                                                                                                                                                             \��]     �               �               5�_�   )   +           *          ����                                                                                                                                                                                                                                                                                                                                                             \��`    �                "        mock_run.assert_any_call()5�_�   *   ,           +           ����                                                                                                                                                                                                                                                                                                                                                 V       \��    �             
       =    @mock.patch("overclockers.OverclockFactory.run_all_mods")   F    def test_overclock_controller_disabled_overclocks(self, mock_run):   3        overclock_controller = OverclockController(   1            self.amd_gpus, self.overclock_factory   	        )   J        overclock_controller.overclock_gpus("ethereum", overclocked=False)   )        self.assertFalse(mock_run.called)   H        mock_run.assert_any_call("echo 1 > /some/glob/path", shell=True)   J        mock_run.assert_any_call("echo 153 > /some/glob/path", shell=True)5�_�   +   -           ,      +    ����                                                                                                                                                                                                                                                                                                                                                             \�f�     �               >from overclockers import OverclockFactory, OverclockController5�_�   ,   .           -      +    ����                                                                                                                                                                                                                                                                                                                                                             \�f�    �               +from overclockers import OverclockFactory, 5�_�   -   2           .      .    ����                                                                                                                                                                                                                                                                                                                                                             \�g    �               .from overclockers import OverclockFactory, AMD5�_�   .   3   1       2   	       ����                                                                                                                                                                                                                                                                                                                                                             \�gF    �      
         O        self.overclock_factory = OverclockFactory(None, None, None, None, None)5�_�   2   4           3   	   2    ����                                                                                                                                                                                                                                                                                                                                                             \�gW     �      
         P        self.amd_gpu_modfactory = OverclockFactory(None, None, None, None, None)5�_�   3   5           4   	   %    ����                                                                                                                                                                                                                                                                                                                                                             \�g[    �      
         C        self.amd_gpu_modfactory = AMD(None, None, None, None, None)5�_�   4   6           5   	   9    ����                                                                                                                                                                                                                                                                                                                                                             \�gb    �      
         P        self.amd_gpu_modfactory = AMDGPUModFactory(None, None, None, None, None)5�_�   5   7           6   	   U    ����                                                                                                                                                                                                                                                                                                                                                             \�gh     �      
         V        self.amd_gpu_modfactory = AMDGPUModFactory(None, None, None, None, None, None)5�_�   6   8           7   	   `    ����                                                                                                                                                                                                                                                                                                                                                             \�go    �                  #from unittest import TestCase, mock       ;from overclockers import OverclockFactory, AMDGPUModFactory           (class TestOverclockController(TestCase):       def setUp(self):       b        self.amd_gpu_modfactory = AMDGPUModFactory(None, None, None, None, None, None, None, None)   H        self.amd_gpus = [{"amd_type": "RX 570"}, {"amd_type": "RX 580"}]   8        self.overclock_controller = OverclockController(   1            self.amd_gpus, self.overclock_factory   	        )       =    @mock.patch("overclockers.OverclockFactory.run_all_mods")   K    def test_overclock_gpus_overclocks_mixed_multiple_gpus(self, mock_run):   N        self.overclock_controller.overclock_gpus("ethereum", overclocked=True)   ?        mock_run.assert_any_call(True, "ethereum", "RX 570", 0)   ?        mock_run.assert_any_call(True, "ethereum", "RX 580", 1)5�_�   7   9           8      )    ����                                                                                                                                                                                                                                                                                                                                                             \�gv    �               1            self.amd_gpus, self.overclock_factory5�_�   8   :           9      2    ����                                                                                                                                                                                                                                                                                                                                                             \�g{    �               :            self.amd_gpus, self.amd_gpu_modfactory_factory5�_�   9   ;           :      )    ����                                                                                                                                                                                                                                                                                                                                                             \�g�    �               ;from overclockers import OverclockFactory, AMDGPUModFactory5�_�   :               ;      0    ����                                                                                                                                                                                                                                                                                                                                                             \�g�    �               N        self.overclock_controller.overclock_gpus("ethereum", overclocked=True)5�_�   .       /   2   1   
       ����                                                                                                                                                                                                                                                                                                                                                             \�g<     �   	            R        self.amdgpu_mod_factory = [{"amd_type": "RX 570"}, {"amd_type": "RX 580"}]5�_�   .   0       1   /      !    ����                                                                                                                                                                                                                                                                                                                                                             \�g%     �   
            6        self.amdgpu_mod_factory = OverclockController(5�_�   /               0      5    ����                                                                                                                                                                                                                                                                                                                                                             \�g3     �   
            %        self.amdgpu_mod_factory = Ov(5�_�                       J    ����                                                                                                                                                                                                                                                                                                                                                             \��!     �         $      Z    def test_overclock_gpus_overclocks_mixed_multiple_gpus(self, mock_run, mock mock_fan):5��