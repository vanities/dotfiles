Vim�UnDo� ��������@��;��2z��{���0H�                                      ]F    _�                            ����                                                                                                                                                                                                                                                                                                                                                             ]F}     �                   �               5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             ]F~    �                  5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             ]F{     �              �                     [Unit]   "Description=Minary Wifi Controller   Requires=dbus.service   After=network-online.target   Wants=network-online.target   StartLimitInterval=200   StartLimitBurst=5       	[Service]   	User=root   TimeoutStartSec=infinity   lExecStartPre=/bin/bash -c "/usr/bin/systemctl set-environment SHORT_UUID=$(cat /etc/machine-id | cut -c -8)"   oExecStartPre=/bin/bash -c "/usr/bin/systemctl set-environment WIFI_HOTSPOT_SSID=Coinmine-${SHORT_UUID:-xxxxxx}"   EEnvironment=MINARY_SENTRY_PUBLIC_KEY=e295da6c82fe4b7aa41d56b65649a8af   ,Environment=MINARY_SENTRY_PROJECT_ID=1307349   "Environment=MINARY_LOG_LEVEL=DEBUG   $Environment=WIFI_SERVER_HOST=0.0.0.0   !Environment=WIFI_SERVER_PORT=5000   ,Environment=WIFI_HOTSPOT_PASSWORD=0123456789   'Environment=CONN_ATTEMPT_MAX_SECONDS=60   )Environment=HOSTNAME_CHECK=www.google.com   2Environment=MINARY_MACHINE_ID_PATH=/etc/machine-id   8Environment=MINARY_CONFIG_PATH=/home/satoshi/config.yaml   :Environment=MINARY_AMBIANCE_SERVER_URL=http://0.0.0.0:5006   &ExecStart=/usr/local/bin/./wifi_server   Restart=on-failure   RestartSec=5       	[Install]   WantedBy=multi-user.target5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             ]F|     �             �               [Unit]   "Description=Minary Wifi Controller   Requires=dbus.service   After=network-online.target   Wants=network-online.target   StartLimitInterval=200   StartLimitBurst=5       	[Service]   	User=root   TimeoutStartSec=infinity   lExecStartPre=/bin/bash -c "/usr/bin/systemctl set-environment SHORT_UUID=$(cat /etc/machine-id | cut -c -8)"   oExecStartPre=/bin/bash -c "/usr/bin/systemctl set-environment WIFI_HOTSPOT_SSID=Coinmine-${SHORT_UUID:-xxxxxx}"   EEnvironment=MINARY_SENTRY_PUBLIC_KEY=e295da6c82fe4b7aa41d56b65649a8af   ,Environment=MINARY_SENTRY_PROJECT_ID=1307349   "Environment=MINARY_LOG_LEVEL=DEBUG   $Environment=WIFI_SERVER_HOST=0.0.0.0   !Environment=WIFI_SERVER_PORT=5000   ,Environment=WIFI_HOTSPOT_PASSWORD=0123456789   'Environment=CONN_ATTEMPT_MAX_SECONDS=60   )Environment=HOSTNAME_CHECK=www.google.com   2Environment=MINARY_MACHINE_ID_PATH=/etc/machine-id   8Environment=MINARY_CONFIG_PATH=/home/satoshi/config.yaml   :Environment=MINARY_AMBIANCE_SERVER_URL=http://0.0.0.0:5006   &ExecStart=/usr/local/bin/./wifi_server   Restart=on-failure   RestartSec=5       	[Install]   WantedBy=multi-user.target5��