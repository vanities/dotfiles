Vim�UnDo� @3�;�(?h�Zg�4 �$�'����˅\8֎��                    =       =   =   =    \{E    _�                             ����                                                                                                                                                                                                                                                                                                                                                             \q�     �                   �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \r     �              5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \r     �                 �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                       $          V       \r     �                 from django.test import TestCase   +from django.contrib.auth.models import User   2from coinmine.wallet.services import WalletService   8from coinmine.wallet.models import Wallet, WalletPrivate   :from .delete_user_and_wallet import delete_user_and_wallet   class TestScripts(TestCase):       fixtures = ['coins.yaml']       def setUp(self):   E        self.user = User.objects.create_user(username='some-spammer')   &        WalletService.setup(self.user)   6        self.initial_user_count = User.objects.count()   :        self.initial_wallet_count = Wallet.objects.count()   I        self.initial_wallet_private_count = WalletPrivate.objects.count()   *    def test_delete_user_and_wallet(self):   4        self.assertEqual(1, self.initial_user_count)   6        self.assertEqual(3, self.initial_wallet_count)   >        self.assertEqual(3, self.initial_wallet_private_count)   2        delete_user_and_wallet(self.user.username)   I        self.assertEqual(self.initial_user_count-1, User.objects.count())   M        self.assertEqual(self.initial_wallet_count-3, Wallet.objects.count())           self.assertEqual(   O            self.initial_wallet_private_count-3, WalletPrivate.objects.count())5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V       \r     �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V       \r     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V       \r     �             5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                 V       \r     �             5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                 V       \r    �             5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                                 V       \r!     �      	       5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                 V       \r#    �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \v,     �                       �             5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             \v6     �                   for wallet in wallets:5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                             \v;     �               "    for wallet_private in wallets:5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \vA     �   
            >    wallets = WalletPrivate.objects.filter(wallet__owner=user)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \vH     �                       if wallet.wallet5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \vL     �                        if wallet_private.wallet5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                             \vQ    �               !        if wallet_private.wallet:5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                             \vk     �               !        if wallet_private.wallet.5�_�                       -    ����                                                                                                                                                                                                                                                                                                                                                             \vq     �                           �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \vs     �                            pa5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \vu     �                           �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \vy     �                           retrurn5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \v{     �                           �             5�_�                       -    ����                                                                                                                                                                                                                                                                                                                                                             \v�    �               /            print('wallet has an amount in it')5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \v�     �                           return5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \v�    �                           exit(1)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \v�     �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \v�    �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \wb    �                       wallet.delete()5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                                             \xP     �                            sys.exit(1)5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                                             \xQ   	 �                           �             5�_�   !   #           "           ����                                                                                                                                                                                                                                                                                                                                                V       \x�     �             �             5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                                                V       \x�     �             5�_�   #   %           $           ����                                                                                                                                                                                                                                                                                                                                                V       \x�   
 �                .        if wallet_private.wallet.amount_mined:   8            print('wallet has an amount in it, exiting')               return5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                                                V       \x�     �               8            print('wallet has an amount in it, exiting')5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                                                V       \x�    �               ;            logger.l('wallet has an amount in it, exiting')5�_�   &   (           '          ����                                                                                                                                                                                                                                                                                                                                                V       \x�     �                �             5�_�   '   )           (          ����                                                                                                                                                                                                                                                                                                                                                V       \x�     �      
          �      	       5�_�   (   *           )   	        ����                                                                                                                                                                                                                                                                                                                                                V       \x�    �      
          logger 5�_�   )   +           *   	       ����                                                                                                                                                                                                                                                                                                                                                V       \x�     �      
         logger�   	   
       5�_�   *   ,           +   	       ����                                                                                                                                                                                                                                                                                                                                                V       \x�     �      
         logger=�   	   
       5�_�   +   -           ,   	       ����                                                                                                                                                                                                                                                                                                                                                V       \x�     �      
         logger==�   	   
       5�_�   ,   .           -   	       ����                                                                                                                                                                                                                                                                                                                                                V       \x�     �      
         	logger===�   	   
       5�_�   -   /           .   	   	    ����                                                                                                                                                                                                                                                                                                                                                V       \y     �   	          5�_�   .   0           /   
        ����                                                                                                                                                                                                                                                                                                                                                V       \y     �   	             �   
          5�_�   /   1           0   
        ����                                                                                                                                                                                                                                                                                                                                                V       \y     �   	            =�   
          5�_�   0   2           1           ����                                                                                                                                                                                                                                                                                                                                                V       \y     �   
             �             5�_�   1   3           2   	        ����                                                                                                                                                                                                                                                                                                                            	   	       
          V   ?    \y     �      	          
logger====   ==5�_�   2   4           3   
        ����                                                                                                                                                                                                                                                                                                                            	   	       	          V   ?    \y     �   
          5�_�   3   5           4   	       ����                                                                                                                                                                                                                                                                                                                            	   	       	          V   ?    \y     �      
         @logger = logging.getLogger('worker.pool_api.estimated_earnings')5�_�   4   6           5   	       ����                                                                                                                                                                                                                                                                                                                            	   	       	          V   ?    \y     �      
         logger = logging.getLogger('')5�_�   5   7           6   	   $    ����                                                                                                                                                                                                                                                                                                                            	   	       	          V   ?    \y*    �      
         &logger = logging.getLogger('scripts.')5�_�   6   8           7          ����                                                                                                                                                                                                                                                                                                                            	   	       	          V   ?    \y2    �               import logger5�_�   7   9           8          ����                                                                                                                                                                                                                                                                                                                            	   	       	          V   ?    \y�    �               =            logger.log('wallet has an amount in it, exiting')5�_�   8   :           9          ����                                                                                                                                                                                                                                                                                                                            	   	       	          V   ?    \z|    �               >            logger.info('wallet has an amount in it, exiting')5�_�   9   ;           :          ����                                                                                                                                                                                                                                                                                                                            	   	       	          V   ?    \{%    �               ?            logger.error('wallet has an amount in it, exiting')5�_�   :   <           ;   	        ����                                                                                                                                                                                                                                                                                                                            	   	       	          V   ?    \{>     �      	          <logger = logging.getLogger('scripts.delete_user_and_wallet')5�_�   ;   =           <           ����                                                                                                                                                                                                                                                                                                                            	   	       	          V   ?    \{@    �                import logging5�_�   <               =   	        ����                                                                                                                                                                                                                                                                                                                               	                 V   ?    \{D    �      	           5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \v2     �               "    for private_wallet in wallets:5��