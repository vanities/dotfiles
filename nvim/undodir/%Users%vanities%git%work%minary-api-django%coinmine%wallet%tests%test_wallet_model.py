Vim�UnDo� pI�D/3U8�����$���b�<H�_ɱ      #class TestWalletServices(TestCase):            (       (   (   (    ]��p   
 _�                             ����                                                                                                                                                                                                                                                                                                                                                             ]�g�     �                   �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�g�     �                  5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]�g�     �                &from cryptography.fernet import Fernet   0from fernet_fields.hkdf import derive_fernet_key5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]�g�     �                 import json    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]�g�     �                 from django.db import connection   +from django.contrib.auth.models import User   ,from django.utils.encoding import force_text    from django.conf import settings   from unittest import mock       %from coinmine.coin.models import Coin5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]�g�     �         !    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]�g�    �                3from coinmine.mineosminer.models import MineOSMiner   Afrom coinmine.wallet.services.wallet_service import WalletService5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                  V        ]�g�     �                )        self.owner = User.objects.first()   0        self.miner = MineOSMiner.objects.first()   :        self.ethereum = Coin.objects.get(short_name="eth")   7        self.zcash = Coin.objects.get(short_name="zec")   7        self.grin = Coin.objects.get(short_name="grin")5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                V       ]�g�     �                =        self.wallet_private = WalletPrivate.objects.get(pk=1)   2        self.wallet_count = Wallet.objects.count()   A        self.wallet_private_count = WalletPrivate.objects.count()5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                V       ]�g�     �               9    def test_find_or_create_wallet_finds_if_exists(self):5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                V       ]�g�    �                   def test_(self):5�_�                            ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�g�     �                :        self.assertEqual(2, WalletPrivate.objects.count())   C        self.assertEqual(self.wallet_count, Wallet.objects.count())   O        wallet = WalletService.find_or_create_wallet(self.miner, self.ethereum)   ,        self.assertEqual(True, bool(wallet))   :        self.assertEqual(2, WalletPrivate.objects.count())   C        self.assertEqual(self.wallet_count, Wallet.objects.count())5�_�                           ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�g�     �                         �               5�_�                       =    ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�g�     �                 >        self.assertEqual(self.wallet.amount_in_smallest_units)5�_�                       ?    ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�g�     �                 @        self.assertEqual(self.wallet.amount_in_smallest_units())5�_�                           ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�g�     �                 >        self.assertEqual(self.wallet.amount_in_smallest_units)5�_�                           ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�g�     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�g�     �             �             5�_�                       (    ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�h     �               A        self.assertEqual(0, self.wallet.amount_in_smallest_units)5�_�                       (    ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�h     �               )        self.assertEqual(0, self.wallet.)5�_�                       (    ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�h     �               A        self.assertEqual(0, self.wallet.amount_in_smallest_units)5�_�                       (    ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�h    �               )        self.assertEqual(0, self.wallet.)5�_�                       )    ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�h     �               8from coinmine.wallet.models import Wallet, WalletPrivate5�_�                           ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�h     �                        "mineosminers.yaml",5�_�                           ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�h    �                   from django.test import TestCase       )from coinmine.wallet.models import Wallet           #class TestWalletServices(TestCase):       fixtures = [           "users.yaml",           "coins.yaml",           "wallets.yaml",           "wallet_privates.yaml",       ]           def setUp(self):   .        self.wallet = Wallet.objects.get(pk=3)       ,    def test_amount_in_smallest_units(self):   ;        self.assertEqual(0, self.wallet.coin.smallest_unit)   5        self.assertEqual(0, self.wallet.amound_mined)   A        self.assertEqual(0, self.wallet.amount_in_smallest_units)5�_�                           ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�h6     �                �             5�_�                           ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�h=     �               ;        self.assertEqual(0, self.wallet.coin.smallest_unit)�             5�_�                       (    ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�h?    �                   from django.test import TestCase   from decimal import Decimal       )from coinmine.wallet.models import Wallet           #class TestWalletServices(TestCase):   S    fixtures = ["users.yaml", "coins.yaml", "wallets.yaml", "wallet_privates.yaml"]           def setUp(self):   .        self.wallet = Wallet.objects.get(pk=3)       ,    def test_amount_in_smallest_units(self):   J        self.assertEqual(Decimal('1E-18'), self.wallet.coin.smallest_unit)   5        self.assertEqual(0, self.wallet.amound_mined)   A        self.assertEqual(0, self.wallet.amount_in_smallest_units)5�_�                       )    ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�hu     �                       �             5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�h     �                       �             5�_�                            ����                                                                                                                                                                                                                                                                                                                               $                 V       ]�h�     �               5        self.assertEqual(0, self.wallet.amound_mined)5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                                v       ]�h�     �                 A        self.assertEqual(0, self.wallet.amount_in_smallest_units)5�_�       "           !           ����                                                                                                                                                                                                                                                                                                                                                v       ]�h�     �                 G        self.assertEqual(Decimal, self.wallet.amount_in_smallest_units)5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                                                v       ]�h�     �                 A        self.assertEqual(), self.wallet.amount_in_smallest_units)5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                                                v       ]�h�    �                 @        self.assertEqual(, self.wallet.amount_in_smallest_units)5�_�   #   %           $      9    ����                                                                                                                                                                                                                                                                                                                                                v       ]�h�    �               @        self.assertEqual(Decimal("1"), self.wallet.amound_mined)5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                                                v       ]�h�     �                 A        self.assertEqual(0, self.wallet.amount_in_smallest_units)5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                                                v       ]�h�     �                 @        self.assertEqual(, self.wallet.amount_in_smallest_units)�               5�_�   &   (           '      (    ����                                                                                                                                                                                                                                                                                                                                                v       ]�h�   	 �                   from django.test import TestCase   from decimal import Decimal       )from coinmine.wallet.models import Wallet           #class TestWalletServices(TestCase):   S    fixtures = ["users.yaml", "coins.yaml", "wallets.yaml", "wallet_privates.yaml"]           def setUp(self):   .        self.wallet = Wallet.objects.get(pk=3)   /        self.wallet.amount_mined = Decimal("1")           self.wallet.save()       ,    def test_amount_in_smallest_units(self):   J        self.assertEqual(Decimal("1E-18"), self.wallet.coin.smallest_unit)   @        self.assertEqual(Decimal("1"), self.wallet.amount_mined)   P        self.assertEqual(Decimal('1E+18'), self.wallet.amount_in_smallest_units)5�_�   '               (          ����                                                                                                                                                                                                                                                                                                                                                             ]��o   
 �               #class TestWalletServices(TestCase):5��