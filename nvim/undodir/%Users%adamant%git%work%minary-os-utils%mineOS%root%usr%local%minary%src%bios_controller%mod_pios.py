Vim�UnDo� �ɓ%���ۣu�r��U�����}���]ݱ�      4        command = "/usr/local/minary/bin/amdmeminfo"      )      3       3   3   3    [���    _�                             ����                                                                                                                                                                                                                                                                                                                                                             [���     �                   5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [���     �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             [���     �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             [��    �               �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             [��&     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             [��'     �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             [��)     �                  �               5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             [��<     �                 class BiosMod())5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             [��@     �               5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                                             [��I     �                  5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             [��Z     �                     def __init__(self)5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             [���     �               �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [���     �         	      E        command = "dmidecode -t 4 | grep ID | sed 's/.*ID://;s/ //g'"5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [���     �         	              command = ""5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [���     �         	              command = "amdmeminfo"5�_�                            ����                                                                                                                                                                                                                                                                                                                                      	          V       [���     �                4        command = "/usr/local/minary/bin/amdmeminfo"   @        output = subprocess.check_output(['bash','-c', command])   *        return output.decode().strip('\n')5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       [���     �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       [���     �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       [���     �               5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                V       [���     �                         5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                V       [���     �                     def    5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                V       [��     �                     def get_info()    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       [��     �         
              �         	    5�_�                    
        ����                                                                                                                                                                                                                                                                                                                            
          
          V       [��     �   	                      def get_info():    5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                      	           v       [��      �   
            5�_�                            ����                                                                                                                                                                                                                                                                                                                                      	           v       [��#     �               �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                      	           v       [��&     �   
              5�_�                           ����                                                                                                                                                                                                                                                                                                                                      	           v       [��/     �               �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                      	           v       [��1     �               �               5�_�                             ����                                                                                                                                                                                                                                                                                                                                      	           v       [��4     �                  5�_�      !                       ����                                                                                                                                                                                                                                                                                                                                      	           v       [��:     �                  5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                      	           v       [��O     �                     def find_memory_type()5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                                      	           v       [��S     �               5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                                      	           v       [��j     �                   def find_memory_type():5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                                      	           v       [��     �                       �             5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                                      	           v       [���     �                       if 'Samsung' in info:'5�_�   %   '           &           ����                                                                                                                                                                                                                                                                                                                                                V       [���     �             �             5�_�   &   (           '          ����                                                                                                                                                                                                                                                                                                                                                V       [���     �                       if 'Samsung' in info:5�_�   '   )           (          ����                                                                                                                                                                                                                                                                                                                                                V       [���     �                       elif 'Samsung' in info:5�_�   (   *           )          ����                                                                                                                                                                                                                                                                                                                                                V       [���     �                       elif '' in info:5�_�   )   +           *          ����                                                                                                                                                                                                                                                                                                                                                V       [���     �                           return 'Samsung'5�_�   *   ,           +          ����                                                                                                                                                                                                                                                                                                                                                V       [���    �               !            return 'HynixSamsung'5�_�   +   -           ,   	        ����                                                                                                                                                                                                                                                                                                                                                V       [��f     �      	           5�_�   ,   .           -           ����                                                                                                                                                                                                                                                                                                                                                V       [��o     �                         �               5�_�   -   /           .          ����                                                                                                                                                                                                                                                                                                                                                V       [���     �                     def mod_bios(mem)5�_�   .   1           /           ����                                                                                                                                                                                                                                                                                                                            
   	          	       V   	    [���     �             �             5�_�   /   2   0       1      )    ����                                                                                                                                                                                                                                                                                                                            
   	          	       V   	    [���     �               4        command = "/usr/local/minary/bin/amdmeminfo"5�_�   1   3           2      )    ����                                                                                                                                                                                                                                                                                                                            
   	          	       V   	    [���     �               *        command = "/usr/local/minary/bin/"5�_�   2               3      1    ����                                                                                                                                                                                                                                                                                                                            
   	          	       V   	    [���    �               2        command = "/usr/local/minary/bin/atiflash"5�_�   /           1   0          ����                                                                                                                                                                                                                                                                                                                            
   	          	       V   	    [���     �              5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             [��]     �                        �                 �                    5��