Vim�UnDo� �=�>�P�:��#�� �%ăd~	�q��x�      /from .heartbeat_updater import HeartbeatUpdater                             \�0x   	 _�                             ����                                                                                                                                                                                                                                                                                                                                                             \�/�     �                   �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \�/�     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \�/�     �               )class MineOSMinerServicesTests(TestCase):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \�/�     �               %class HeartbeatUpdaterests(TestCase):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \�/�    �                      &class HeartbeatUpdaterTests(TestCase):       """   &    Test suite for the miner services.       """           fixtures = [           "users.yaml",           "coins.yaml",           "wallets.yaml",           "wallet_privates.yaml",           "mineosminers.yaml",           "configs.yaml",           "statuses.yaml",       ]           def setUp(self):   2        self.miner = MineOSMiner.objects.get(pk=1)   .        self.old_coin = Coin.objects.get(pk=1)   .        self.new_coin = Coin.objects.get(pk=2)       C        self.miner_without_children = MineOSMiner.objects.get(pk=2)   7        self.actual_eth_wallet = Wallet.objects.first()   9        self.inital_config_count = Config.objects.count()   9        self.inital_status_count = Status.objects.count()       F    @mock.patch("django.utils.timezone.now", return_value="some-time")   N    def test_heartbeat_updater_adds_heartbeat_to_request(self, mock_datetime):   A        request = HeartbeatUpdater.add_heartbeat(FakeRequest({}))   I        self.assertDictEqual(request.data, {"heartbeat_at": "some-time"})5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \�/�     �              �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \�0      �         (    5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                             \�0     �               )   	import re   from unittest import mock        from django.test import TestCase       Cfrom coinmine.mineosminer.models import MineOSMiner, Config, Status   %from coinmine.coin.models import Coin   )from coinmine.wallet.models import Wallet   %from .coin_changer import CoinChanger   'from .child_creator import ChildCreator   /from .heartbeat_updater import HeartbeatUpdater       &class HeartbeatUpdaterTests(TestCase):       """   &    Test suite for the miner services.       """           fixtures = [           "users.yaml",           "coins.yaml",           "wallets.yaml",           "wallet_privates.yaml",           "mineosminers.yaml",           "configs.yaml",           "statuses.yaml",       ]           def setUp(self):   2        self.miner = MineOSMiner.objects.get(pk=1)   .        self.old_coin = Coin.objects.get(pk=1)   .        self.new_coin = Coin.objects.get(pk=2)       C        self.miner_without_children = MineOSMiner.objects.get(pk=2)   7        self.actual_eth_wallet = Wallet.objects.first()   9        self.inital_config_count = Config.objects.count()   9        self.inital_status_count = Status.objects.count()       F    @mock.patch("django.utils.timezone.now", return_value="some-time")   N    def test_heartbeat_updater_adds_heartbeat_to_request(self, mock_datetime):   A        request = HeartbeatUpdater.add_heartbeat(FakeRequest({}))   I        self.assertDictEqual(request.data, {"heartbeat_at": "some-time"})5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                             \�0    �                 	import re5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                       	           V        \�0    �                %from .coin_changer import CoinChanger   'from .child_creator import ChildCreator5�_�   
                 	        ����                                                                                                                                                                                                                                                                                                                                                  V        \�0     �   	      '    �   	   
   '    5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                                  V        \�0    �               +   from unittest import mock        from django.test import TestCase       Cfrom coinmine.mineosminer.models import MineOSMiner, Config, Status   %from coinmine.coin.models import Coin   )from coinmine.wallet.models import Wallet   /from .heartbeat_updater import HeartbeatUpdater           class FakeRequest:       def __init__(self, data):           self.data = data       &class HeartbeatUpdaterTests(TestCase):       """   &    Test suite for the miner services.       """           fixtures = [           "users.yaml",           "coins.yaml",           "wallets.yaml",           "wallet_privates.yaml",           "mineosminers.yaml",           "configs.yaml",           "statuses.yaml",       ]           def setUp(self):   2        self.miner = MineOSMiner.objects.get(pk=1)   .        self.old_coin = Coin.objects.get(pk=1)   .        self.new_coin = Coin.objects.get(pk=2)       C        self.miner_without_children = MineOSMiner.objects.get(pk=2)   7        self.actual_eth_wallet = Wallet.objects.first()   9        self.inital_config_count = Config.objects.count()   9        self.inital_status_count = Status.objects.count()       F    @mock.patch("django.utils.timezone.now", return_value="some-time")   N    def test_heartbeat_updater_adds_heartbeat_to_request(self, mock_datetime):   A        request = HeartbeatUpdater.add_heartbeat(FakeRequest({}))   I        self.assertDictEqual(request.data, {"heartbeat_at": "some-time"})5�_�                           ����                                                                                                                                                                                                                                                                                                                            '   8                 V   H    \�01     �                    """   &    Test suite for the miner services.       """           fixtures = [           "users.yaml",           "coins.yaml",           "wallets.yaml",           "wallet_privates.yaml",           "mineosminers.yaml",           "configs.yaml",           "statuses.yaml",       ]           def setUp(self):   2        self.miner = MineOSMiner.objects.get(pk=1)   .        self.old_coin = Coin.objects.get(pk=1)   .        self.new_coin = Coin.objects.get(pk=2)       C        self.miner_without_children = MineOSMiner.objects.get(pk=2)   7        self.actual_eth_wallet = Wallet.objects.first()   9        self.inital_config_count = Config.objects.count()   9        self.inital_status_count = Status.objects.count()5�_�                            ����                                                                                                                                                                                                                                                                                                                               8                 V   H    \�02    �                  from unittest import mock        from django.test import TestCase       Cfrom coinmine.mineosminer.models import MineOSMiner, Config, Status   %from coinmine.coin.models import Coin   )from coinmine.wallet.models import Wallet   /from .heartbeat_updater import HeartbeatUpdater           class FakeRequest:       def __init__(self, data):           self.data = data           &class HeartbeatUpdaterTests(TestCase):       F    @mock.patch("django.utils.timezone.now", return_value="some-time")   N    def test_heartbeat_updater_adds_heartbeat_to_request(self, mock_datetime):   A        request = HeartbeatUpdater.add_heartbeat(FakeRequest({}))   I        self.assertDictEqual(request.data, {"heartbeat_at": "some-time"})5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        \�05    �                Cfrom coinmine.mineosminer.models import MineOSMiner, Config, Status   %from coinmine.coin.models import Coin   )from coinmine.wallet.models import Wallet5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        \�0w   	 �               /from .heartbeat_updater import HeartbeatUpdater5��