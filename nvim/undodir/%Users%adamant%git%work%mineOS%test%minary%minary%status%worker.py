Vim�UnDo� �=H+���b�AZ��~�I8���@�yR�<	Q   9           @                       \��    _�                        !    ����                                                                                                                                                                                                                                                                                                                                                             \~�     �         <      >        lambda: CoinmineRequests.get(minary_api_url, 'config')5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \%     �         <    �         <    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \'     �         C    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V       \.     �                ;    config = CoinmineRequests.get(minary_api_url, 'config')   )    admin_api_url = config.get('api_url')    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V       \0    �         A    �         A    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                   V       \8    �                 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V       \U    �          C      L    machine_uuid = SystemHelpers.get_uuid(environ['MINARY_MACHINE_ID_PATH'])5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                 V       \[     �                J    machine_id = SystemHelpers.get_uuid(environ['MINARY_MACHINE_ID_PATH'])5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                 V       \]    �         B    �         B    5�_�   	              
            ����                                                                                                                                                                                                                                                                                                                                                   V       \`    �                  5�_�   
                    %    ����                                                                                                                                                                                                                                                                                                                                                   V       \�    �         B      A            admin_api_url, 'config/{}'.format(machine_id), token)5�_�                       %    ����                                                                                                                                                                                                                                                                                                                                                   V       \�     �         B      @            admin_api_url, 'sessions'.format(machine_id), token)5�_�                       %    ����                                                                                                                                                                                                                                                                                                                                                   V       \�    �         B      .            admin_api_url, 'sessions'), token)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                   V       \�     �         B      &            admin_api_url, 'sessions')5�_�                           ����                                                                                                                                                                                                                                                                                                                                                   V       \�    �         B                  )5�_�                           ����                                                                                                                                                                                                                                                                                                                                                   V       \�?     �         B      *        lambda: CoinmineRequests.test_get(   $            'http://www.google.com')5�_�                       +    ����                                                                                                                                                                                                                                                                                                                                                 V       \�@   	 �         A      C        lambda: CoinmineRequests.test_get( 'http://www.google.com')5�_�                            ����                                                                                                                                                                                                                                                                                                                                                 V       \�D   
 �         A      (    # wait for admin api server to be up5�_�                       A    ����                                                                                                                                                                                                                                                                                                                                                             \��    �         A      B        lambda: CoinmineRequests.test_get('http://www.google.com')5�_�                    ;       ����                                                                                                                                                                                                                                                                                                                                                             \��    �   :   <   A              machine_uuid,5�_�                       @    ����                                                                                                                                                                                                                                                                                                                                                             \�%    �         A      F        lambda: CoinmineRequests.test_get('http://www.google.com', '')5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \�Z     �                        admin_api_url,5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \�\    �                        minary_api_url,5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \�h     �                        logger,5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \�k    �                        logger,5�_�                    &        ����                                                                                                                                                                                                                                                                                                                            &          '          V       \��    �   %   &                      logger,               claymore_socket,5�_�                     *        ����                                                                                                                                                                                                                                                                                                                            *          +          V       \��    �   )   *                      logger,               claymore_socket,5��