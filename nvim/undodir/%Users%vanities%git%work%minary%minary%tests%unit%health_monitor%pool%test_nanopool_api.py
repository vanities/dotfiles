Vim�UnDo� �� 5}>���AM�����A.��"'�����7�   
   N        self.assertEqual(gw.to_dict(), {"hashrate": nanopool_hashrate_dict()})   
   4      <       <   <   <    ]/d�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ]/T*     �                   �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]/T+     �         	    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]/T,    �               
           .class EstimatedEarningsGatewayTests(TestCase):       def test_to_dict(self):   &        gw = EstimatedEarningsGateway(   R            MockResponse({"status": True, "data": estimated_earnings_dict()}, 200)   	        )           self.assertEqual(   K            gw.to_dict(), {"estimated_earnings": estimated_earnings_dict()}   	        )5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]/T.     �                .class EstimatedEarningsGatewayTests(TestCase):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]/T/    �                class GatewayTests(TestCase):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]/Tk     �               &        gw = EstimatedEarningsGateway(5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]/Tm     �                       gw = Gateway(5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             ]/Tp     �          	       �              5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                             ]/Tq     �          
       5�_�   	              
      .    ����                                                                                                                                                                                                                                                                                                                                                             ]/Tx    �               
   /from health_monitor.pool import HashrateGateway       %class HashrateGatewayTests(TestCase):       def test_to_dict(self):           gw = HashrateGateway(   R            MockResponse({"status": True, "data": estimated_earnings_dict()}, 200)   	        )           self.assertEqual(   K            gw.to_dict(), {"estimated_earnings": estimated_earnings_dict()}   	        )5�_�   
                    .    ����                                                                                                                                                                                                                                                                                                                                                             ]/T{     �                 �              5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]/T�    �                from unittest import TestCasxe5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]/T�     �             �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]/T�    �                  from unittest import TestCase   /from health_monitor.pool import HashrateGateway       class MockResponse:   /    def __init__(self, json_data, status_code):   "        self.json_data = json_data   &        self.status_code = status_code           def json(self):           return self.json_data       %class HashrateGatewayTests(TestCase):       def test_to_dict(self):           gw = HashrateGateway(   R            MockResponse({"status": True, "data": estimated_earnings_dict()}, 200)   	        )           self.assertEqual(   K            gw.to_dict(), {"estimated_earnings": estimated_earnings_dict()}   	        )5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]/T�     �                   �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]/T�    �                  from unittest import TestCase   /from health_monitor.pool import HashrateGateway           class MockResponse:   /    def __init__(self, json_data, status_code):   "        self.json_data = json_data   &        self.status_code = status_code           def json(self):           return self.json_data   hashrate_dict = {       "status": true,       "data": 306   }           %class HashrateGatewayTests(TestCase):       def test_to_dict(self):           gw = HashrateGateway(   R            MockResponse({"status": True, "data": estimated_earnings_dict()}, 200)   	        )           self.assertEqual(   K            gw.to_dict(), {"estimated_earnings": estimated_earnings_dict()}   	        )5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]/T�    �               -hashrate_dict = {"status": true, "data": 306}5�_�                       2    ����                                                                                                                                                                                                                                                                                                                                                             ]/T�     �               R            MockResponse({"status": True, "data": estimated_earnings_dict()}, 200)5�_�                       2    ����                                                                                                                                                                                                                                                                                                                                                             ]/T�     �               I            MockResponse({"status": True, "data": _earnings_dict()}, 200)5�_�                       2    ����                                                                                                                                                                                                                                                                                                                                                             ]/T�     �               @            MockResponse({"status": True, "data": _dict()}, 200)5�_�                       1    ����                                                                                                                                                                                                                                                                                                                                                             ]/U     �               K            gw.to_dict(), {"estimated_earnings": estimated_earnings_dict()}5�_�                       9    ����                                                                                                                                                                                                                                                                                                                                                             ]/U     �               S            gw.to_dict(), {"estimated_earnings": hashrateestimated_earnings_dict()}5�_�                       9    ����                                                                                                                                                                                                                                                                                                                                                             ]/U     �               J            gw.to_dict(), {"estimated_earnings": hashrate_earnings_dict()}5�_�                       9    ����                                                                                                                                                                                                                                                                                                                                                             ]/U   	 �                  from unittest import TestCase   /from health_monitor.pool import HashrateGateway           class MockResponse:   /    def __init__(self, json_data, status_code):   "        self.json_data = json_data   &        self.status_code = status_code           def json(self):           return self.json_data           -hashrate_dict = {"status": True, "data": 306}           %class HashrateGatewayTests(TestCase):       def test_to_dict(self):           gw = HashrateGateway(   H            MockResponse({"status": True, "data": hashrate_dict()}, 200)   	        )           self.assertEqual(   A            gw.to_dict(), {"estimated_earnings": hashrate_dict()}   	        )5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]/U�     �               -hashrate_dict = {"status": True, "data": 306}5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]/U�     �               1def hashrate_dict = {"status": True, "data": 306}5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]/U�     �               3def hashrate_dict() = {"status": True, "data": 306}5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]/U�   
 �                  from unittest import TestCase   /from health_monitor.pool import HashrateGateway           class MockResponse:   /    def __init__(self, json_data, status_code):   "        self.json_data = json_data   &        self.status_code = status_code           def json(self):           return self.json_data           9def hashrate_dict(): return {"status": True, "data": 306}           %class HashrateGatewayTests(TestCase):       def test_to_dict(self):           gw = HashrateGateway(   H            MockResponse({"status": True, "data": hashrate_dict()}, 200)   	        )   O        self.assertEqual(gw.to_dict(), {"estimated_earnings": hashrate_dict()})5�_�                       ;    ����                                                                                                                                                                                                                                                                                                                                                             ]/U�    �                 O        self.assertEqual(gw.to_dict(), {"estimated_earnings": hashrate_dict()})5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]/X6     �                class MockResponse:   /    def __init__(self, json_data, status_code):   "        self.json_data = json_data   &        self.status_code = status_code           def json(self):           return self.json_data    5�_�                             ����                                                                                                                                                                                                                                                                                                                                                  V        ]/X7     �                 5�_�      !                       ����                                                                                                                                                                                                                                                                                                                                                  V        ]/X8     �                �             5�_�       "           !           ����                                                                                                                                                                                                                                                                                                                                                  V        ]/X;     �                f5�_�   !   #           "           ����                                                                                                                                                                                                                                                                                                                                                  V        ]/X>     �             �             5�_�   "   &           #           ����                                                                                                                                                                                                                                                                                                                                                  V        ]/X>    �             5�_�   #   '   %       &          ����                                                                                                                                                                                                                                                                                                                                                  V        ]/Y�     �   
            %class HashrateGatewayTests(TestCase):5�_�   &   (           '          ����                                                                                                                                                                                                                                                                                                                                                  V        ]/Y�    �   
            )class TestHashrateGatewayTests(TestCase):5�_�   '   )           (          ����                                                                                                                                                                                                                                                                                                                                                V       ]/Z     �                def hashrate_dict():   (    return {"status": True, "data": 306}5�_�   (   *           )           ����                                                                                                                                                                                                                                                                                                                                                V       ]/Z    �                  from unittest import TestCase       #from tests.unit import MockResponse   /from health_monitor.pool import HashrateGateway                   $class TestHashrateGateway(TestCase):       def test_to_dict(self):           gw = HashrateGateway(   H            MockResponse({"status": True, "data": hashrate_dict()}, 200)   	        )   E        self.assertEqual(gw.to_dict(), {"hashrate": hashrate_dict()})5�_�   )   +           *   
   2    ����                                                                                                                                                                                                                                                                                                                                                V       ]/Z8    �   	            H            MockResponse({"status": True, "data": hashrate_dict()}, 200)5�_�   *   ,           +      4    ����                                                                                                                                                                                                                                                                                                                                                V       ]/Z=    �                 E        self.assertEqual(gw.to_dict(), {"hashrate": hashrate_dict()})5�_�   +   -           ,      L    ����                                                                                                                                                                                                                                                                                                                                                V       ]/Zf     �                 N        self.assertEqual(gw.to_dict(), {"hashrate": nanopool_hashrate_dict()})5�_�   ,   .           -   
   J    ����                                                                                                                                                                                                                                                                                                                                                V       ]/Zh    �   	            Q            MockResponse({"status": True, "data": nanopool_hashrate_dict()}, 200)5�_�   -   /           .           ����                                                                                                                                                                                                                                                                                                                                                V       ]/Z�     �             �             5�_�   .   0           /      H    ����                                                                                                                                                                                                                                                                                                                                                V       ]/Z�     �   
            O            MockResponse({"status": True, "data": nanopool_hashrate_dict}, 200)5�_�   /   1           0      J    ����                                                                                                                                                                                                                                                                                                                                                V       ]/Z�    �                 L        self.assertEqual(gw.to_dict(), {"hashrate": nanopool_hashrate_dict})5�_�   0   2           1          ����                                                                                                                                                                                                                                                                                                                                                  V        ]/d     �   
            Q            MockResponse({"status": True, "data": nanopool_hashrate_dict()}, 200)�             5�_�   1   3           2      6    ����                                                                                                                                                                                                                                                                                                                                                  V        ]/d     �   
            n            MockResponse({"status": True, "data": 306}{"status": True, "data": nanopool_hashrate_dict()}, 200)5�_�   2   4           3      6    ����                                                                                                                                                                                                                                                                                                                                                  V        ]/d     �   
            _            MockResponse({"status": True, "data": 306}, "data": nanopool_hashrate_dict()}, 200)5�_�   3   5           4      6    ����                                                                                                                                                                                                                                                                                                                                                  V        ]/d    �                  from unittest import TestCase       #from tests.unit import MockResponse   <from tests.unit.health_monitor import nanopool_hashrate_dict   /from health_monitor.pool import HashrateGateway           $class TestHashrateGateway(TestCase):       def test_to_dict(self):           gw = HashrateGateway(   <            MockResponse({"status": True, "data": 306}, 200)   	        )   N        self.assertEqual(gw.to_dict(), {"hashrate": nanopool_hashrate_dict()})5�_�   4   6           5           ����                                                                                                                                                                                                                                                                                                                                                  V        ]/db    �                <from tests.unit.health_monitor import nanopool_hashrate_dict5�_�   5   7           6   
   4    ����                                                                                                                                                                                                                                                                                                                                                  V        ]/d�     �   	              N        self.assertEqual(gw.to_dict(), {"hashrate": nanopool_hashrate_dict()})5�_�   6   8           7   
   5    ����                                                                                                                                                                                                                                                                                                                                                  V        ]/d�     �   	              6        self.assertEqual(gw.to_dict(), {"hashrate": })5�_�   7   9           8   
   4    ����                                                                                                                                                                                                                                                                                                                                                  V        ]/d�     �   	              5        self.assertEqual(gw.to_dict(), {"hashrate": )5�_�   8   :           9   
   7    ����                                                                                                                                                                                                                                                                                                                                                  V        ]/d�     �   	              8        self.assertEqual(gw.to_dict(), {"hashrate": 305)5�_�   9   ;           :   
   6    ����                                                                                                                                                                                                                                                                                                                                                  V        ]/d�    �   	              7        self.assertEqual(gw.to_dict(), {"hashrate": 30)5�_�   :   <           ;   
   8    ����                                                                                                                                                                                                                                                                                                                                                  V        ]/d�    �   	              8        self.assertEqual(gw.to_dict(), {"hashrate": 306)5�_�   ;               <   
   8    ����                                                                                                                                                                                                                                                                                                                                                  V        ]/d�    �   	              9        self.assertEqual(gw.to_dict(), {"hashrate": 306))5�_�   #       $   &   %          ����                                                                                                                                                                                                                                                                                                                                                  V        ]/X�     �                           5�_�   #           %   $          ����                                                                                                                                                                                                                                                                                                                                                  V        ]/X�     �                           )}, 200)5��