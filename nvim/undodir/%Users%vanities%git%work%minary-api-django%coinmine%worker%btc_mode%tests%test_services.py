Vim�UnDo� 6�āQ��Z��Wr�W��Ӛ'�+�`��t�e��   �                 !       !   !   !    ^M�|    _�                     �       ����                                                                                                                                                                                                                                                                                                                                                             ^A��     �   �   �   �      /        miners = miners.union(miners, all=True)5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             ^A��    �   �   �   �              miners = miners5�_�                    �   /    ����                                                                                                                                                                                                                                                                                                                                                             ^A�      �   �   �   �      >        self.assertEqual(expected_miner_count, miners.count())5�_�                    �   9    ����                                                                                                                                                                                                                                                                                                                                                             ^A�"     �   �   �   �      B        self.assertEqual(expected_miner_count, len(miners.count())5�_�                    �   :    ����                                                                                                                                                                                                                                                                                                                                                             ^A�"    �   �   �   �      ;        self.assertEqual(expected_miner_count, len(miners))5�_�                    _       ����                                                                                                                                                                                                                                                                                                                                                             ^L;n     �   ^   `   �                  Decimal("0.00"),5�_�                    _       ����                                                                                                                                                                                                                                                                                                                                                             ^L;q    �   ^   `   �                  0.00"),5�_�      	              n       ����                                                                                                                                                                                                                                                                                                                                                             ^L;x     �   m   o   �                  Decimal("0.05"),5�_�      
           	   n       ����                                                                                                                                                                                                                                                                                                                                                             ^L;}     �   m   o   �                  0.05"),5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             ^L;�     �   ~   �   �                  Decimal("0.05"),5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             ^L;�     �   ~   �   �                 0.05"),5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^L;�    �               �   from unittest.mock import patch   from decimal import Decimal    from django.test import TestCase       3from coinmine.mineosminer.models import MineOSMiner   )from coinmine.wallet.models import Wallet   +from django.contrib.auth.models import User   ;from coinmine.worker.btc_mode.service import BTCModeService   %from coinmine.coin.models import Coin           $class BTCModeServiceTests(TestCase):       fixtures = [           "users.yaml",           "coins.yaml",           "wallets.yaml",           "wallet_privates.yaml",           "mineosminers.yaml",           "statuses.yaml",           "configs.yaml",           "pools.yaml",           "user_profiles.yaml",       ]           def setUp(self):   0        eth = Coin.objects.get(short_name="eth")   &        eth.btc_per_day = Decimal("1")           eth.save()       2        self.miner = MineOSMiner.objects.get(pk=5)   ?        self.hashcat = Coin.objects.get(name__iexact="hashcat")   3        self.hashcat.btc_per_day = Decimal("0.001")           self.hashcat.save()   #        self.seconds_in_day = 86400       $    def btc_mode_miners_count(self):           return (   3            MineOSMiner.objects.exclude(owner=None)   A            .filter(config__wallet__coin__short_name__in=["btc"])               .count()   	        )           def incorrect_miners(self):   W        return MineOSMiner.objects.filter(config__wallet__coin__short_name__in=["eth"])       '    def test_convert_sats_to_btc(self):           self.assertEqual(   R            1, BTCModeService.smallest_unit_to_decimal(100000000, Decimal("1e-8"))   	        )       )    def test_amount_earned_per_day(self):               self.assertEqual(                Decimal("95000000"),   <            BTCModeService.adjusted_units_earned_per_second(   3                Decimal("1"), Decimal("1e-8"), 0.05               )   "            * self.seconds_in_day,   	        )           def test_get_fee(self):   (        general = User.objects.get(pk=1)   (        founder = User.objects.get(pk=2)   (        missing = User.objects.get(pk=3)   D        self.assertEqual(0.05, BTCModeService.get_fee(general, 0.9))   D        self.assertEqual(0.00, BTCModeService.get_fee(founder, 0.9))   C        self.assertEqual(0.9, BTCModeService.get_fee(missing, 0.9))       $    def test_make_wallet_dict(self):           self.assertEqual(               {   -                "amount_mined": Decimal("2"),   /                "unpaid_balance": Decimal("2"),   .                "usd_value": Decimal("18000"),               },   ,            BTCModeService.make_wallet_dict(   I                Decimal("1"), Decimal("1"), Decimal("1"), Decimal("9000")               ),   	        )       7    @patch("coinmine.mineosminer.models.Status.online")   J    def test_updates_miner_wallets_with_general(self, mock_status_online):   .        mock_status_online.return_value = True       @        wallet = Wallet.objects.filter(address="btc-address")[0]   ;        self.assertEqual(0.0, Decimal(wallet.amount_mined))   =        self.assertEqual(0.0, Decimal(wallet.unpaid_balance))   8        self.assertEqual(0.0, Decimal(wallet.usd_value))       &        BTCModeService.update_wallets(   -            BTCModeService.filtered_miners(),               Decimal("9000"),               Decimal("1e-8"),   .            Decimal(str(self.seconds_in_day)),               0.00,   	        )            wallet.refresh_from_db()   D        self.assertEqual(Decimal("1"), Decimal(wallet.amount_mined))   F        self.assertEqual(Decimal("1"), Decimal(wallet.unpaid_balance))   D        self.assertEqual(Decimal("9000"), Decimal(wallet.usd_value))               # simulated payout   !        wallet.unpaid_balance = 0           wallet.save()   &        BTCModeService.update_wallets(   -            BTCModeService.filtered_miners(),               Decimal("9000"),               Decimal("1e-8"),   .            Decimal(str(self.seconds_in_day)),               0.05,   	        )            wallet.refresh_from_db()   D        self.assertEqual(Decimal("2"), Decimal(wallet.amount_mined))   F        self.assertEqual(Decimal("1"), Decimal(wallet.unpaid_balance))   E        self.assertEqual(Decimal("18000"), Decimal(wallet.usd_value))       J    @patch("coinmine.worker.btc_mode.service.BTCModeService.update_model")   7    @patch("coinmine.mineosminer.models.Status.online")   W    def test_only_runs_against_btc_miners(self, mock_status_online, mock_update_model):   .        mock_status_online.return_value = True   -        mock_update_model.return_value = None   &        BTCModeService.update_wallets(   -            BTCModeService.filtered_miners(),               Decimal("9000"),               Decimal("1e-8"),   )            Decimal(self.seconds_in_day),              0.05,   	        )   T        self.assertEqual(mock_update_model.call_count, self.btc_mode_miners_count())       J    @patch("coinmine.worker.btc_mode.service.BTCModeService.update_model")   7    @patch("coinmine.mineosminer.models.Status.online")   1    def test_only_runs_against_online_btc_miners(   3        self, mock_status_online, mock_update_model       ):   /        mock_status_online.return_value = False   -        mock_update_model.return_value = None   &        BTCModeService.update_wallets(   -            BTCModeService.filtered_miners(),               Decimal("9000"),               Decimal("1e-8"),   )            Decimal(self.seconds_in_day),               Decimal("0.05"),   	        )   9        self.assertEqual(mock_update_model.call_count, 0)       7    @patch("coinmine.mineosminer.models.Status.online")   K    def test_adds_sats_for_each_miner_same_owner(self, mock_status_online):   .        mock_status_online.return_value = True   1        miners = BTCModeService.filtered_miners()   (        wallet = miners[0].config.wallet                miners = miners + miners            expected_miner_count = 2       ;        self.assertEqual(expected_miner_count, len(miners))   0        self.assertEqual(0, wallet.amount_mined)   &        BTCModeService.update_wallets(               miners,               Decimal("9000"),               Decimal("1e-8"),   )            Decimal(self.seconds_in_day),               Decimal("0.05"),   	        )                wallet.refresh_from_db()   R        self.assertEqual(Decimal("1") * expected_miner_count, wallet.amount_mined)       7    @patch("coinmine.mineosminer.models.Status.online")   @    def test_hashcat_coin_integration(self, mock_status_online):   .        mock_status_online.return_value = True       !        # set hashcat as the coin   6        self.miner.config.btc_mode_coin = self.hashcat            self.miner.config.save()       :        wallet = Wallet.objects.get(address="btc-address")   ;        self.assertEqual(0.0, Decimal(wallet.amount_mined))   =        self.assertEqual(0.0, Decimal(wallet.unpaid_balance))   8        self.assertEqual(0.0, Decimal(wallet.usd_value))       &        BTCModeService.update_wallets(   -            BTCModeService.filtered_miners(),               Decimal("9000"),               Decimal("1e-8"),   )            Decimal(self.seconds_in_day),               Decimal("0.05"),   	        )                wallet.refresh_from_db()           # 6.5 sats per minute   ?        self.assertEqual(Decimal("0.001"), wallet.amount_mined)       A    def test_adjusted_sats_earned_per_second_decimal_error(self):           general_fee = 0.00   G        sats_founder = BTCModeService.adjusted_units_earned_per_second(               0, 0, general_fee   	        )   2        self.assertEqual(Decimal(0), sats_founder)5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             ^L;�     �   �   �   �                  Decimal("0.05"),5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             ^L;�    �   �   �   �                  0.05"),5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             ^L;�     �   �   �   �                  Decimal("0.05"),5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             ^L;�     �   �   �   �                  0.05"),5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             ^L;�    �               �   from unittest.mock import patch   from decimal import Decimal    from django.test import TestCase       3from coinmine.mineosminer.models import MineOSMiner   )from coinmine.wallet.models import Wallet   +from django.contrib.auth.models import User   ;from coinmine.worker.btc_mode.service import BTCModeService   %from coinmine.coin.models import Coin           $class BTCModeServiceTests(TestCase):       fixtures = [           "users.yaml",           "coins.yaml",           "wallets.yaml",           "wallet_privates.yaml",           "mineosminers.yaml",           "statuses.yaml",           "configs.yaml",           "pools.yaml",           "user_profiles.yaml",       ]           def setUp(self):   0        eth = Coin.objects.get(short_name="eth")   &        eth.btc_per_day = Decimal("1")           eth.save()       2        self.miner = MineOSMiner.objects.get(pk=5)   ?        self.hashcat = Coin.objects.get(name__iexact="hashcat")   3        self.hashcat.btc_per_day = Decimal("0.001")           self.hashcat.save()   #        self.seconds_in_day = 86400       $    def btc_mode_miners_count(self):           return (   3            MineOSMiner.objects.exclude(owner=None)   A            .filter(config__wallet__coin__short_name__in=["btc"])               .count()   	        )           def incorrect_miners(self):   W        return MineOSMiner.objects.filter(config__wallet__coin__short_name__in=["eth"])       '    def test_convert_sats_to_btc(self):           self.assertEqual(   R            1, BTCModeService.smallest_unit_to_decimal(100000000, Decimal("1e-8"))   	        )       )    def test_amount_earned_per_day(self):               self.assertEqual(                Decimal("95000000"),   <            BTCModeService.adjusted_units_earned_per_second(   3                Decimal("1"), Decimal("1e-8"), 0.05               )   "            * self.seconds_in_day,   	        )           def test_get_fee(self):   (        general = User.objects.get(pk=1)   (        founder = User.objects.get(pk=2)   (        missing = User.objects.get(pk=3)   D        self.assertEqual(0.05, BTCModeService.get_fee(general, 0.9))   D        self.assertEqual(0.00, BTCModeService.get_fee(founder, 0.9))   C        self.assertEqual(0.9, BTCModeService.get_fee(missing, 0.9))       $    def test_make_wallet_dict(self):           self.assertEqual(               {   -                "amount_mined": Decimal("2"),   /                "unpaid_balance": Decimal("2"),   .                "usd_value": Decimal("18000"),               },   ,            BTCModeService.make_wallet_dict(   I                Decimal("1"), Decimal("1"), Decimal("1"), Decimal("9000")               ),   	        )       7    @patch("coinmine.mineosminer.models.Status.online")   J    def test_updates_miner_wallets_with_general(self, mock_status_online):   .        mock_status_online.return_value = True       @        wallet = Wallet.objects.filter(address="btc-address")[0]   ;        self.assertEqual(0.0, Decimal(wallet.amount_mined))   =        self.assertEqual(0.0, Decimal(wallet.unpaid_balance))   8        self.assertEqual(0.0, Decimal(wallet.usd_value))       &        BTCModeService.update_wallets(   -            BTCModeService.filtered_miners(),               Decimal("9000"),               Decimal("1e-8"),   .            Decimal(str(self.seconds_in_day)),               0.00,   	        )            wallet.refresh_from_db()   D        self.assertEqual(Decimal("1"), Decimal(wallet.amount_mined))   F        self.assertEqual(Decimal("1"), Decimal(wallet.unpaid_balance))   D        self.assertEqual(Decimal("9000"), Decimal(wallet.usd_value))               # simulated payout   !        wallet.unpaid_balance = 0           wallet.save()   &        BTCModeService.update_wallets(   -            BTCModeService.filtered_miners(),               Decimal("9000"),               Decimal("1e-8"),   .            Decimal(str(self.seconds_in_day)),               0.05,   	        )            wallet.refresh_from_db()   D        self.assertEqual(Decimal("2"), Decimal(wallet.amount_mined))   F        self.assertEqual(Decimal("1"), Decimal(wallet.unpaid_balance))   E        self.assertEqual(Decimal("18000"), Decimal(wallet.usd_value))       J    @patch("coinmine.worker.btc_mode.service.BTCModeService.update_model")   7    @patch("coinmine.mineosminer.models.Status.online")   W    def test_only_runs_against_btc_miners(self, mock_status_online, mock_update_model):   .        mock_status_online.return_value = True   -        mock_update_model.return_value = None   &        BTCModeService.update_wallets(   -            BTCModeService.filtered_miners(),               Decimal("9000"),               Decimal("1e-8"),   )            Decimal(self.seconds_in_day),               0.05,   	        )   T        self.assertEqual(mock_update_model.call_count, self.btc_mode_miners_count())       J    @patch("coinmine.worker.btc_mode.service.BTCModeService.update_model")   7    @patch("coinmine.mineosminer.models.Status.online")   1    def test_only_runs_against_online_btc_miners(   3        self, mock_status_online, mock_update_model       ):   /        mock_status_online.return_value = False   -        mock_update_model.return_value = None   &        BTCModeService.update_wallets(   -            BTCModeService.filtered_miners(),               Decimal("9000"),               Decimal("1e-8"),   )            Decimal(self.seconds_in_day),               0.05,   	        )   9        self.assertEqual(mock_update_model.call_count, 0)       7    @patch("coinmine.mineosminer.models.Status.online")   K    def test_adds_sats_for_each_miner_same_owner(self, mock_status_online):   .        mock_status_online.return_value = True   1        miners = BTCModeService.filtered_miners()   (        wallet = miners[0].config.wallet                miners = miners + miners            expected_miner_count = 2       ;        self.assertEqual(expected_miner_count, len(miners))   0        self.assertEqual(0, wallet.amount_mined)   &        BTCModeService.update_wallets(               miners,               Decimal("9000"),               Decimal("1e-8"),   )            Decimal(self.seconds_in_day),               0.05,   	        )                wallet.refresh_from_db()   R        self.assertEqual(Decimal("1") * expected_miner_count, wallet.amount_mined)       7    @patch("coinmine.mineosminer.models.Status.online")   @    def test_hashcat_coin_integration(self, mock_status_online):   .        mock_status_online.return_value = True       !        # set hashcat as the coin   6        self.miner.config.btc_mode_coin = self.hashcat            self.miner.config.save()       :        wallet = Wallet.objects.get(address="btc-address")   ;        self.assertEqual(0.0, Decimal(wallet.amount_mined))   =        self.assertEqual(0.0, Decimal(wallet.unpaid_balance))   8        self.assertEqual(0.0, Decimal(wallet.usd_value))       &        BTCModeService.update_wallets(   -            BTCModeService.filtered_miners(),               Decimal("9000"),               Decimal("1e-8"),   )            Decimal(self.seconds_in_day),               Decimal("0.05"),   	        )                wallet.refresh_from_db()           # 6.5 sats per minute   ?        self.assertEqual(Decimal("0.001"), wallet.amount_mined)       A    def test_adjusted_sats_earned_per_second_decimal_error(self):           general_fee = 0.00   G        sats_founder = BTCModeService.adjusted_units_earned_per_second(               0, 0, general_fee   	        )   2        self.assertEqual(Decimal(0), sats_founder)5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             ^L;�     �   �   �   �                  Decimal("0.05"),5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             ^L;�    �   �   �   �                  0.05"),5�_�                    ^       ����                                                                                                                                                                                                                                                                                                                                                             ^LH     �   ]   _   �      .            Decimal(str(self.seconds_in_day)),5�_�                    ^   !    ����                                                                                                                                                                                                                                                                                                                                                             ^LH    �   ]   _   �      "            self.seconds_in_day)),5�_�                    m       ����                                                                                                                                                                                                                                                                                                                                                             ^LH�     �   l   n   �      .            Decimal(str(self.seconds_in_day)),5�_�                    m       ����                                                                                                                                                                                                                                                                                                                                                             ^LH�     �   l   n   �      &            str(self.seconds_in_day)),5�_�                    m       ����                                                                                                                                                                                                                                                                                                                                                             ^LH�   	 �   l   n   �      "            self.seconds_in_day)),5�_�                    ~       ����                                                                                                                                                                                                                                                                                                                                                             ^LH�     �   }      �      )            Decimal(self.seconds_in_day),5�_�                    ~        ����                                                                                                                                                                                                                                                                                                                                                             ^LH�     �   }      �      !            self.seconds_in_day),5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             ^LH�     �   �   �   �      )            Decimal(self.seconds_in_day),5�_�                    �        ����                                                                                                                                                                                                                                                                                                                                                             ^LH�     �   �   �   �      !            self.seconds_in_day),5�_�                    �   6    ����                                                                                                                                                                                                                                                                                                                                                             ^LH�     �   �   �   �      X            miners, Decimal("9000"), Decimal("1e-8"), Decimal(self.seconds_in_day), 0.055�_�                    �   J    ����                                                                                                                                                                                                                                                                                                                                                             ^LH�     �   �   �   �      P            miners, Decimal("9000"), Decimal("1e-8"), self.seconds_in_day), 0.055�_�                     �       ����                                                                                                                                                                                                                                                                                                                                                             ^LH�     �   �   �   �      )            Decimal(self.seconds_in_day),5�_�      !               �        ����                                                                                                                                                                                                                                                                                                                                                             ^LH�    �   �   �   �      !            self.seconds_in_day),5�_�                   !   �        ����                                                                                                                                                                                                                                                                                                                            �           �          V       ^M�{    �   �   �              A    def test_adjusted_sats_earned_per_second_decimal_error(self):           general_fee = 0.00   G        sats_founder = BTCModeService.adjusted_units_earned_per_second(               0, 0, general_fee   	        )   2        self.assertEqual(Decimal(0), sats_founder)5��