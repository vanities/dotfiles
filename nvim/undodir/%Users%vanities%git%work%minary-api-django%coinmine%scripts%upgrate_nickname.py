Vim�UnDo� yy�X-��c� �/�z%Ա���0��o D�l              ;                       ]�T]    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ]�S    �      	         -nickname = input("enter nickname:", "SAMF.*")5�_�                    
       ����                                                                                                                                                                                                                                                                                                                            
          
          v        ]�S�     �   	                docker_tag=str(nickname)5�_�                           ����                                                                                                                                                                                                                                                                                                                            
          
          v        ]�S�     �      
       �      	       5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                v        ]�S�     �      
         @nickname = input("enter nickname, or samf for empty:", "SAMF.*")5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                v        ]�S�     �      
         ?version = input("enter nickname, or samf for empty:", "SAMF.*")5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                v        ]�S�     �      
         >version = input("enter version, or samf for empty:", "SAMF.*")5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                v        ]�S�     �      
         *version = input("enter version", "SAMF.*")5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                v        ]�S�     �                  �               5�_�      
           	      
    ����                                                                                                                                                                                                                                                                                                                                                v        ]�T      �                 
if version5�_�   	              
   
   
    ����                                                                                                                                                                                                                                                                                                                            
   
       
   
       V   
    ]�T     �   	            Hconfigs = Config.objects.filter(miner__nickname__regex=nickname).update(5�_�   
                         ����                                                                                                                                                                                                                                                                                                                            
                      V        ]�T     �               �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]�T
     �                 >Config.objects.filter(miner__nickname__regex=nickname).update(       docker_tag=str(version)   )5�_�                   
        ����                                                                                                                                                                                                                                                                                                                            
                      V        ]�T&     �   	   
          >Config.objects.filter(miner__nickname__regex=nickname).update(       docker_tag=str(version)   )5�_�                    	        ����                                                                                                                                                                                                                                                                                                                            
           
           V        ]�T'     �   	             �   	          5�_�                    
   ?    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�T=     �   	            ?coin = input("enter short coin name, or no change fro empty, ")5�_�                    	   @    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�T@     �      
         Bversion = input("enter version, or no change for empty", "SAMF.*")5�_�                    	   <    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�TB    �      
         =version = input("enter version, or no change for empty", "S")5�_�                    
   ;    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�TG     �   	            <coin = input("enter short coin name, or no change fro empty)5�_�                    
   5    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�TI    �   	            =coin = input("enter short coin name, or no change fro empty")5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]�TO     �               �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ]�T[     �                if version:   B    Config.objects.filter(miner__nickname__regex=nickname).update(           docker_tag=str(version)       )5�_�                     
        ����                                                                                                                                                                                                                                                                                                                                                  V        ]�T\    �   	   
          =coin = input("enter short coin name, or no change for empty")5�_�                    
        ����                                                                                                                                                                                                                                                                                                                            
          
          V       ]�T#     �   	           5��