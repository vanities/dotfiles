Vim�UnDo� �͚�^!U�nb�G�u�J���
�\~CC��                                      ^.    _�                     	        ����                                                                                                                                                                                                                                                                                                                                       	           V        ^.
     �      	          if [ ${count} \> 0 ];   then   l    sed -i -E 's/return "([0-9]+)\.([0-9]+)\.([0-9]+)"/return "\1.\2.\3.'$count'"/g' htpclient/initialize.py   fi;5�_�                    
        ����                                                                                                                                                                                                                                                                                                                            
                      V        ^.    �   	   
          if [ ${count} \> 0 ];   then   m    sed -i -E 's/return "([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)"/return "\1.\2.\3"/g' htpclient/initialize.py   fi;5�_�                            ����                                                                                                                                                                                                                                                                                                                            
           
           V        ^.     �                Jcount=$(git log $(git describe --tags --abbrev=0)..HEAD --oneline | wc -l)5�_�                             ����                                                                                                                                                                                                                                                                                                                            	           	           V        ^.    �                N# write commit count since release into version number when compiling into zip5��