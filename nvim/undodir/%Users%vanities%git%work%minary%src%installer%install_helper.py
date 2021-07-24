Vim�UnDo� n�
 ����{�cY\mY
`�(\���x_�G�      class InstallHelper:                             \��    _�                            ����                                                                                                                                                                                                                                                                                                                                                             \ԥF     �                  �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \ԥf     �                   �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             \ԥh    �                      class InstallHelper:       pass    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             \��    �                class InstallHelper:5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             \ԥE     �              �                
b'#!/bin/bash\n\nNC=\'\\e[0m\' # No Color\nRED=\'\\e[0;31m\'\nYELLOW=\'\\e[1;33m\'\nGREEN=\'\\e[0;32m\'\nROOT_DIR=\'/app/cli/mineOS/.host_root\'\n\nset -e\n\nDOCKER_AUTH=$(curl -s http://0.0.0.0:5002/config | jq -r .docker_auth)\nif [ "$DOCKER_AUTH" = "" ];\nthen\n  printf "No docker_auth setting, using default\\n"\nelse\n  printf "Found docker_auth setting\\n"\n  DOCKER=$(echo "$DOCKER_AUTH" | base64 -d -)\n  DOCKER_USER=$(echo "$DOCKER" | cut -d : -f 1)\n  DOCKER_PASS=$(echo "$DOCKER" | cut -d : -f 2)\n  echo "$DOCKER_PASS" | docker login --username "$DOCKER_USER" --password-stdin\nfi\n\nGRUB=$(cat /etc/default/grub)\n\nif [ -z "$1" ]; then\n  printf "No version supplied, using env.\\n\\n"\n  CURRENT_MINARY_VERSION=$(curl -s http://0.0.0.0:5002/system_info | jq -r .minary_version)\n  DESIRED_MINARY_VERSION=$(curl -s http://0.0.0.0:5002/config | jq -r .docker_tag)\n  printf "CURRENT_MINARY_VERSION=$CURRENT_MINARY_VERSION\\n"\n  printf "DESIRED_MINARY_VERSION=$DESIRED_MINARY_VERSION\\n\\n"\n\n  if [ "$CURRENT_MINARY_VERSION" = "$DESIRED_MINARY_VERSION" ]; then\n    printf "\\nCurrent and desired versions are the same - exiting install\\n\\n"\n    printf "USAGE: $0 [VERSION]\\nExample: $ $0 0.2.9\\n\\n"\n    exit 1\n  elif [ "$DESIRED_MINARY_VERSION" = "" ]; then\n    printf "\\nNo desired version supplied\\n\\n"\n    exit 1\n  else\n    VERSION=$DESIRED_MINARY_VERSION\n  fi\nelse\n  VERSION=$1\n  printf "version supplied, using version: ${YELLOW}$VERSION${NC}\\n"\n  docker pull coinmine/minary:$VERSION\nfi\n\nif [ "$2" = "staging" ]; then\n  ENVIRONMENT="staging"\nelif [ -f /home/satoshi/config.yaml ]; then\n  ENVIRONMENT=$(cat /home/satoshi/config.yaml | grep \'env\' | awk \'{print $2}\')\nelse\n  ENVIRONMENT="production"\nfi\n\nprintf "\\nBeginning ${GREEN}${ENVIRONMENT}${NC} installation\\n\\n"\n\ndocker run --rm -i \\\n  --env ENVIRONMENT=$ENVIRONMENT \\\n  --env VERSION=$VERSION \\\n  --volume "/etc:/etc" \\\n  --volume "/usr/local/bin:$ROOT_DIR/usr/local/bin" \\\n  --volume "/usr/lib/python3.7/site-packages:$ROOT_DIR/usr/lib/python3.7/site-packages" \\\n  --volume "/root:$ROOT_DIR/root" \\\n  --volume "/home:$ROOT_DIR/home" \\\n  --volume "/run/systemd:/run/systemd" \\\n  --volume "/var/run/dbus:/var/run/dbus" \\\n  --volume "/sys/fs/cgroup:/sys/fs/cgroup:ro" \\\n  --volume "/var/run/docker.sock:/var/run/docker.sock" \\\n  --volume "/systemd/run:/systemd/run" \\\n  --workdir "/app/cli/" \\\n  --privileged \\\n  coinmine/minary:$VERSION make install --no-print-directory\n\nNEW_GRUB=$(cat /etc/default/grub)\n\nif [ "$GRUB" != "$GRUB" ];\nthen\n  printf "\\nUpdating ${GREEN}grub${NC}\\n\\n"\n  grub-mkconfig -o /boot/grub/grub.cfg\nfi\n'5��