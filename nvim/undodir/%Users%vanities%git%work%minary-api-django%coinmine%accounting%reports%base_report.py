Vim�UnDo� ]�Vԉ����ɬ	��t��(X����^j�\�   !                                  ^P&g    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ^P�     �                   5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^P�     �                     �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^P�    �                 9    def _get_tier_rates(self, accumulated_period_seconds)5�_�                       G    ����                                                                                                                                                                                                                                                                                                                                                             ^P�     �                 G    def _get_tier_rates(self, coin_per_day, accumulated_period_seconds)5�_�                       *    ����                                                                                                                                                                                                                                                                                                                                                             ^P�    �                 H    def _get_tier_rates(self, coin_per_day, accumulated_period_seconds):5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                             ^P�     �               �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ^P�    �                  class BaseReport:       @    def _get_tier_rates(self, coin, accumulated_period_seconds):   %        rate = self.coin.coin_per_day           result = {}       0        for fee in UserProfile.USER_FEE_CHOICES:               fee_id = fee[0]               fee_rate = fee[1]   3            fee_name = UserProfile.fee_name(fee_id)       T            units_earned_per_second = self.service.adjusted_units_earned_per_second(   7                rate, self.coin.smallest_unit, fee_rate               )   O            units_earned = units_earned_per_second * accumulated_period_seconds   @            coin_earned = self.service.smallest_unit_to_decimal(   5                units_earned, self.coin.smallest_unit               )   :            usd_earned = coin_earned * self.coin.usd_value                    result[fee_name] = {   %                "fee_rate": fee_rate,   +                "coin_earned": coin_earned,   )                "usd_earned": usd_earned,               }           return result5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             ^P�     �               %        rate = self.coin.coin_per_day5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             ^P�     �               7                rate, self.coin.smallest_unit, fee_rate5�_�   	              
      '    ����                                                                                                                                                                                                                                                                                                                                                             ^P�     �               :            usd_earned = coin_earned * self.coin.usd_value5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             ^P�    �               5                units_earned, self.coin.smallest_unit5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^P�     �              �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^P�     �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^P�    �                  ,from coinmine.user.models import UserProfile       class BaseReport:   @    def _get_tier_rates(self, coin, accumulated_period_seconds):            rate = coin.coin_per_day           result = {}       0        for fee in UserProfile.USER_FEE_CHOICES:               fee_id = fee[0]               fee_rate = fee[1]   3            fee_name = UserProfile.fee_name(fee_id)       T            units_earned_per_second = self.service.adjusted_units_earned_per_second(   2                rate, coin.smallest_unit, fee_rate               )   O            units_earned = units_earned_per_second * accumulated_period_seconds   @            coin_earned = self.service.smallest_unit_to_decimal(   0                units_earned, coin.smallest_unit               )   5            usd_earned = coin_earned * coin.usd_value                    result[fee_name] = {   %                "fee_rate": fee_rate,   +                "coin_earned": coin_earned,   )                "usd_earned": usd_earned,               }           return result5�_�                            ����                                                                                                                                                                                                                                                                                                                               '          5       v   <    ^P&b     �      "       �             5�_�                     "        ����                                                                                                                                                                                                                                                                                                                            "          9          V       ^P&f    �   !   "          @    def _get_tier_rates(self, coin, accumulated_period_seconds):            rate = coin.coin_per_day           result = {}       0        for fee in UserProfile.USER_FEE_CHOICES:               fee_id = fee[0]               fee_rate = fee[1]   3            fee_name = UserProfile.fee_name(fee_id)       T            units_earned_per_second = self.service.adjusted_units_earned_per_second(   2                rate, coin.smallest_unit, fee_rate               )   O            units_earned = units_earned_per_second * accumulated_period_seconds   @            coin_earned = self.service.smallest_unit_to_decimal(   0                units_earned, coin.smallest_unit               )   5            usd_earned = coin_earned * coin.usd_value                    result[fee_name] = {   %                "fee_rate": fee_rate,   +                "coin_earned": coin_earned,   )                "usd_earned": usd_earned,               }           return result5��