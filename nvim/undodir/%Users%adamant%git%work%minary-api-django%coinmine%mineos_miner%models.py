Vim�UnDo� ��?��96�ϴG6�W�ĈZT�"�d�      >    miner = models.ForeignKey(Miner, on_delete=models.CASCADE)                             [��    _�                             ����                                                                                                                                                                                                                                                                                                                                                  V        [��R     �                �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        [��b     �               class Miner(models.Model)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        [��k     �             �             5�_�                            ����                                                                                                                                                                                                                                                                                                                            	           	           V        [��m     �                 5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                  V        [��n     �   	   
          5    created = models.DateTimeField(auto_now_add=True)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        [��o     �      
       �      	       5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                  V        [��o     �   	          5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                  V        [��q     �                 5�_�                 	          ����                                                                                                                                                                                                                                                                                                                                                  V        [��y     �   
            >    miner = models.ForeignKey(Miner, on_delete=models.CASCADE)5�_�   	      
                 ����                                                                                                                                                                                                                                                                                                                                                  V        [��    �      	             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                            
           
           V        [���    �               ?    miner = models.ForeigdnKey(Miner, on_delete=models.CASCADE)5�_�                            ����                                                                                                                                                                                                                                                                                                                            
           
           V        [���    �      	             �      	       5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        [��     �                'from coinmine.miner.models import Miner5�_�                            ����                                                                                                                                                                                                                                                                                                                            
           
           V        [��    �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        [��`    �                   def miner__worker(self):5�_�                          ����                                                                                                                                                                                                                                                                                                                                                  V        [��z     �                   def (self):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        [��     �                        return self.miner.worker5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        [��     �                       return self.miner.5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        [��     �                   def uuid (self):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        [��     �                   def coin__short_name(self):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        [��     �                          return self.miner.worker5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        [��    �                         return self.miner.5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        [��#    �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        [���   	 �               class Miner(models.Model):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        [��   
 �               >    miner = models.ForeignKey(Miner, on_delete=models.CASCADE)5�_�                             ����                                                                                                                                                                                                                                                                                                                                                  V        [��    �               D    miner = models.ForeignKey(MIneOSMiner, on_delete=models.CASCADE)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        [��v     �                5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                  V        [��{     �   
            8    miner = models.Onet(Miner, on_delete=models.CASCADE)5��