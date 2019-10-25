#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

# zabbix sender path
zabbix_sender = '/usr/bin/zabbix_sender'
check_tnsping = '/home/nagios/bin/check_oracle_health'

# oracle username,password,tnsname.hostname
tnsnameList = ['tnsname1', 'tnsname2',
               'tnsname3','tnsname4', 'tnsname5']

for tnsname in tnsnameList:
    check_command = check_tnsping + ' --connect=' + tnsname + ' --mode=tnsping'
    command_result = os.popen(check_command).read().rstrip('\n')
    zabbix_sender_command = zabbix_sender + ' -z 192.168.128.181 -s ' + \
        tnsname + ' -k oracle.tnsping -o \'' + command_result + '\''
    os.system(zabbix_sender_command)
