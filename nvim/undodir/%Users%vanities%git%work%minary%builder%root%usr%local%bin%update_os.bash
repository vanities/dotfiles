Vim�UnDo� ����Ӑ�.\��63E�)��n%���֣��   N   ?  printf "${GREEN}Pulled${NC} latest $VERSION docker image\n\n"      '      1       1   1   1    ^ +7    _�                             ����                                                                                                                                                                                                                                                                                                                                                             ^ )    �                 �              5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^ )�     �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^ )�     �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^ )�     �               �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^ )�     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^ )�     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ^ )�     �      -       �             5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                             ^ )�     �      0   0    �         0    5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                             ^ )�     �         ^    5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                                             ^ )�     �                #!/bin/bash5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                             ^ )�    �                 5�_�                   .        ����                                                                                                                                                                                                                                                                                                                                                  V        ^ *     �   -   4   ]    �   .   /   ]    5�_�                    .        ����                                                                                                                                                                                                                                                                                                                                                  V        ^ *     �   .   0   c    5�_�                    .        ����                                                                                                                                                                                                                                                                                                                                                  V        ^ *     �   -   /   d       5�_�                    5        ����                                                                                                                                                                                                                                                                                                                                                  V        ^ *     �   4   5          }5�_�                    1        ����                                                                                                                                                                                                                                                                                                                                                  V        ^ *     �   0   1          O  if (( $(awk 'BEGIN {print ("'$CURRENT_MINOR_VERSION'" < "'8.14'")}') )); then5�_�                    1        ����                                                                                                                                                                                                                                                                                                                            1          1          V       ^ *     �   0   2   b      z     sudo -u builduser bash -c 'cd ~ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -sri --noconfirm'5�_�                    1        ����                                                                                                                                                                                                                                                                                                                            1          1          V       ^ *      �   0   2   b      y    sudo -u builduser bash -c 'cd ~ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -sri --noconfirm'5�_�                    1        ����                                                                                                                                                                                                                                                                                                                            1          1          V       ^ *!     �   0   2   b      w  sudo -u builduser bash -c 'cd ~ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -sri --noconfirm'5�_�                    0       ����                                                                                                                                                                                                                                                                                                                            1          1          V       ^ *"     �   /   1   b      install_yay() {   usudo -u builduser bash -c 'cd ~ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -sri --noconfirm'5�_�                    0       ����                                                                                                                                                                                                                                                                                                                            0          0          V       ^ *#     �   /   2   a      �install_yay() { sudo -u builduser bash -c 'cd ~ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -sri --noconfirm'5�_�                    1        ����                                                                                                                                                                                                                                                                                                                            1           1           V        ^ *%     �   0   2   b      usudo -u builduser bash -c 'cd ~ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -sri --noconfirm'5�_�                    2        ����                                                                                                                                                                                                                                                                                                                            1           1           V        ^ *'     �   1   2            fi5�_�                    0        ����                                                                                                                                                                                                                                                                                                                            1           1           V        ^ *'     �   /   1   a      install_yay() {   w  sudo -u builduser bash -c 'cd ~ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -sri --noconfirm'5�_�                    0       ����                                                                                                                                                                                                                                                                                                                            0          0          V        ^ *)     �   /   1   `      �install_yay() { sudo -u builduser bash -c 'cd ~ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -sri --noconfirm'5�_�                    0       ����                                                                                                                                                                                                                                                                                                                            0          0          V        ^ **     �   /   2   `      �install_yay() {sudo -u builduser bash -c 'cd ~ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -sri --noconfirm'5�_�                    1        ����                                                                                                                                                                                                                                                                                                                            0          0          V        ^ *+    �   0   2   a      usudo -u builduser bash -c 'cd ~ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -sri --noconfirm'5�_�                    1   %    ����                                                                                                                                                                                                                                                                                                                            0          0          V        ^ *0     �   0   3   a      w  sudo -u builduser bash -c 'cd ~ && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -sri --noconfirm'5�_�                    2   =    ����                                                                                                                                                                                                                                                                                                                            0          0          V        ^ *6    �   1   4   b      V    git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -sri --noconfirm'5�_�                             ����                                                                                                                                                                                                                                                                                                                                                  V        ^ *?    �                !BLACK='\033[0;30m'        # Black   RED='\033[0;31m'          # Red5�_�      !                       ����                                                                                                                                                                                                                                                                                                                                       	           V        ^ *C    �                "PURPLE='\033[0;35m'       # Purple    CYAN='\033[0;36m'         # Cyan   !WHITE='\033[0;37m'        # White5�_�       "           !           ����                                                                                                                                                                                                                                                                                                                            	                      V        ^ *J    �                %ROOT_DIR='/app/cli/mineOS/.host_root'   &MINARY_API_URL='http://localhost:5002'5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                                                  V        ^ *�     �         \    5�_�   "   $           #           ����                                                                                                                                                                                                                                                                                                                                                  V        ^ *�     �         ^       �         ]    5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                                                  V        ^ *�     �                .  printf "${YELLOW}Logging${NC} into docker\n"5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                                                  V        ^ *�     �         ]    �         ]    5�_�   %   '           &           ����                                                                                                                                                                                                                                                                                                                                                V       ^ *�     �         ^       docker login5�_�   &   (           '           ����                                                                                                                                                                                                                                                                                                                                                V       ^ *�     �                @  DOCKER_AUTH=$(curl -s "$CONFIG_ENDPOINT" | jq -r .docker_auth)     if [ "$DOCKER_AUTH" = "" ];     then   4    printf "No docker_auth setting, using default\n"     else   (    printf "Found docker_auth setting\n"   /    DOCKER=$(echo "$DOCKER_AUTH" | base64 -d -)   1    DOCKER_USER=$(echo "$DOCKER" | cut -d : -f 1)   1    DOCKER_PASS=$(echo "$DOCKER" | cut -d : -f 2)   Q    echo "$DOCKER_PASS" | docker login --username "$DOCKER_USER" --password-stdin     fi5�_�   '   )           (           ����                                                                                                                                                                                                                                                                                                                                                V       ^ *�    �                 5�_�   (   *           )           ����                                                                                                                                                                                                                                                                                                                                       
           V        ^ *�     �                (CONFIG_ENDPOINT='$MINARY_API_URL/config'       GRUB=$(cat /etc/default/grub)5�_�   )   +           *   	        ����                                                                                                                                                                                                                                                                                                                            	                      V        ^ *�   	 �      	          ENVIRONMENT=$2   bCURRENT_VERSION=$(cat /etc/minary-release.yaml  |  grep -oE '(release).*' | sed 's/[^0-9\\.]*//g')   ?CURRENT_MINOR_VERSION=$(echo $CURRENT_VERSION | cut -d . -f 2-)5�_�   *   ,           +   L       ����                                                                                                                                                                                                                                                                                                                            	           	           V        ^ *�   
 �   L               �   L            5�_�   +   -           ,   H        ����                                                                                                                                                                                                                                                                                                                            	           	           V        ^ *�    �   H   J   M    5�_�   ,   .           -           ����                                                                                                                                                                                                                                                                                                                            	           	           V        ^ *�     �      	   N      
VERSION=$15�_�   -   /           .      *    ����                                                                                                                                                                                                                                                                                                                            	           	           V        ^ +!     �         N      A  printf "\n${YELLOW}Pulling${NC} latest $VERSION docker image\n"5�_�   .   0           /          ����                                                                                                                                                                                                                                                                                                                            	           	           V        ^ +(     �         N      &  docker pull coinmine/minary:$VERSION5�_�   /   1           0      '    ����                                                                                                                                                                                                                                                                                                                            	           	           V        ^ +*    �         N      ?  printf "${GREEN}Pulled${NC} latest $VERSION docker image\n\n"5�_�   0               1      .    ����                                                                                                                                                                                                                                                                                                                            	           	           V        ^ +6    �         N      F  printf "${GREEN}Pulled${NC} latest $VMINARY_ERSION docker image\n\n"5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        ^ )�     �              5��