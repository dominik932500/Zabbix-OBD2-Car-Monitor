# Zabbix-OBD2-Car-Monitor
Car monitoring is done using a Bluetooth ELM327 OBD-II dongle connected to a Raspberry Pi 3. Car data from the dongle is read with a Python 3 script (carmonitoring.py) and is sent to the Zabbix server via Zabbix agent.
Additionally, USB modem can be monitored too. ZTE MF 823 was used in this project. It is monitored with networkmonitoring.py script. Network monitoring might not work with different modems. 
Two XML files are used to import alarms and triggers to the Zabbix server. If your host has a dynamic IP then the hosts file is not needed as long as you make an autodiscovery rule on your Zabbix server. 
raspberrymon.sh file is used to measure Rasberry Pi microcomputers parameters, especially the operating CPU temperature. 
It is recommended to run all three files on startup as a service to fully automate the car monitoring process. 
