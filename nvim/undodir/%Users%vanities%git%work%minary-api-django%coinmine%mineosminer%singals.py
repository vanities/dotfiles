Vim�UnDo� ���Lh�ՙx?\<W_��F�14a�|�ΈNi                                      ]�j�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ]�jo     �                   �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�jv     �             �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�jz     �                �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]�j�     �               !@receiver(post_save, sender=User)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�j�     �               8def post_save_user(sender, instance, created, **kwargs):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             ]�j�     �                    if created:5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]�j�     �                 +        setup_user.delay(instance.username)5�_�      	                 	    ����                                                                                                                                                                                                                                                                                                                                                V       ]�j�     �               �               5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                V       ]�j�     �                 I        publish_config.delay(obj.miner__uuid, ConfigSerializer(obj).data)5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                V       ]�j�     �                 E    publish_config.delay(obj.miner__uuid, ConfigSerializer(obj).data)5�_�   
                    D    ����                                                                                                                                                                                                                                                                                                                                                V       ]�j�     �                 J    publish_config.delay(instance.miner__uuid, ConfigSerializer(obj).data)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       ]�j�     �                '    setup_user.delay(instance.username)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       ]�j�     �             �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]�j�     �                  5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]�j�    �                  .from django.db.models.signals import post_save   .from coinmine.mineosminer.models import Config   =from coinmine.mineosminer.serializers import ConfigSerializer       #@receiver(post_save, sender=Config)   :def post_save_config(sender, instance, created, **kwargs):   O    publish_config.delay(instance.miner__uuid, ConfigSerializer(instance).data)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]�j�     �              �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       ]�j�    �         	    5�_�                             ����                                                                                                                                                                                                                                                                                                                                                V       ]�j�    �         
    �         
    5��