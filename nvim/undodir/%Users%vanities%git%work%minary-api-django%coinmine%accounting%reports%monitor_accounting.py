Vim�UnDo� qR�nn��)��w���w~�����V�����   E                                  ^�Q�    _�                    ,       ����                                                                                                                                                                                                                                                                                                                                                             ^�Q�     �   +   -   F              ] * float(5�_�                    ,       ����                                                                                                                                                                                                                                                                                                                                                             ^�Q�     �   +   -   F              ] *                coin.smallest_unit5�_�                    -       ����                                                                                                                                                                                                                                                                                                                                                             ^�Q�     �   ,   -          	        )5�_�                     -        ����                                                                                                                                                                                                                                                                                                                                                             ^�Q�    �               D   from time import sleep        from django.db.models import Sum   /from django.db.models.functions import Coalesce       <from coinmine.balance_adjustment.models import MiningBalance   %from coinmine.coin.models import Coin   5from coinmine.pools.apis.nanopool import load_account   )from coinmine.wallet.models import Wallet           class MonitorAccounting:   B    def __init__(self, username_filter="", description_filter=""):   .        self.username_filter = username_filter   4        self.description_filter = description_filter           def run(self):   +        for coin in self._coins_queryset():   %            self._print_summary(coin)           def _coins_queryset(self):   W        return Coin.objects.filter(short_name__in=["eth", "xmr", "grin", "hns", "zec"])       &    def _wallets_queryset(self, coin):   %        return Wallet.objects.filter(   F            coin=coin, owner__username__icontains=self.username_filter   	        )       #    def _print_summary(self, coin):   -        print("{} Totals:".format(coin.name))   I        print("   Mining   {:.8f}".format(self._get_balance_total(coin)))   H        print("   Wallet   {:.8f}".format(self._get_wallet_total(coin)))       L        # print(" Pool API   {:.8f}".format(self._get_poolside_total(coin)))           print("")       '    def _get_balance_total(self, coin):   ,        return MiningBalance.objects.filter(               coin=coin,   ;            description__icontains=self.description_filter,   <            owner__username__icontains=self.username_filter,   H        ).aggregate(total=Coalesce(Sum("amount_in_smallest_units"), 0))[               "total"           ] * coin.smallest_unit       &    def _get_wallet_total(self, coin):           return (   (            self._wallets_queryset(coin)   1            .aggregate(total=Sum("amount_mined"))               .get("total")   	        )       (    def _get_poolside_total(self, coin):           unpaid_balance = 0.0   3        for wallet in self._wallets_queryset(coin):   M            unpaid_balance += self._get_poolside_unpaid_balance(coin, wallet)               sleep(2)           return unpaid_balance       9    def _get_poolside_unpaid_balance(self, coin, wallet):   4        if coin.short_name in ["eth", "xmr", "zec"]:               return (   =                load_account(coin.short_name, wallet.address)                   .to_dict()   +                .get("unpaid_balance", 0.0)               )           else:               return 0.05�_�                     ,       ����                                                                                                                                                                                                                                                                                                                                                             ^�Q�     �   +   -   F              ] * 5��