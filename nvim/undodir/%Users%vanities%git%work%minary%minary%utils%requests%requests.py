Vim�UnDo� �%WSͶ��X��_G=�@q~c:8�?�Vϐ0   [   =            logger.warn("no json returned with this request")   C                          ^q8>   	 _�                     \       ����                                                                                                                                                                                                                                                                                                                                                             ]q     �   ]            �   ]            �   \            5�_�                    ]        ����                                                                                                                                                                                                                                                                                                                                                             ]q     �   \   ^   d       5�_�                    ]        ����                                                                                                                                                                                                                                                                                                                                                             ]q     �   \   ]          o5�_�                    ]        ����                                                                                                                                                                                                                                                                                                                                                             ]q    �   ]   _   d       �   ]   _   c    5�_�                    ]        ����                                                                                                                                                                                                                                                                                                                            ]           d          V       ]q5    �   \   ]                  @staticmethod       def get_timezone(self):           timezone = ""   <        response = requests.get("https://ipapi.co/timezone")   '        if response.status_code == 200:   0            timezone = response.content.decode()           return timezone5�_�                    V        ����                                                                                                                                                                                                                                                                                                                            V           \          V       ]dm    �   U   V              2    def sanitize_redis_value(miner_status, field):   /        string_result = miner_status.get(field)           if string_result:   "            # if "None", returns 0   7            return ast.literal_eval(string_result) or 0           return 05�_�                            ����                                                                                                                                                                                                                                                                                                                            V           V          V       ]dq    �                
import ast5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                  V        ]��J     �         T    �         T    5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                  V        ]��K     �         Z    5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                  V        ]��M     �         [      <    def post_request(base_url, path, json=None, token=None):5�_�   
                    0    ����                                                                                                                                                                                                                                                                                                                                                  V        ]��U    �         [      J        request = RequestFactory(full_url, "POST", json=json, token=token)5�_�                     C       ����                                                                                                                                                                                                                                                                                                                                                             ^q8=   	 �   B   D   [      =            logger.warn("no json returned with this request")5��