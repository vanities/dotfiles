Vim�UnDo� ����.e+^�Fk���8��i>��e޻R��   T                 '       '   '   '    ^V��    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ^UbW     �                   �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^UbX    �                  5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^Ub�    �         y      $class NanopoolService(ServiceUtils):5�_�                       A    ����                                                                                                                                                                                                                                                                                                                                                             ^Uc     �         y      W            .filter(config__wallet__coin__short_name__in=NanopoolService.enabled_coins)5�_�                      7    ����                                                                                                                                                                                                                                                                                                                                                             ^Uc     �         y      V            Coin.objects.filter(short_name__in=NanopoolService.enabled_earnings_coins)5�_�                    1   1    ����                                                                                                                                                                                                                                                                                                                                                             ^Uc     �   0   2   y      G            if wallet.coin.short_name in NanopoolService.enabled_coins:5�_�      	              1   :    ����                                                                                                                                                                                                                                                                                                                                                             ^Uc    �               y   import logging   import time   from decimal import Decimal       ;from coinmine.mineosminer.models import MineOSMiner, Config   %from coinmine.coin.models import Coin   Sfrom coinmine.worker.nanopool.api import load_account, payments, estimated_earnings   .from coinmine.worker.utils import ServiceUtils       5logger = logging.getLogger("worker.nanopool.service")           .class NanopoolAccountingService(ServiceUtils):   )    enabled_coins = ["eth", "xmr", "zec"]   :    enabled_earnings_coins = ["eth", "xmr", "zec", "grin"]           def filtered_miners():           return list(   /            MineOSMiner.objects.select_related(   B                "config", "config__wallet", "config__wallet__coin"               )                .exclude(owner=None)   a            .filter(config__wallet__coin__short_name__in=NanopoolAccountingService.enabled_coins)   	        )           def filtered_coins():           return list(   `            Coin.objects.filter(short_name__in=NanopoolAccountingService.enabled_earnings_coins)   	        )           def update_wallets(miners):   K        logger.info("updating {} miners from nanopool".format(len(miners)))               for miner in miners:   9            # Nanopool rate limit: 30 requests per minute               time.sleep(2)                   try:   ,                wallet = miner.config.wallet   '            except Config.DoesNotExist:                   logger.warning(   T                    "miner with config removed during nanopool run miner={}".format(                           miner                       )                   )                   continue       @            # during our run, ensure they haven't switched coins   Q            if wallet.coin.short_name in NanopoolAccountingService.enabled_coins:   C                logger.debug("processing wallet={}".format(wallet))       ?                wallet_dict = NanopoolService.make_wallet_dict(   Q                    wallet.coin.short_name, wallet.address, wallet.coin.usd_value                   )                       if wallet_dict:   M                    NanopoolService.update_model(logger, wallet, wallet_dict)   S                    NanopoolService.update_model(logger, miner.status, wallet_dict)       /    def update_coins_estimated_earnings(coins):           for coin in coins:   9            # Nanopool rate limit: 30 requests per minute               time.sleep(2)   -            coin_short_name = coin.short_name   )            if coin_short_name == "grin":   *                coin_short_name = "grin29"       7            coin_dict = NanopoolService.make_coin_dict(   8                coin_short_name, coin.estimated_hashrate               )   A            NanopoolService.update_model(logger, coin, coin_dict)       C    def make_wallet_dict(coin_short_name, address, coin_price_usd):           wallet_dict = {}       @        load_account_gw = load_account(coin_short_name, address)       -        if load_account_gw.status() is False:               logger.warning(   G                'skipping reason="load_account failure" e="{}"'.format(   +                    load_account_gw.error()                   )               )               return wallet_dict       S        wallet_dict["unpaid_balance"] = load_account_gw.to_dict()["unpaid_balance"]       8        payments_gw = payments(coin_short_name, address)   )        if payments_gw.status() is False:               logger.warning(   W                'skipping reason="payments failure" e="{}"'.format(payments_gw.error())               )               return wallet_dict       '        wallet_dict["amount_mined"] = (   L            wallet_dict["unpaid_balance"] + payments_gw.to_dict()["balance"]   	        )       V        wallet_dict["usd_value"] = float(coin_price_usd) * wallet_dict["amount_mined"]               return wallet_dict       A    def make_coin_dict(coin_short_name, coin_estimated_hashrate):           coin_dict = {}   O        earnings = estimated_earnings(coin_short_name, coin_estimated_hashrate)               if earnings.status():   @            btc_earnings = earnings.to_dict().get("btc_per_day")               if btc_earnings:   @                coin_dict["btc_per_day"] = Decimal(btc_earnings)       B            coin_earnings = earnings.to_dict().get("coin_per_day")               if coin_earnings:   B                coin_dict["coin_per_day"] = Decimal(coin_earnings)           else:               logger.warning(   L                'skipping reason="estimated_earnings failure e="{}"'.format(   $                    earnings.error()                   )               )           return coin_dict5�_�      
           	   8   &    ����                                                                                                                                                                                                                                                                                                                                                             ^Uc    �   7   9   }      ?                wallet_dict = NanopoolService.make_wallet_dict(5�_�   	              
   =       ����                                                                                                                                                                                                                                                                                                                                                             ^Uc    �   <   >   }      M                    NanopoolService.update_model(logger, wallet, wallet_dict)5�_�   
                 >       ����                                                                                                                                                                                                                                                                                                                                                             ^Uc     �   =   ?   }      S                    NanopoolService.update_model(logger, miner.status, wallet_dict)5�_�                    >   %    ����                                                                                                                                                                                                                                                                                                                                                             ^Uc    �               }   import logging   import time   from decimal import Decimal       ;from coinmine.mineosminer.models import MineOSMiner, Config   %from coinmine.coin.models import Coin   Sfrom coinmine.worker.nanopool.api import load_account, payments, estimated_earnings   .from coinmine.worker.utils import ServiceUtils       5logger = logging.getLogger("worker.nanopool.service")           .class NanopoolAccountingService(ServiceUtils):   )    enabled_coins = ["eth", "xmr", "zec"]   :    enabled_earnings_coins = ["eth", "xmr", "zec", "grin"]           def filtered_miners():           return list(   /            MineOSMiner.objects.select_related(   B                "config", "config__wallet", "config__wallet__coin"               )                .exclude(owner=None)               .filter(   \                config__wallet__coin__short_name__in=NanopoolAccountingService.enabled_coins               )   	        )           def filtered_coins():           return list(                Coin.objects.filter(   O                short_name__in=NanopoolAccountingService.enabled_earnings_coins               )   	        )           def update_wallets(miners):   K        logger.info("updating {} miners from nanopool".format(len(miners)))               for miner in miners:   9            # Nanopool rate limit: 30 requests per minute               time.sleep(2)                   try:   ,                wallet = miner.config.wallet   '            except Config.DoesNotExist:                   logger.warning(   T                    "miner with config removed during nanopool run miner={}".format(                           miner                       )                   )                   continue       @            # during our run, ensure they haven't switched coins   Q            if wallet.coin.short_name in NanopoolAccountingService.enabled_coins:   C                logger.debug("processing wallet={}".format(wallet))       I                wallet_dict = NanopoolAccountingService.make_wallet_dict(   Q                    wallet.coin.short_name, wallet.address, wallet.coin.usd_value                   )                       if wallet_dict:   W                    NanopoolAccountingService.update_model(logger, wallet, wallet_dict)   ]                    NanopoolAccountingService.update_model(logger, miner.status, wallet_dict)       /    def update_coins_estimated_earnings(coins):           for coin in coins:   9            # Nanopool rate limit: 30 requests per minute               time.sleep(2)   -            coin_short_name = coin.short_name   )            if coin_short_name == "grin":   *                coin_short_name = "grin29"       7            coin_dict = NanopoolService.make_coin_dict(   8                coin_short_name, coin.estimated_hashrate               )   A            NanopoolService.update_model(logger, coin, coin_dict)       C    def make_wallet_dict(coin_short_name, address, coin_price_usd):           wallet_dict = {}       @        load_account_gw = load_account(coin_short_name, address)       -        if load_account_gw.status() is False:               logger.warning(   G                'skipping reason="load_account failure" e="{}"'.format(   +                    load_account_gw.error()                   )               )               return wallet_dict       S        wallet_dict["unpaid_balance"] = load_account_gw.to_dict()["unpaid_balance"]       8        payments_gw = payments(coin_short_name, address)   )        if payments_gw.status() is False:               logger.warning(   W                'skipping reason="payments failure" e="{}"'.format(payments_gw.error())               )               return wallet_dict       '        wallet_dict["amount_mined"] = (   L            wallet_dict["unpaid_balance"] + payments_gw.to_dict()["balance"]   	        )       V        wallet_dict["usd_value"] = float(coin_price_usd) * wallet_dict["amount_mined"]               return wallet_dict       A    def make_coin_dict(coin_short_name, coin_estimated_hashrate):           coin_dict = {}   O        earnings = estimated_earnings(coin_short_name, coin_estimated_hashrate)               if earnings.status():   @            btc_earnings = earnings.to_dict().get("btc_per_day")               if btc_earnings:   @                coin_dict["btc_per_day"] = Decimal(btc_earnings)       B            coin_earnings = earnings.to_dict().get("coin_per_day")               if coin_earnings:   B                coin_dict["coin_per_day"] = Decimal(coin_earnings)           else:               logger.warning(   L                'skipping reason="estimated_earnings failure e="{}"'.format(   $                    earnings.error()                   )               )           return coin_dict5�_�                    J        ����                                                                                                                                                                                                                                                                                                                                                             ^Uc!    �   I   K         7            coin_dict = NanopoolService.make_coin_dict(5�_�                   M       ����                                                                                                                                                                                                                                                                                                                                                             ^Uc-   	 �   L   N         A            NanopoolService.update_model(logger, coin, coin_dict)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^U��     �               Sfrom coinmine.worker.nanopool.api import load_account, payments, estimated_earnings5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                             ^U��   
 �               ffrom coinmine.pools.apis.nanopoolworker.nanopool.api import load_account, payments, estimated_earnings5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             ^U��     �   	            5logger = logging.getLogger("worker.nanopool.service")5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             ^U��    �   	            logger = logging.getLogger("")5�_�                            ����                                                                                                                                                                                                                                                                                                                                       !           V        ^V�@     �                        def filtered_coins():           return list(                Coin.objects.filter(   O                short_name__in=NanopoolAccountingService.enabled_earnings_coins               )   	        )5�_�                            ����                                                                                                                                                                                                                                                                                                                                       
           V        ^V�U     �                %from coinmine.coin.models import Coin5�_�                    :        ����                                                                                                                                                                                                                                                                                                                            :          E          V       ^V�v     �   9   :          /    def update_coins_estimated_earnings(coins):           for coin in coins:   9            # Nanopool rate limit: 30 requests per minute               time.sleep(2)   -            coin_short_name = coin.short_name   )            if coin_short_name == "grin":   *                coin_short_name = "grin29"       A            coin_dict = NanopoolAccountingService.make_coin_dict(   8                coin_short_name, coin.estimated_hashrate               )   K            NanopoolAccountingService.update_model(logger, coin, coin_dict)5�_�                    X        ����                                                                                                                                                                                                                                                                                                                            X           k          V       ^V��     �   W   X              A    def make_coin_dict(coin_short_name, coin_estimated_hashrate):           coin_dict = {}   O        earnings = estimated_earnings(coin_short_name, coin_estimated_hashrate)               if earnings.status():   @            btc_earnings = earnings.to_dict().get("btc_per_day")               if btc_earnings:   @                coin_dict["btc_per_day"] = Decimal(btc_earnings)       B            coin_earnings = earnings.to_dict().get("coin_per_day")               if coin_earnings:   B                coin_dict["coin_per_day"] = Decimal(coin_earnings)           else:               logger.warning(   L                'skipping reason="estimated_earnings failure e="{}"'.format(   $                    earnings.error()                   )               )           return coin_dict5�_�                           ����                                                                                                                                                                                                                                                                                                                            X           X          V       ^V��    �               W   import logging   import time   from decimal import Decimal       ;from coinmine.mineosminer.models import MineOSMiner, Config   Sfrom coinmine.pools.apis.nanopool import load_account, payments, estimated_earnings   .from coinmine.worker.utils import ServiceUtils       $logger = logging.getLogger(__name__)           .class NanopoolAccountingService(ServiceUtils):   )    enabled_coins = ["eth", "xmr", "zec"]   :    enabled_earnings_coins = ["eth", "xmr", "zec", "grin"]           def filtered_miners():           return list(   /            MineOSMiner.objects.select_related(   B                "config", "config__wallet", "config__wallet__coin"               )                .exclude(owner=None)               .filter(   \                config__wallet__coin__short_name__in=NanopoolAccountingService.enabled_coins               )   	        )           def update_wallets(miners):   K        logger.info("updating {} miners from nanopool".format(len(miners)))               for miner in miners:   9            # Nanopool rate limit: 30 requests per minute               time.sleep(2)                   try:   ,                wallet = miner.config.wallet   '            except Config.DoesNotExist:                   logger.warning(   T                    "miner with config removed during nanopool run miner={}".format(                           miner                       )                   )                   continue       @            # during our run, ensure they haven't switched coins   Q            if wallet.coin.short_name in NanopoolAccountingService.enabled_coins:   C                logger.debug("processing wallet={}".format(wallet))       I                wallet_dict = NanopoolAccountingService.make_wallet_dict(   Q                    wallet.coin.short_name, wallet.address, wallet.coin.usd_value                   )                       if wallet_dict:   W                    NanopoolAccountingService.update_model(logger, wallet, wallet_dict)   ;                    NanopoolAccountingService.update_model(   9                        logger, miner.status, wallet_dict                       )           C    def make_wallet_dict(coin_short_name, address, coin_price_usd):           wallet_dict = {}       @        load_account_gw = load_account(coin_short_name, address)       -        if load_account_gw.status() is False:               logger.warning(   G                'skipping reason="load_account failure" e="{}"'.format(   +                    load_account_gw.error()                   )               )               return wallet_dict       S        wallet_dict["unpaid_balance"] = load_account_gw.to_dict()["unpaid_balance"]       8        payments_gw = payments(coin_short_name, address)   )        if payments_gw.status() is False:               logger.warning(   W                'skipping reason="payments failure" e="{}"'.format(payments_gw.error())               )               return wallet_dict       '        wallet_dict["amount_mined"] = (   L            wallet_dict["unpaid_balance"] + payments_gw.to_dict()["balance"]   	        )       V        wallet_dict["usd_value"] = float(coin_price_usd) * wallet_dict["amount_mined"]               return wallet_dict5�_�                            ����                                                                                                                                                                                                                                                                                                                            W           W          V       ^V��    �                from decimal import Decimal5�_�                       ?    ����                                                                                                                                                                                                                                                                                                                            V           V          V       ^V��    �         U      Sfrom coinmine.pools.apis.nanopool import load_account, payments, estimated_earnings5�_�                           ����                                                                                                                                                                                                                                                                                                                            V           V          V       ^V��    �                :    enabled_earnings_coins = ["eth", "xmr", "zec", "grin"]5�_�                           ����                                                                                                                                                                                                                                                                                                                            U           U          V       ^V��     �         U              �         T    5�_�                           ����                                                                                                                                                                                                                                                                                                                            W           W          V       ^V��    �         W              �         V    5�_�                     5       ����                                                                                                                                                                                                                                                                                                                            X           X          V       ^V��     �   5   7   X                          �   5   7   W    5�_�      !               6   +    ����                                                                                                                                                                                                                                                                                                                            Y           Y          V       ^V��     �   5   7   X      ,                    wallets.append(Wallet())5�_�       "           !   6   #    ����                                                                                                                                                                                                                                                                                                                            Y           Y          V       ^V��     �   5   7   X      $                    wallets.append()5�_�   !   #           "   6       ����                                                                                                                                                                                                                                                                                                                            Y           Y          V       ^V�)     �   5   6          ,                    wallets.append(wallet.d)5�_�   "   $           #           ����                                                                                                                                                                                                                                                                                                                                                 V       ^V�,    �                        wallets = []           status = []    5�_�   #   %           $           ����                                                                                                                                                                                                                                                                                                                                                             ^V��     �      
   T    �      	   T    5�_�   $   &           %           ����                                                                                                                                                                                                                                                                                                                                                             ^V��     �                $logger = logging.getLogger(__name__)5�_�   %   '           &           ����                                                                                                                                                                                                                                                                                                                                                             ^V��     �         T    �         T    5�_�   &               '           ����                                                                                                                                                                                                                                                                                                                                                             ^V��    �                 import logging5�_�                   M       ����                                                                                                                                                                                                                                                                                                                                                             ^Uc'     �   L   N         @            NanopolService.update_model(logger, coin, coin_dict)5�_�                    M       ����                                                                                                                                                                                                                                                                                                                                                             ^Uc$     �   L   N         @            NanopoolServie.update_model(logger, coin, coin_dict)5�_�                       8    ����                                                                                                                                                                                                                                                                                                                                                             ^Uc	     �         y      `            Coin.objects.filter(short_name__in=NanopoolSAccountingervice.enabled_earnings_coins)5��