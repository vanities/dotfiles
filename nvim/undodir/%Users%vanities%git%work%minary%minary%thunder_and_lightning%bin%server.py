Vim�UnDo� hs��k��C�	.�?*j9�v��W��9   9               if json_obj:                             ]�Q�   
 _�          	                 ����                                                                                                                                                                                                                                                                                                                                                             ]�Q�     �         9                  �         8    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�Q�     �         9      )            json_obj = request.get_json()5�_�                       2    ����                                                                                                                                                                                                                                                                                                                                                             ]�Q�     �         9      D                ambiance_app.config["state"] = {**state, **json_obj}5�_�                       ?    ����                                                                                                                                                                                                                                                                                                                                                             ]�Q�     �         9      H                ambiance_app.config["state"] = {**old_state, **json_obj}5�_�                       ?    ����                                                                                                                                                                                                                                                                                                                                                             ]�Q�     �         9      @                ambiance_app.config["state"] = {**old_state, **}5�_�                      >    ����                                                                                                                                                                                                                                                                                                                                                             ]�Q�     �          9      A                json.dumps({"success": True, "state": json_obj}),5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�Q�   
 �         9                  if json_obj:5�_�                       =    ����                                                                                                                                                                                                                                                                                                                                                             ]�Q�     �          9      J                json.dumps({"success": True, "state": json_obnew_statej}),5�_�       
         	          ����                                                                                                                                                                                                                                                                                                                                                             ]�Q�     �         8      ,    old_state = ambiance_app.config["state"]5�_�   	               
      7    ����                                                                                                                                                                                                                                                                                                                                                             ]�Q�     �         8      B            logger.info("got ambiance state={}".format(old_state))5�_�             	         9    ����                                                                                                                                                                                                                                                                                                                                                             ]�*    �         8      9                ambiance_app.config["state"] = **json_obj5�_�                        1    ����                                                                                                                                                                                                                                                                                                                                                             ]��    �         8      7                ambiance_app.config["state"] = json_obj5�_�                       0    ����                                                                                                                                                                                                                                                                                                                                                             ]�     �         8      <                ambiance_app.config["state"] = { **json_obj}5�_�                       1    ����                                                                                                                                                                                                                                                                                                                                                             ]�     �         8      ;                ambiance_app.config["state"] = {**json_obj}5�_�                      ;    ����                                                                                                                                                                                                                                                                                                                                                             ]�     �         8      :                ambiance_app.config["state"] = {**json_obj5�_�                       2    ����                                                                                                                                                                                                                                                                                                                                                             ]�    �         8      7                ambiance_app.config["state"] = json_obj5�_�                        /    ����                                                                                                                                                                                                                                                                                                                                                             ]�    �         8      9                ambiance_app.config["state"] = **json_obj5�_�                       ;    ����                                                                                                                                                                                                                                                                                                                                                             ]�     �         8      :                ambiance_app.config["state"] = {**json_obj5��