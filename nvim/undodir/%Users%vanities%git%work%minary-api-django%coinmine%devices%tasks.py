Vim�UnDo� ��8�ƀ'q����Vؚvdw
"@�d�7w�9      W    logger.info("Support Miner Polling Interval {} secs".format(polling_interval_secs))      @      A       A   A   A    ^D<�    _�                             ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�E     �                import logging5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�G     �   	      '    �   	   
   '    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�K     �                 =from apscheduler.schedulers.blocking import BlockingScheduler   	import os   import django5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�K     �                  5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�L     �                 django.setup()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�O     �          #      Efrom coinmine.worker.support_miner.service import SupportMinerService5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�T     �          #      Ofrom coinmine.devices.services.support_miner.service import SupportMinerService5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�W     �          #      Bfrom coinmine.devices.services..service import SupportMinerService5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�X     �          #      :from coinmine.devices.services. import SupportMinerService5�_�   	              
      2    ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�\     �          #      9from coinmine.devices.services import SupportMinerService5�_�   
                    ;    ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�^    �               #   Cfrom coinmine.devices.services import SupportMinerAccountingService   %from coinmine.coin.models import Coin   ,from coinmine.user.models import UserProfile       import logging   8logger = logging.getLogger("worker.support_miner.clock")   scheduler = BlockingScheduler()       Spolling_interval_secs = int(os.getenv("SUPPORT_MINER_POLLING_INTERVAL_SECS", 1800))           def job(polling_interval_secs):   W    logger.info("Support Miner Polling Interval {} secs".format(polling_interval_secs))   2    logger.info("Running Support Miner Worker...")           default_fee = float(           os.getenv(   U            "FEE_PERCENTAGE_DECIMAL", UserProfile.lookup_fee(UserProfile.GENERAL_FEE)   	        )       )       0    bitcoin = Coin.objects.get(short_name="btc")       '    SupportMinerService.update_credits(   .        SupportMinerService.filtered_miners(),           bitcoin.usd_value,           polling_interval_secs,           default_fee,       )           # scheduler.add_job(   R#    lambda: job(polling_interval_secs), "interval", seconds=polling_interval_secs   # )   # scheduler.start()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�e     �         $      '    SupportMinerService.update_credits(5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�h     �                        bitcoin.usd_value,5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�h    �               #   Cfrom coinmine.devices.services import SupportMinerAccountingService   %from coinmine.coin.models import Coin   ,from coinmine.user.models import UserProfile       import logging       8logger = logging.getLogger("worker.support_miner.clock")   scheduler = BlockingScheduler()       Spolling_interval_secs = int(os.getenv("SUPPORT_MINER_POLLING_INTERVAL_SECS", 1800))           def job(polling_interval_secs):   W    logger.info("Support Miner Polling Interval {} secs".format(polling_interval_secs))   2    logger.info("Running Support Miner Worker...")           default_fee = float(           os.getenv(   U            "FEE_PERCENTAGE_DECIMAL", UserProfile.lookup_fee(UserProfile.GENERAL_FEE)   	        )       )       0    bitcoin = Coin.objects.get(short_name="btc")       1    SupportMinerAccountingService.update_credits(   .        SupportMinerService.filtered_miners(),           polling_interval_secs,           default_fee,       )           # scheduler.add_job(   R#    lambda: job(polling_interval_secs), "interval", seconds=polling_interval_secs   # )   # scheduler.start()5�_�                            ����                                                                                                                                                                                                                                                                                                                                       !           V        ^C�k    �                        # scheduler.add_job(   R#    lambda: job(polling_interval_secs), "interval", seconds=polling_interval_secs   # )   # scheduler.start()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�m     �                0    bitcoin = Coin.objects.get(short_name="btc")5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�n    �                  Cfrom coinmine.devices.services import SupportMinerAccountingService   %from coinmine.coin.models import Coin   ,from coinmine.user.models import UserProfile       import logging       8logger = logging.getLogger("worker.support_miner.clock")   scheduler = BlockingScheduler()       Spolling_interval_secs = int(os.getenv("SUPPORT_MINER_POLLING_INTERVAL_SECS", 1800))           def job(polling_interval_secs):   W    logger.info("Support Miner Polling Interval {} secs".format(polling_interval_secs))   2    logger.info("Running Support Miner Worker...")           default_fee = float(           os.getenv(   U            "FEE_PERCENTAGE_DECIMAL", UserProfile.lookup_fee(UserProfile.GENERAL_FEE)   	        )       )           1    SupportMinerAccountingService.update_credits(   Q        SupportMinerService.filtered_miners(), polling_interval_secs, default_fee       )5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�}    �                %from coinmine.coin.models import Coin5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�     �                ,from coinmine.user.models import UserProfile5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ^C��    �              �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^C��    �                scheduler = BlockingScheduler()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ^C��     �              �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^C��    �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^C��     �                import logging5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^C��   	 �              �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^C��     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                    V        ^C��   
 �               def job(polling_interval_secs):5�_�                            ����                                                                                                                                                                                                                                                                                                                                                    V        ^C��    �             �             5�_�                             ����                                                                                                                                                                                                                                                                                                                            "           "           V        ^C��     �                )from celery.task.schedules import crontab5�_�      !                       ����                                                                                                                                                                                                                                                                                                                            !           !           V        ^C��    �              �              5�_�       "           !      &    ����                                                                                                                                                                                                                                                                                                                            "           "           V        ^C�     �         !      Spolling_interval_secs = int(os.getenv("SUPPORT_MINER_POLLING_INTERVAL_SECS", 1800))5�_�   !   #           "      "    ����                                                                                                                                                                                                                                                                                                                            "           "           V        ^C�	     �         !      Npolling_interval_secs = settings."SUPPORT_MINER_POLLING_INTERVAL_SECS", 1800))5�_�   "   $           #      M    ����                                                                                                                                                                                                                                                                                                                            "           "           V        ^C�
    �         !      Mpolling_interval_secs = settings.SUPPORT_MINER_POLLING_INTERVAL_SECS", 1800))5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                            "           "           V        ^C�)     �         !      ;    run_every=crontab(hour=0, minute=10, day_of_month="1"),�         !    5�_�   $   &           %      2    ����                                                                                                                                                                                                                                                                                                                            "           "           V        ^C�*     �         !      _    run_every=timedelta(seconds=accounting_period)crontab(hour=0, minute=10, day_of_month="1"),5�_�   %   '           &      3    ����                                                                                                                                                                                                                                                                                                                            "           "           V        ^C�0    �         !      Q    run_every=timedelta(seconds=accounting_period), minute=10, day_of_month="1"),5�_�   &   )           '      .    ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C�2     �                .    # execute on the first day of every month.   B    # after the interests calculation, prepping for the next month5�_�   '   +   (       )           ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C�;     �             �             5�_�   )   ,   *       +      	    ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C�B     �                %    name="create_balanced_snapshots",�              5�_�   +   -           ,      '    ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C�C     �                B    name="update_support_miner_balancescreate_balanced_snapshots",5�_�   ,   .           -      '    ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C�D    �                   import logging   from datetime import timedelta    from django.conf import settings   )from celery.task.schedules import crontab   +from celery.decorators import periodic_task       ,from coinmine.user.models import UserProfile   Cfrom coinmine.devices.services import SupportMinerAccountingService           8logger = logging.getLogger("worker.support_miner.clock")       Dpolling_interval_secs = settings.SUPPORT_MINER_POLLING_INTERVAL_SECS           @periodic_task(   3    run_every=timedelta(seconds=accounting_period),   )    name="update_support_miner_balances",   )   9def update_support_miner_balances(polling_interval_secs):   W    logger.info("Support Miner Polling Interval {} secs".format(polling_interval_secs))   2    logger.info("Running Support Miner Worker...")           default_fee = float(           os.getenv(   U            "FEE_PERCENTAGE_DECIMAL", UserProfile.lookup_fee(UserProfile.GENERAL_FEE)   	        )       )       1    SupportMinerAccountingService.update_credits(   Q        SupportMinerService.filtered_miners(), polling_interval_secs, default_fee       )5�_�   -   /           .           ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C�L     �               Dpolling_interval_secs = settings.SUPPORT_MINER_POLLING_INTERVAL_SECS5�_�   .   0           /           ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C�M    �               / = settings.SUPPORT_MINER_POLLING_INTERVAL_SECS5�_�   /   1           0           ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C�U    �                )from celery.task.schedules import crontab5�_�   0   2           1          ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C�c     �                        os.getenv(5�_�   1   3           2          ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C�e     �               U            "FEE_PERCENTAGE_DECIMAL", UserProfile.lookup_fee(UserProfile.GENERAL_FEE)5�_�   2   4           3          ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C�g     �                	        )5�_�   3   5           4          ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C�g    �                  import logging   from datetime import timedelta    from django.conf import settings   +from celery.decorators import periodic_task       ,from coinmine.user.models import UserProfile   Cfrom coinmine.devices.services import SupportMinerAccountingService           8logger = logging.getLogger("worker.support_miner.clock")       @accounting_period = settings.SUPPORT_MINER_POLLING_INTERVAL_SECS           @periodic_task(   X    run_every=timedelta(seconds=accounting_period), name="update_support_miner_balances"   )   9def update_support_miner_balances(polling_interval_secs):   W    logger.info("Support Miner Polling Interval {} secs".format(polling_interval_secs))   2    logger.info("Running Support Miner Worker...")           default_fee = float(   ;            UserProfile.lookup_fee(UserProfile.GENERAL_FEE)       )       1    SupportMinerAccountingService.update_credits(   Q        SupportMinerService.filtered_miners(), polling_interval_secs, default_fee       )5�_�   4   6           5      /    ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C�v     �               Q        SupportMinerService.filtered_miners(), polling_interval_secs, default_fee5�_�   5   7           6      /    ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C�w    �               <        SupportMinerService.filtered_miners(), , default_fee5�_�   6   8           7          ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C��     �               M        SupportMinerService.filtered_miners(), accounting_period, default_fee5�_�   7   9           8          ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C��     �                   �             5�_�   8   :           9          ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C��     �                   miners = �             5�_�   9   ;           :          ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C��     �               (        , accounting_period, default_fee5�_�   :   <           ;          ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C��    �                  import logging   from datetime import timedelta    from django.conf import settings   +from celery.decorators import periodic_task       ,from coinmine.user.models import UserProfile   Cfrom coinmine.devices.services import SupportMinerAccountingService           8logger = logging.getLogger("worker.support_miner.clock")       @accounting_period = settings.SUPPORT_MINER_POLLING_INTERVAL_SECS           @periodic_task(   X    run_every=timedelta(seconds=accounting_period), name="update_support_miner_balances"   )   9def update_support_miner_balances(polling_interval_secs):   W    logger.info("Support Miner Polling Interval {} secs".format(polling_interval_secs))   2    logger.info("Running Support Miner Worker...")       H    default_fee = float(UserProfile.lookup_fee(UserProfile.GENERAL_FEE))   2    miners = SupportMinerService.filtered_miners()       1    SupportMinerAccountingService.update_credits(   .        miners, accounting_period, default_fee       )5�_�   ;   =           <          ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C��     �               2    miners = SupportMinerService.filtered_miners()5�_�   <   ?           =          ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C��    �               4    miners = SupportMinerAcService.filtered_miners()5�_�   =   @   >       ?      "    ����                                                                                                                                                                                                                                                                                                                                                             ^D<�     �               9def update_support_miner_balances(polling_interval_secs):5�_�   ?   A           @      @    ����                                                                                                                                                                                                                                                                                                                                                             ^D<�     �               W    logger.info("Support Miner Polling Interval {} secs".format(polling_interval_secs))5�_�   @               A      @    ����                                                                                                                                                                                                                                                                                                                                                             ^D<�    �               B    logger.info("Support Miner Polling Interval {} secs".format())5�_�   =           ?   >          ����                                                                                                                                                                                                                                                                                                                                                             ^D8     �               accounting_period = settings.5�_�   )           +   *          ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C�@     �                def (polling_interval_secs):5�_�   '           )   (           ����                                                                                                                                                                                                                                                                                                                               2          .       V   2    ^C�:     �             �               from datetime import timedelta5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^C��     �             �               ,from coinmine.user.models import UserProfile5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^C�o     �              5��