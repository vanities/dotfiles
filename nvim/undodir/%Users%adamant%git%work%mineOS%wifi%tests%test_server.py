Vim�UnDo� ���s��Yrs�"��\�U<��jw+�U��e��      :                "uuid": "f1780b81987a48ab9dac3ea3be67cfba"                             [���   	 _�                             ����                                                                                                                                                                                                                                                                                                                                                             [���     �                   �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             [���     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [���     �               )        client = config_app.test_client()5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             [��     �              �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [��    �                from config import config_app5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                             [��	     �               6class TestConfigServerIntegrations(unittest.TestCase):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [��$    �             �             5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                             [��&     �                from unittest import TestCase5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                             [��'     �              �             5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                                             [��(    �             5�_�   
                 	   2    ����                                                                                                                                                                                                                                                                                                                                                             [��1     �      
         L        config_app.config['machine_id_path'] = os.environ['MACHINE_ID_PATH']5�_�                    	   0    ����                                                                                                                                                                                                                                                                                                                                                             [��2    �      
         J        config_app.config['machine_id_path'] = oenviron['MACHINE_ID_PATH']5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [��8    �              �             5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             [��@    �   	            I        config_app.config['machine_id_path'] = environ['MACHINE_ID_PATH']5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [��    �               from config import wifi_app5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             [��     �                  from os import environ   from unittest import TestCase       from wifi import wifi_app           -class TestConfigServerIntegrations(TestCase):       def test_get_uuid(self):   '        client = wifi_app.test_client()   G        wifi_app.config['machine_id_path'] = environ['MACHINE_ID_PATH']   &        response = client.get('/uuid')               self.assertEqual(               {   :                "uuid": "f1780b81987a48ab9dac3ea3be67cfba"               },                response.get_json(),   	        )5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                             [��    �               from wifi import wifi_app5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [���     �               :                "uuid": "f1780b81987a48ab9dac3ea3be67cfba"5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             [���   	 �                               "uuid": ""5��