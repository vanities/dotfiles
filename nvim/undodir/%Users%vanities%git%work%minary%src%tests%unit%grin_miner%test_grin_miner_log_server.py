Vim�UnDo�  �БL���"B�����J+\��vsv���H�      M        grin_miner_log_path = "/app/src/tests/unit/grin_miner/grin-miner.log"      #                       \ȡ�    _�                            ����                                                                                                                                                                                                                                                                                                                                                             \Ƞ�    �                  from unittest import TestCase       'from grin_miner.log import GrinMinerLog   /from grin_miner.server import grin_miner_server           $class TestGrinMinerServer(TestCase):       def setUp(self):   !        # connect to api to redis   @        self.grin_miner_server = grin_miner_server.test_client()   G        grin_miner_log_path = '/minary_miners/src/tests/grin-miner.log'       B        grin_miner_server.config['grin_miner_log'] = GrinMinerLog(                grin_miner_log_path)           def test_get_stats(self):   7        response = self.grin_miner_server.get('/stats')   I        self.assertEqual({'results': {'graph_rate': 1.6672557414652411}},   -                         response.get_json())5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \ȡ     �   
            G        grin_miner_log_path = "/minary_miners/src/tests/grin-miner.log"5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                             \ȡ�     �   
            K        grin_miner_log_path = "/src/minary_miners/src/tests/grin-miner.log"5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                             \ȡ�     �   
            K        grin_miner_log_path = "/app/minary_miners/src/tests/grin-miner.log"5�_�                       %    ����                                                                                                                                                                                                                                                                                                                                                             \ȡ�     �   
            >        grin_miner_log_path = "/app//src/tests/grin-miner.log"5�_�                       .    ����                                                                                                                                                                                                                                                                                                                                                             \ȡ�     �   
            =        grin_miner_log_path = "/app/src/tests/grin-miner.log"5�_�                       3    ����                                                                                                                                                                                                                                                                                                                                                             \ȡ�    �   
            B        grin_miner_log_path = "/app/src/tests/unit/grin-miner.log"5�_�      
                 6    ����                                                                                                                                                                                                                                                                                                                                                             \ȡ�     �               7        response = self.grin_miner_server.get("/stats")           self.assertEqual(5�_�         	       
      6    ����                                                                                                                                                                                                                                                                                                                                                             \ȡ�    �                  from unittest import TestCase       'from grin_miner.log import GrinMinerLog   /from grin_miner.server import grin_miner_server           $class TestGrinMinerServer(TestCase):       def setUp(self):   !        # connect to api to redis   @        self.grin_miner_server = grin_miner_server.test_client()   M        grin_miner_log_path = "/app/src/tests/unit/grin_miner/grin-miner.log"       V        grin_miner_server.config["grin_miner_log"] = GrinMinerLog(grin_miner_log_path)           def test_get_stats(self):   ;            response = self.grin_miner_server.get("/stats")               self.assertEqual(   P            {"results": {"graph_rate": 1.6672557414652411}}, response.get_json()   	        )5�_�   
                     #    ����                                                                                                                                                                                                                                                                                                                                                             \ȡ�    �   
            M        grin_miner_log_path = "/app/src/tests/unit/grin_miner/grin-miner.log"5�_�              
   	          ����                                                                                                                                                                                                                                                                                                                                                             \ȡ�     �               :            esponse = self.grin_miner_server.get("/stats")5��