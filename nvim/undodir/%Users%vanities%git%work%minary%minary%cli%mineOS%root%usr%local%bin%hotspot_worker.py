Vim�UnDo� q�*�Y�Eɉ�5�'Dp�"�;�$s�բ�G�Z��      6from wifi_controller import Hotspot, HotspotController                             ]��   
 _�                             ����                                                                                                                                                                                                                                                                                                                                                  V        ]�f     �                    3    device_name = os.getenv("DEVICE_NAME", "wlan0")       netman = NetworkManager   *    hotspot = Hotspot(netman, device_name)   "    hotspot.set_ssid_and_password(   L        os.environ["WIFI_HOTSPOT_SSID"], os.environ["WIFI_HOTSPOT_PASSWORD"]       )    5�_�                      +    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�k     �               8    minary_api_url = os.environ["MINARY_API_SERVER_URL"]5�_�                       2    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�n     �               3    hotspot_controller = HotspotController(hotspot)5�_�                       3    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�o     �               4    hotspot_controller = HotspotController(hotsWIFI)5�_�                          ����                                                                                                                                                                                                                                                                                                                                                  V        ]��     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ]��     �               9    minary_api_url = os.environ["MINARY_WIFI_SERVER_URL"]5�_�                       3    ����                                                                                                                                                                                                                                                                                                                                                  V        ]��     �               9    minary_api_url = os.environ["MINARY_WIFI_SERVER_URL"]5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ]��    �               8    minary_api_url = os.environ["MINARY_API_SERVER_URL"]5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ]��    �               >    minary_api_sever_url = os.environ["MINARY_API_SERVER_URL"]5�_�                       -    ����                                                                                                                                                                                                                                                                                                                                                  V        ]��     �               A    status = CoinmineRequests.get(minary_api_url, "miner_status")5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                  V        ]��    �               -    hotspot_controller = HotspotController(m)5�_�                       @    ����                                                                                                                                                                                                                                                                                                                                                  V        ]��    �             5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                  V        ]��    �                 %    hotspot_controller.update_state()5�_�                           ����                                                                                                                                                                                                                                                                                                                            	                    V   )    ]��     �                try:       import NetworkManager   except Exception:       pass5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V   )    ]��     �                 5�_�                          ����                                                                                                                                                                                                                                                                                                                                                V   )    ]��     �               6from wifi_controller import Hotspot, HotspotController5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V   )    ]��   
 �                  	import os       .from wifi_controller import  HotspotController   +from utils.requests import CoinmineRequests           if __name__ == "__main__":       ?    minary_api_server_url = os.environ["MINARY_API_SERVER_URL"]   A    minary_wifi_server_url = os.environ["MINARY_WIFI_SERVER_URL"]       B    hotspot_controller = HotspotController(minary_wifi_server_url)   H    status = CoinmineRequests.get(minary_api_server_url, "miner_status")   +    hotspot_controller.update_state(status)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V   )    ]��    �              5�_�                          ����                                                                                                                                                                                                                                                                                                                                                  V        ]�s     �                   minary_api_url = 5�_�                       *    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�u     �             �               Q    hotspot_controller = HotspotController(os.environ["MINARY_WIFI_SERVER_URL"]m)5�_�      	                 O    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�v     �               P    hotspot_controller = HotspotController(os.environ["MINARY_WIFI_SERVER_URL"])5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                  V        ]�w     �              5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                      	          V       ]�x    �              5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                V       ]�{     �      
        5�_�                             ����                                                                                                                                                                                                                                                                                                                                                V       ]�|    �              
   	import os       6from wifi_controller import Hotspot, HotspotController   +from utils.requests import CoinmineRequests           if __name__ == "__main__":   P    hotspot_controller = HotspotController(os.environ["MINARY_WIFI_SERVER_URL"])   A    status = CoinmineRequests.get(minary_api_url, "miner_status")   %    hotspot_controller.update_state()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        ]�h     �              5��