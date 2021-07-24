Vim�UnDo� U��6N��Jj�1c��B�Ք�Zť���(�6�      6from rest_framework.test import APIClient, APITestCase      +      8       8   8   8    ]鏒    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ]�hY     �                   �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�hZ     �                  5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�h]     �               ,class SupportMinerManagerTests(APITestCase):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�hc     �                       �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�ho     �                       self.support_miner5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�hz    �                �             5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                             ]�i'     �                       �             5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                             ]�i2     �                        self.support_miner.actve5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             ]�i5     �               !        self.support_miner.active5�_�   	              
      2    ����                                                                                                                                                                                                                                                                                                                                                             ]�i;     �               2        self.assertFalse(self.support_miner.active5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             ]�i<    �                        pass5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�j[     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�j^     �               ;        self.support_miner = SupportMiner.objects.get(pk=2)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�jd     �               ;        self.support_miner = SupportMiner.objects.get(pk=2)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�jm     �               ;        self.support_miner = SupportMiner.objects.get(pk=2)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�jq     �                 3        self.assertFalse(self.support_miner.active)5�_�                       %    ����                                                                                                                                                                                                                                                                                                                                                             ]�jt     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�jv     �               ;        self.assertFalse(self.ten_day_support_miner.active)5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                             ]�jz    �               :        self.assertTrue(self.ten_day_support_miner.active)5�_�                       "    ����                                                                                                                                                                                                                                                                                                                                                             ]�j�     �                       �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�j�     �                        print(self.)5�_�                       B    ����                                                                                                                                                                                                                                                                                                                                                             ]�j�    �               C        self.forever_support_miner = SupportMiner.objects.get(pk=2)5�_�                       4    ����                                                                                                                                                                                                                                                                                                                                                             ]�j�    �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�j�     �                 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�j�    �               E    def test_active_manager_returns_only_active_support_miners(self):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�j�    �               D    def test_support_miner_returns_only_active_support_miners(self):5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�j�     �                �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�j�     �                !from freezegun import freeze_time5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�j�     �              �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�j�     �             5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             ]�j�    �                  !from freezegun import freeze_time       6from rest_framework.test import APIClient, APITestCase       +from django.contrib.auth.models import User       0from coinmine.devices.models import SupportMiner           *class SupportMinerModelTests(APITestCase):       maxDiff = None   ,    fixtures = ["support_miners_local.yaml"]           def setUp(self):   !        self.client = APIClient()   *        self.user = User.objects.get(pk=1)       C        self.forever_support_miner = SupportMiner.objects.get(pk=1)   C        self.ten_day_support_miner = SupportMiner.objects.get(pk=2)   K    def test_support_miner_active_returns_only_active_support_miners(self):   :        self.assertTrue(self.forever_support_miner.active)   ;        self.assertFalse(self.ten_day_support_miner.active)5�_�      !                       ����                                                                                                                                                                                                                                                                                                                                                             ]�j�   	 �                 5�_�       "           !           ����                                                                                                                                                                                                                                                                                                                                                             ]�j�     �                �             5�_�   !   #           "           ����                                                                                                                                                                                                                                                                                                                               )          )       V   )    ]�j�     �               *@freeze_time("2019-10-21 16:34:30.056476")5�_�   "   $           #      )    ����                                                                                                                                                                                                                                                                                                                               )          )       V   )    ]�j�   
 �             5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                               )          )       V   )    ]�k     �               .    @freeze_time("2019-10-21 16:34:30.056476")�             5�_�   $   &           %      ,    ����                                                                                                                                                                                                                                                                                                                               )          )       V   )    ]�k     �               I    @freeze_time("2013-03-16T17:41:28+00:00""2019-10-21 16:34:30.056476")5�_�   %   (           &          ����                                                                                                                                                                                                                                                                                                                               )          )       V   )    ]�k    �                 ;        self.assertFalse(self.ten_day_support_miner.active)5�_�   &   )   '       (           ����                                                                                                                                                                                                                                                                                                                                                  V        ]�|9     �               �               5�_�   (   *           )          ����                                                                                                                                                                                                                                                                                                                                                  V        ]�|9     �             5�_�   )   +           *      D    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�|=     �               K    def test_support_miner_active_returns_only_active_support_miners(self):5�_�   *   -           +      H    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�|D     �               V    def test_support_miner_active_returns_only_active_support_miners_all_active(self):5�_�   +   .   ,       -      D    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�|L     �               K    def test_support_miner_active_returns_only_active_support_miners(self):5�_�   -   0           .      T    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�|Q    �                  !from freezegun import freeze_time       6from rest_framework.test import APIClient, APITestCase       +from django.contrib.auth.models import User   0from coinmine.devices.models import SupportMiner           *class SupportMinerModelTests(APITestCase):       maxDiff = None   ,    fixtures = ["support_miners_local.yaml"]           def setUp(self):   !        self.client = APIClient()   *        self.user = User.objects.get(pk=1)       C        self.forever_support_miner = SupportMiner.objects.get(pk=1)   C        self.ten_day_support_miner = SupportMiner.objects.get(pk=2)       -    @freeze_time("2013-03-16T17:41:28+00:00")   Z    def test_support_miner_active_returns_only_active_support_miners_ten_day_active(self):   :        self.assertTrue(self.forever_support_miner.active)   :        self.assertTrue(self.ten_day_support_miner.active)       -    @freeze_time("2013-03-16T17:41:28+00:00")   \    def test_support_miner_active_returns_only_active_support_miners_ten_day_inactive(self):   :        self.assertTrue(self.forever_support_miner.active)   :        self.assertTrue(self.ten_day_support_miner.active)5�_�   .   1   /       0          ����                                                                                                                                                                                                                                                                                                                                                  V        ]�|c    �                -    @freeze_time("2013-03-16T17:41:28+00:00")5�_�   0   3           1           ����                                                                                                                                                                                                                                                                                                                                                  V        ]�|v     �                 :        self.assertTrue(self.ten_day_support_miner.active)5�_�   1   5   2       3      %    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�|�    �                -    @freeze_time("2013-03-26T17:41:28+00:00")5�_�   3   6   4       5           ����                                                                                                                                                                                                                                                                                                                                                  V        ]鏉     �                !        self.client = APIClient()   *        self.user = User.objects.get(pk=1)5�_�   5   7           6           ����                                                                                                                                                                                                                                                                                                                                                  V        ]鏉    �                 5�_�   6   8           7           ����                                                                                                                                                                                                                                                                                                                                                  V        ]鏎     �                +from django.contrib.auth.models import User5�_�   7               8      +    ����                                                                                                                                                                                                                                                                                                                                                  V        ]鏑    �               6from rest_framework.test import APIClient, APITestCase5�_�   3           5   4           ����                                                                                                                                                                                                                                                                                                                                                  V        ]�|�    �      !          :        self.assertTrue(self.ten_day_support_miner.active)5�_�   1           3   2      +    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�|}    �                -    @freeze_time("2013-03-26T17:41:28+00:01")5�_�   .           0   /          ����                                                                                                                                                                                                                                                                                                                                                  V        ]�|^    �                -    @freeze_time("2013-13-16T17:41:28+00:00")5�_�   +           -   ,      D    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�|J     �               O    def test_support_miner_active_returns_only_active_support_minten_day(self):5�_�   &           (   '           ����                                                                                                                                                                                                                                                                                                                                                V       ]�|3     �               u    @freeze_time("2013-03-16T17:41:28+00:00") def test_support_miner_active_returns_only_active_support_miners(self):5��