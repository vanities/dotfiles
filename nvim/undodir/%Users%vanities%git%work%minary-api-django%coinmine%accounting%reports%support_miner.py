Vim�UnDo� ş�^��?�R��&t�v"٭�o�4<3�]#���   .   J    def __init__(self, report_period_seconds, accumulated_period_seconds):      .                       ^��?    _�                            ����                                                                                                                                                                                                                                                                                                                                                             ^��     �         .      3    def __init__(self, accumulated_period_seconds):5�_�                      9    ����                                                                                                                                                                                                                                                                                                                                                             ^��6    �               .   from decimal import Decimal        from django.db.models import Sum       0from coinmine.devices.models import SupportMiner   5from coinmine.balance_adjustment.models import Credit   .from coinmine.worker.utils import ServiceUtils   >from coinmine.accounting.reports.base_report import BaseReport           %class SupportMinerReport(BaseReport):   J    def __init__(self, report_period_seconds, accumulated_period_seconds):   #        self.service = ServiceUtils   D        self.accumulated_period_seconds = accumulated_period_seconds           def generate(self, coins):   G        report = {"accounting_period": self.accumulated_period_seconds}           for coin in coins:   !            report[coin.name] = {   <                "miner_count": self._get_miners_count(coin),   ,                "usd_value": coin.usd_value,   ;                "coin_short_name": coin.short_name.upper(),   ?                "total_credits": self._get_total_credits(coin),   G                "total_credits_usd": self._get_total_credits_usd(coin),   2                "coin_per_day": coin.coin_per_day,   0                "btc_per_day": coin.btc_per_day,   B                "usd_per_day": coin.coin_per_day * coin.usd_value,   3                "tier_rates": self._get_tier_rates(   :                    coin, self.accumulated_period_seconds,                   ),               }           return report       &    def _get_miners_count(self, coin):   B        return len(SupportMiner.objects.filter(wallet__coin=coin))       '    def _get_total_credits(self, coin):           return (   T            Credit.objects.filter(coin=coin, support_miner__isnull=False).aggregate(   /                Sum("amount_in_smallest_units")   .            )["amount_in_smallest_units__sum"]               or Decimal(0)           ) * coin.smallest_unit       +    def _get_total_credits_usd(self, coin):   =        return self._get_total_credits(coin) * coin.usd_value5�_�                        .    ����                                                                                                                                                                                                                                                                                                                                                             ^��>    �         .      J    def __init__(self, report_period_seconds, accumulated_period_seconds):5�_�                      9    ����                                                                                                                                                                                                                                                                                                                                                             ^��     �         .      I    def __init__(self, report_period_seconds, accounting_period_seconds):5�_�                      5    ����                                                                                                                                                                                                                                                                                                                                                             ^��b     �         .      C        self.accumulated_period_seconds = accounting_period_seconds5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^��h     �         .      B        self.accounting_period_seconds = accounting_period_seconds5�_�                       7    ����                                                                                                                                                                                                                                                                                                                                                             ^��k     �         .      F        report = {"accounting_period": self.accounting_period_seconds}5�_�                       *    ����                                                                                                                                                                                                                                                                                                                                                             ^��n     �         .      9                    coin, self.accounting_period_seconds,5�_�                        (    ����                                                                                                                                                                                                                                                                                                                                                             ^��o    �       /       .   from decimal import Decimal        from django.db.models import Sum       0from coinmine.devices.models import SupportMiner   5from coinmine.balance_adjustment.models import Credit   .from coinmine.worker.utils import ServiceUtils   >from coinmine.accounting.reports.base_report import BaseReport           %class SupportMinerReport(BaseReport):   I    def __init__(self, report_period_seconds, accounting_period_seconds):   #        self.service = ServiceUtils   B        self.accounting_period_seconds = accounting_period_seconds           def generate(self, coins):   F        report = {"accounting_period": self.accounting_period_seconds}           for coin in coins:   !            report[coin.name] = {   <                "miner_count": self._get_miners_count(coin),   ,                "usd_value": coin.usd_value,   ;                "coin_short_name": coin.short_name.upper(),   ?                "total_credits": self._get_total_credits(coin),   G                "total_credits_usd": self._get_total_credits_usd(coin),   2                "coin_per_day": coin.coin_per_day,   0                "btc_per_day": coin.btc_per_day,   B                "usd_per_day": coin.coin_per_day * coin.usd_value,   3                "tier_rates": self._get_tier_rates(   8                    coin, self.accounting_period_seconds                   ),               }           return report       &    def _get_miners_count(self, coin):   B        return len(SupportMiner.objects.filter(wallet__coin=coin))       '    def _get_total_credits(self, coin):           return (   T            Credit.objects.filter(coin=coin, support_miner__isnull=False).aggregate(   /                Sum("amount_in_smallest_units")   .            )["amount_in_smallest_units__sum"]               or Decimal(0)           ) * coin.smallest_unit       +    def _get_total_credits_usd(self, coin):   =        return self._get_total_credits(coin) * coin.usd_value5�_�                      5    ����                                                                                                                                                                                                                                                                                                                                                             ^��`     �         .      ?        self.accumulated_period_seconds = report_period_seconds5�_�                      "    ����                                                                                                                                                                                                                                                                                                                                                             ^��$     �         .              �         /              self.5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^��&     �              5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^��'     �         .      ?        self.report_period_seconds = accumulated_period_seconds5�_�                       0    ����                                                                                                                                                                                                                                                                                                                                                             ^��,     �         .      :        self.report_period_seconds = report_period_seconds5�_�                       *    ����                                                                                                                                                                                                                                                                                                                                                             ^��-     �         .    �         .      :        self.report_period_seconds = report_period_seconds5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             ^��/     �         /      >        self.accounting_period_seconds = report_period_seconds5�_�      
           	      /    ����                                                                                                                                                                                                                                                                                                                                                             ^��3     �         /      B        self.accounting_period_seconds = accounting_period_seconds5�_�   	              
      2    ����                                                                                                                                                                                                                                                                                                                                                             ^��4    �       0       /   from decimal import Decimal        from django.db.models import Sum       0from coinmine.devices.models import SupportMiner   5from coinmine.balance_adjustment.models import Credit   .from coinmine.worker.utils import ServiceUtils   >from coinmine.accounting.reports.base_report import BaseReport           %class SupportMinerReport(BaseReport):   I    def __init__(self, report_period_seconds, accounting_period_seconds):   #        self.service = ServiceUtils   :        self.report_period_seconds = report_period_seconds   B        self.accounting_period_seconds = accounting_period_seconds           def generate(self, coins):   G        report = {"accounting_period": self.accumulated_period_seconds}           for coin in coins:   !            report[coin.name] = {   <                "miner_count": self._get_miners_count(coin),   ,                "usd_value": coin.usd_value,   ;                "coin_short_name": coin.short_name.upper(),   ?                "total_credits": self._get_total_credits(coin),   G                "total_credits_usd": self._get_total_credits_usd(coin),   2                "coin_per_day": coin.coin_per_day,   0                "btc_per_day": coin.btc_per_day,   B                "usd_per_day": coin.coin_per_day * coin.usd_value,   3                "tier_rates": self._get_tier_rates(   9                    coin, self.accumulated_period_seconds                   ),               }           return report       &    def _get_miners_count(self, coin):   B        return len(SupportMiner.objects.filter(wallet__coin=coin))       '    def _get_total_credits(self, coin):           return (   T            Credit.objects.filter(coin=coin, support_miner__isnull=False).aggregate(   /                Sum("amount_in_smallest_units")   .            )["amount_in_smallest_units__sum"]               or Decimal(0)           ) * coin.smallest_unit       +    def _get_total_credits_usd(self, coin):   =        return self._get_total_credits(coin) * coin.usd_value5�_�   
                     7    ����                                                                                                                                                                                                                                                                                                                                                             ^��8     �         /      B        report = {"accounting_period": self.report_period_seconds}5��