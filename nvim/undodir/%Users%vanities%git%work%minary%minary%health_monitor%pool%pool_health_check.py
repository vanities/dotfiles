Vim�UnDo� h�0�����W��w-��W�Py0�?�G{L7�Q      <            "zcash": nanopool_hashrate("zec", self.address),      :      L       L   L   L    ]9�    _�                            ����                                                                                                                                                                                                                                                                                                                                                             ]/[�     �                       �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]/\     �               
        {}5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]/\     �                       hashrate = {}5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]/\     �                       hashrate = {"ethereum"}5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]/\�    �             �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]/\�     �               /from health_monitor.pool import HashrateGateway5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]/\�     �                from health_monitor.pool import 5�_�      	                 (    ����                                                                                                                                                                                                                                                                                                                                                             ]/\�    �               (from health_monitor.pool import hashrate5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                             ]/\�     �               !        hashrate = {"ethereum": }5�_�   	              
      7    ����                                                                                                                                                                                                                                                                                                                                                             ]/\�     �               9        hashrate = {"ethereum": nanopool_hashrate('eth')}5�_�   
                    D    ����                                                                                                                                                                                                                                                                                                                                                             ]/\�    �                  ,from health_monitor import BaseHealthChecker        from utils import CoinmineLogger   =from health_monitor.pool import hashrate as nanopool_hashrate       !logger = CoinmineLogger(__name__)           +class PoolHealthChecker(BaseHealthChecker):   &    def __init__(self, coin, address):           self.coin = coin           self.address = address           def _is_healthy(self):   '        hashrate = self._get_hashrate()           if hashrate:               return True           else:               return False           def _get_hashrate(self):   G        hashrate = {"ethereum": nanopool_hashrate('eth', self.address)}           pass5�_�                      F    ����                                                                                                                                                                                                                                                                                                                                                             ]/\�     �               G        hashrate = {"ethereum": nanopool_hashrate("eth", self.address)}5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]/\�     �                �             �             5�_�                            ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/\�     �               3"ethereum": nanopool_hashrate("eth", self.address)}5�_�                            ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/\�     �               7    "ethereum": nanopool_hashrate("eth", self.address)}5�_�                            ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/\�     �               ;        "ethereum": nanopool_hashrate("eth", self.address)}5�_�                            ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/\�     �               ?            "ethereum": nanopool_hashrate("eth", self.address)}5�_�                            ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/\�     �               C                "ethereum": nanopool_hashrate("eth", self.address)}5�_�                           ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/\�     �               G                    "ethereum": nanopool_hashrate("eth", self.address)}5�_�                       4    ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/\�     �               E                    "monero": nanopool_hashrate("eth", self.address)}5�_�                       3    ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/\�     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/\�     �               E                    "monero": nanopool_hashrate("xmr", self.address)}5�_�                           ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/\�     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/\�     �               E                    "monero": nanopool_hashrate("xmr", self.address)}5�_�                       3    ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/\�     �               D                    "zcash": nanopool_hashrate("xmr", self.address)}5�_�                       2    ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/\�    �               C                    "grin": nanopool_hashrate("xmr", self.address)}5�_�                       D    ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/\�     �               D                    "zcash": nanopool_hashrate("zec", self.address)}5�_�                       E    ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/]     �               E                    "monero": nanopool_hashrate("xmr", self.address)}5�_�                       D    ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/]     �               D                    "grin": nanopool_hashrate("grin", self.address)}5�_�                        C    ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/]     �               C                    "grin": nanopool_hashrate("grin", self.address)5�_�      !                  C    ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/]    �                  ,from health_monitor import BaseHealthChecker        from utils import CoinmineLogger   =from health_monitor.pool import hashrate as nanopool_hashrate       !logger = CoinmineLogger(__name__)           +class PoolHealthChecker(BaseHealthChecker):   &    def __init__(self, coin, address):           self.coin = coin           self.address = address           def _is_healthy(self):   '        hashrate = self._get_hashrate()           if hashrate:               return True           else:               return False           def _get_hashrate(self):   G        hashrate = {"ethereum": nanopool_hashrate("eth", self.address),   E                    "monero": nanopool_hashrate("xmr", self.address),   D                    "zcash": nanopool_hashrate("zec", self.address),   D                    "grin": nanopool_hashrate("grin", self.address),                       }           pass5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/]     �                       �             5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/]     �                       hashrate[]5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/]     �                        pass5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/]    �                         return hashrate[]5�_�   $   &           %           ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/]~     �               =from health_monitor.pool import hashrate as nanopool_hashrate5�_�   %   '           &           ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/]~     �               5from health_monitor.pool import  as nanopool_hashrate5�_�   &   (           '           ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/]   	 �                  ,from health_monitor import BaseHealthChecker        from utils import CoinmineLogger   2from health_monitor.pool import  nanopool_hashrate       !logger = CoinmineLogger(__name__)           +class PoolHealthChecker(BaseHealthChecker):   &    def __init__(self, coin, address):           self.coin = coin           self.address = address           def _is_healthy(self):   '        hashrate = self._get_hashrate()           if hashrate:               return True           else:               return False           def _get_hashrate(self):           hashrate = {   ?            "ethereum": nanopool_hashrate("eth", self.address),   =            "monero": nanopool_hashrate("xmr", self.address),   <            "zcash": nanopool_hashrate("zec", self.address),   <            "grin": nanopool_hashrate("grin", self.address),   	        }   "        return hashrate[self.coin]5�_�   '   )           (          ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/]�     �                           �             5�_�   (   *           )      /    ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/]�     �               0            logger.info("Pool side hashrate={}")5�_�   )   +           *          ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/^      �             �             5�_�   *   ,           +          ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/^     �               A            logger.info("Pool side hashrate={}".format(hashrate))5�_�   +   -           ,          ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/^   
 �               A            logger.warn("Pool side hashrate={}".format(hashrate))5�_�   ,   .           -          ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/^b    �               A            logger.warn("Pool side hashrate={}".format(hashrate))5�_�   -   /           .      !    ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/_�    �                       �             5�_�   .   0           /      "    ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/`Z    �                 "        return hashrate[self.coin]5�_�   /   1           0          ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/`z     �                        print(hashrate)5�_�   0   2           1      #    ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/a�     �                 .        return hashrate[self.coin]["hashrate"]5�_�   1   3           2      (    ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/a�     �                 3        return hashrate[self.coin].get()"hashrate"]5�_�   2   4           3      2    ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/a�    �                 2        return hashrate[self.coin].get("hashrate"]5�_�   3   5           4           ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/er     �             �             5�_�   4   6           5           ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/ev     �                1from health_monitor.pool import nanopool_hashrate5�_�   5   7           6      1    ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/ev    �               1from health_monitor.pool import nanopool_hashrate5�_�   6   8           7          ����                                                                                                                                                                                                                                                                                                                               2          2       V   2    ]/e|    �               <            "grin": nanopool_hashrate("grin", self.address),5�_�   7   9           8           ����                                                                                                                                                                                                                                                                                                                                                             ]/l
     �                       �             5�_�   8   :           9   
   $    ����                                                                                                                                                                                                                                                                                                                                                             ]/l    �   	            &    def __init__(self, coin, address):5�_�   9   ;           :          ����                                                                                                                                                                                                                                                                                                                                                             ]/{     �               J            logger.warn("Warning! Pool side hashrate={}".format(hashrate))5�_�   :   <           ;      !    ����                                                                                                                                                                                                                                                                                                                                                             ]/{     �               K            logger.error("Warning! Pool side hashrate={}".format(hashrate))5�_�   ;   >           <      !    ����                                                                                                                                                                                                                                                                                                                                                             ]/{    �               J            logger.error("Warnin! Pool side hashrate={}".format(hashrate))5�_�   <   ?   =       >          ����                                                                                                                                                                                                                                                                                                                                                             ]/{2     �                        �             5�_�   >   @           ?          ����                                                                                                                                                                                                                                                                                                                                                             ]/{:     �                            return False5�_�   ?   A           @          ����                                                                                                                                                                                                                                                                                                                                                             ]/{;    �                            return True5�_�   @   B           A      .    ����                                                                                                                                                                                                                                                                                                                                                             ]/�E     �               <            "grin": grinmint_hashrate("grin", self.address),5�_�   A   C           B      2    ����                                                                                                                                                                                                                                                                                                                                                             ]/�I     �               4            "grin": grinmint_hashrate(self.address),5�_�   B   D           C          ����                                                                                                                                                                                                                                                                                                                                                             ]/�N     �                       �             5�_�   C   E           D          ����                                                                                                                                                                                                                                                                                                                                                             ]/�P     �                       self.uuid5�_�   D   F           E          ����                                                                                                                                                                                                                                                                                                                                                             ]/�T     �                       self.uuid = uuid5�_�   E   G           F          ����                                                                                                                                                                                                                                                                                                                                                             ]/�W     �                       self.short_uuid = uuid5�_�   F   H           G   
   %    ����                                                                                                                                                                                                                                                                                                                                                             ]/�Z     �   	            6    def __init__(self, coin, address, remedy_command):5�_�   G   I           H   
   0    ����                                                                                                                                                                                                                                                                                                                                                             ]/�]    �   	            A    def __init__(self, coin, address, short_uuid remedy_command):5�_�   H   J           I      9    ����                                                                                                                                                                                                                                                                                                                                                             ]/��    �               ?            "grin": grinmint_hashrate(self.address, self.uuid),5�_�   I   K           J      =    ����                                                                                                                                                                                                                                                                                                                                                             ]9�     �               ?            "ethereum": nanopool_hashrate("eth", self.address),5�_�   J   L           K      ;    ����                                                                                                                                                                                                                                                                                                                                                             ]9�     �               =            "monero": nanopool_hashrate("xmr", self.address),5�_�   K               L      :    ����                                                                                                                                                                                                                                                                                                                                                             ]9�    �               <            "zcash": nanopool_hashrate("zec", self.address),5�_�   <           >   =          ����                                                                                                                                                                                                                                                                                                                                                             ]/{*     �              5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]/\�     �                       hashrate = {5��