Vim�UnDo� �Eq!�/��Z�;% _����D=�P�}e7�s              !      #       #   #   #    \��    _�                     
        ����                                                                                                                                                                                                                                                                                                                                                             \u�     �   
          5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \u�     �             5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             \u�     �      	         8    config_server_url = environ['MINARY_API_SERVER_URL']5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \u�     �      	         2    _server_url = environ['MINARY_API_SERVER_URL']5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \u�    �               @    ngrok = Ngrok(config_server_url, ngrok_server_url, ssh_port)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \v     �             �             5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                             \v     �                 5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             \v     �                )    # wait for minary api server to be up5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             \v     �                #    # wait for  api server to be up5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             \v     �                    # wait for  server to be up5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \v.    �                *    # wait for ngrok admin server to be up5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \v3    �         !       �              5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \vC     �         !              logger,5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \vH    �         !              logger,5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \vS     �                D    ngrok = Ngrok(minary_api_server_url, ngrok_server_url, ssh_port)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \vU    �              �              5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \v^    �         !              mineos_api_server_url,5�_�                       +    ����                                                                                                                                                                                                                                                                                                                                                             \vd    �         !      E        lambda: CoinmineRequests.get(mineos_api_server_url, 'config')5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \vk    �         !      from utils import SystemHelpers5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \vr   	 �         !              admin_api_url,5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \v�     �         !      A            admin_api_url, 'config/{}'.format(machine_id), token)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \v�     �         !      D            ngrok_server_url, 'config/{}'.format(machine_id), token)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \v�     �         !      ;            ngrok_server_url, ''.format(machine_id), token)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \v�     �         !      <            ngrok_server_url, 't'.format(machine_id), token)5�_�                       *    ����                                                                                                                                                                                                                                                                                                                                                             \v�   
 �         !      F            ngrok_server_url, 'api/tunnels'.format(machine_id), token)5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                             \v�     �         !      >            ngrok_server_url, 'api'.format(machine_id), token)5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                             \v�    �         !      +            ngrok_server_url, 'api', token)5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                             \v�     �         !      %        lambda: CoinmineRequests.get(   $            ngrok_server_url, 'api')5�_�                       &    ����                                                                                                                                                                                                                                                                                                                                                             \v�    �                >        lambda: CoinmineRequests.get( ngrok_server_url, 'api')5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             \v�    �                 5�_�      !                  !    ����                                                                                                                                                                                                                                                                                                                                                             \~�     �               E        lambda: CoinmineRequests.get(minary_api_server_url, 'config')5�_�       "           !      !    ����                                                                                                                                                                                                                                                                                                                                                             \~�    �               =        lambda: CoinmineRequests.get(ngrok_server_url, 'api')5�_�   !   #           "           ����                                                                                                                                                                                                                                                                                                                                                  V        \��     �                        ngrok.logger,           minary_api_server_url,5�_�   "               #           ����                                                                                                                                                                                                                                                                                                                                                V       \��    �                        ngrok.logger,           ngrok_server_url,5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \u�     �      	         '     = environ['MINARY_API_SERVER_URL']5��