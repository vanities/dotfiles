Vim�UnDo� k���ZK�1^��	�	��H�ѵ����                    D       D   D   D    ]�}�    _�                     	        ����                                                                                                                                                                                                                                                                                                                                                             ]�z     �   	             �   	          5�_�                    
        ����                                                                                                                                                                                                                                                                                                                                                             ]�z    �   	             5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             ]�z6     �   	            dry_run = input("dry run? y/n")5�_�                    
   '    ����                                                                                                                                                                                                                                                                                                                                                             ]�z:    �   	            'dry_run = input("dry run? y/n").lower()5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                             ]�z>     �                   �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�zC     �                   if dry_run == "y"5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]�zL     �             �             5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                V       ]�zP     �   
                A   Config.objects.filter(miner__nickname__regex=nickname).update(�               B    Config.objects.filter(miner__nickname__regex=nickname).update(5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                V       ]�zT     �               Gconfig = Config.objects.filter(miner__nickname__regex=nickname).update(           docker_tag=str(version)5�_�   	              
      ?    ����                                                                                                                                                                                                                                                                                                                                                V       ]�zV     �               _config = Config.objects.filter(miner__nickname__regex=nickname).update( docker_tag=str(version)5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                V       ]�zW     �                    )5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]�zX     �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       ]�z[    �               ?config = Config.objects.filter(miner__nickname__regex=nickname)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]�z\    �   
             c5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]�zd     �                   �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       ]�zo     �                       �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       ]�z     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       ]�z�     �               8        miners.count(), current_version, desired_version5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       ]�z�     �               =    "\nretargeting {} miners from version {} to {}\n".format(5�_�                       *    ����                                                                                                                                                                                                                                                                                                                                                V       ]�z�     �               K    "\nretargeting {} miners with nickname from version {} to {}\n".format(5�_�                       .    ����                                                                                                                                                                                                                                                                                                                                                V       ]�z�     �               N    "\nretargeting {} miners with nickname {} from version {} to {}\n".format(5�_�                       .    ����                                                                                                                                                                                                                                                                                                                                                V       ]�z�     �               J    "\nretargeting {} miners with nickname {}  version {} to {}\n".format(5�_�                       .    ����                                                                                                                                                                                                                                                                                                                                                V       ]�z�     �               B    "\nretargeting {} miners with nickname {}  {} to {}\n".format(5�_�                       .    ����                                                                                                                                                                                                                                                                                                                                                V       ]�z�     �               ?    "\nretargeting {} miners with nickname {}  to {}\n".format(5�_�                       (    ����                                                                                                                                                                                                                                                                                                                                                V       ]�z�     �               9        configs.count(), current_version, desired_version5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                V       ]�z�     �               2        configs.count(), nickname, desired_version5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                V       ]�z�    �               #        configs.count(), nickname, 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V   )    ]�z�     �                     if dry_run == "y":           print("updating ")   B    Config.objects.filter(miner__nickname__regex=nickname).update(           docker_tag=str(version)       )5�_�                       >    ����                                                                                                                                                                                                                                                                                                                                                V   )    ]�z�     �               F        Config.objects.filter(miner__nickname__regex=nickname).update(5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V   )    ]�z�     �                       config.update(   #            docker_tag=str(version)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V   )    ]�z�     �                 .        config.update( docker_tag=str(version)   	        )5�_�      !                  .    ����                                                                                                                                                                                                                                                                                                                                         +       V   )    ]�z�     �                         �               5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                         +       V   )    ]�z�     �               /        config.update( docker_tag=str(version))5�_�   !   #           "      '    ����                                                                                                                                                                                                                                                                                                                                         +       V   )    ]�z�     �               '        config.docker_tag=str(version))5�_�   "   $           #      %    ����                                                                                                                                                                                                                                                                                                                                         +       V   )    ]�z�    �                  import django       django.setup()       .from coinmine.mineosminer.models import Config           @nickname = input("enter nickname, or samf for empty:", "SAMF.*")   8version = input("enter version, or no change for empty")   .dry_run = input("dry run? y/n").lower() or "y"       @configs = Config.objects.filter(miner__nickname__regex=nickname)   print(   >    "\nretargeting {} miners with nickname {} to {}\n".format(   *        configs.count(), nickname, version       )   )       if version:       for config in configs:           if dry_run == "y":               print("updating ")   &        config.docker_tag=str(version)           config.save()5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                                         +       V   )    ]�z�     �                           print("updating ")5�_�   $   &           %      $    ����                                                                                                                                                                                                                                                                                                                                         +       V   )    ]�z�     �               %            print("updating uuid={}")5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                                         +       V   )    ]�z�     �               ?            print("updating uuid={}".format(config.miner.uuid))5�_�   &   (           '      8    ����                                                                                                                                                                                                                                                                                                                                         +       V   )    ]�z�     �               K            print("updating nickname={} uuid={}".format(config.miner.uuid))5�_�   '   )           (      H    ����                                                                                                                                                                                                                                                                                                                                         +       V   )    ]�z�    �                  import django       django.setup()       .from coinmine.mineosminer.models import Config           @nickname = input("enter nickname, or samf for empty:", "SAMF.*")   8version = input("enter version, or no change for empty")   .dry_run = input("dry run? y/n").lower() or "y"       @configs = Config.objects.filter(miner__nickname__regex=nickname)   print(   >    "\nretargeting {} miners with nickname {} to {}\n".format(   *        configs.count(), nickname, version       )   )       if version:       for config in configs:           if dry_run == "y":   \            print("updating nickname={} uuid={}".format(config.nickname, config.miner.uuid))   (        config.docker_tag = str(version)           config.save()5�_�   (   *           )           ����                                                                                                                                                                                                                                                                                                                                                V       ]�z�     �                 (        config.docker_tag = str(version)           config.save()5�_�   )   +           *          ����                                                                                                                                                                                                                                                                                                                                                V       ]�z�     �                            print(   6                "updating nickname={} uuid={}".format(   6                    config.nickname, config.miner.uuid                   )               )5�_�   *   ,           +          ����                                                                                                                                                                                                                                                                                                                                                V       ]�z�     �             �             5�_�   +   -           ,           ����                                                                                                                                                                                                                                                                                                                                                V       ]�z�     �                           print(   6                "updating nickname={} uuid={}".format(   6                    config.nickname, config.miner.uuid                   )               )5�_�   ,   .           -           ����                                                                                                                                                                                                                                                                                                                                                V       ]�{     �                print(   >    "\nretargeting {} miners with nickname {} to {}\n".format(   *        configs.count(), nickname, version       )   )5�_�   -   /           .           ����                                                                                                                                                                                                                                                                                                                                                V       ]�{     �             �             5�_�   .   0           /           ����                                                                                                                                                                                                                                                                                                                                                  V        ]�{     �               print(   >    "\nretargeting {} miners with nickname {} to {}\n".format(   *        configs.count(), nickname, version       )   )5�_�   /   1           0          ����                                                                                                                                                                                                                                                                                                                                                  V        ]�{     �                             �               5�_�   0   2           1          ����                                                                                                                                                                                                                                                                                                                                                  V        ]�{     �                     print()"5�_�   1   3           2      
    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�{     �                     print()5�_�   2   4           3   	       ����                                                                                                                                                                                                                                                                                                                                                  V        ]�{"     �      
         8version = input("enter version, or no change for empty")5�_�   3   5           4   	       ����                                                                                                                                                                                                                                                                                                                                                  V        ]�{#     �      
         version = input("enter version)5�_�   4   6           5   	       ����                                                                                                                                                                                                                                                                                                                                                  V        ]�{'    �                  import django       django.setup()       .from coinmine.mineosminer.models import Config           @nickname = input("enter nickname, or samf for empty:", "SAMF.*")   !version = input("enter version:")   .dry_run = input("dry run? y/n").lower() or "y"       @configs = Config.objects.filter(miner__nickname__regex=nickname)       if version:   
    print(   B        "\nretargeting {} miners with nickname {} to {}\n".format(   .            configs.count(), nickname, version   	        )       )       for config in configs:           print(   2            "updating nickname={} uuid={}".format(   2                config.nickname, config.miner.uuid               )   	        )           if dry_run == "y":   ,            config.docker_tag = str(version)               config.save()   else:   )    print("No version supplied, exiting")5�_�   5   7           6      5    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�{.     �      	         @nickname = input("enter nickname, or samf for empty:", "SAMF.*")5�_�   6   8           7      6    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�{/     �      	         Anickname = input("enter nickname, or samf for empty:"), "SAMF.*")5�_�   7   9           8      <    ����                                                                                                                                                                                                                                                                                                                                                  V        ]�{1   	 �      	         Enickname = input("enter nickname, or samf for empty:") or , "SAMF.*")5�_�   8   :           9           ����                                                                                                                                                                                                                                                                                                                                                V       ]�{�     �               ,            config.docker_tag = str(version)               config.save()5�_�   9   ;           :          ����                                                                                                                                                                                                                                                                                                                                                V       ]�{�    �                           �             5�_�   :   <           ;          ����                                                                                                                                                                                                                                                                                                                               (                 v       ]�}i     �                       if dry_run == "y":5�_�   ;   =           <           ����                                                                                                                                                                                                                                                                                                                                                V       ]�}k     �                (        config.docker_tag = str(version)           config.save()5�_�   <   >           =           ����                                                                                                                                                                                                                                                                                                                                                V       ]�}k     �             �             5�_�   =   ?           >           ����                                                                                                                                                                                                                                                                                                                                                V       ]�}m     �               (        config.docker_tag = str(version)           config.save()5�_�   >   @           ?          ����                                                                                                                                                                                                                                                                                                                                                V       ]�}n     �                            continue5�_�   ?   A           @           ����                                                                                                                                                                                                                                                                                                                                                V       ]�}p     �                           �             5�_�   @   B           A          ����                                                                                                                                                                                                                                                                                                                                                V       ]�}{     �                            print("r")5�_�   A   C           B           ����                                                                                                                                                                                                                                                                                                                                                V       ]�}�     �                        else:5�_�   B   D           C           ����                                                                                                                                                                                                                                                                                                                                                V       ]�}�     �                �             5�_�   C               D          ����                                                                                                                                                                                                                                                                                                                                                V       ]�}�    �               if dry_run != "n"5��