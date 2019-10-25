#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

# zabbix sender path
zabbix_sender = '/usr/bin/zabbix_sender'

# oracle username,password,tnsname.hostname
oracle = ['username5','password5','tnsname5','zabbix_hostname5']

# script list 
# script path,zabbix item key
ScriptList = [['/home/oracle/zabbix/oracle_con_unused.sh','oracle.oracle_con_unused'],
                ['/home/oracle/zabbix/oracle_data_buffer_ratio.sh','oracle.oracle_data_buffer_ratio'],
                ['/home/oracle/zabbix/oracle_df_scatter_read.sh','oracle.oracle_df_scatter_read'],
                ['/home/oracle/zabbix/oracle_SGA_logical_phys_reads.sh','oracle.oracle_SGA_logical_phys_reads'],
                ['/home/oracle/zabbix/oracle_df_seq_read.sh','oracle.oracle_df_seq_read'],
                ['/home/oracle/zabbix/oracle_enqueuenum.sh','oracle.oracle_enqueuenum'],
                ['/home/oracle/zabbix/oracle_latchnum.sh','oracle.oracle_latchnum'],
                ['/home/oracle/zabbix/oracle_lc_pin_lock_number.sh','oracle.oracle_lc_pin_lock_number'],
                ['/home/oracle/zabbix/oracle_lock_num.sh','oracle.oracle_lock_num'],
                ['/home/oracle/zabbix/oracle_longtimesessionnum.sh','oracle.oracle_longtimesessionnum'],
                ['/home/oracle/zabbix/oracle_share_pool_used.sh','oracle.oracle_share_pool_used'],
                ['/home/oracle/zabbix/oracle_tablespace_check.sh','oracle.oracle_tablespace_check'],
                ['/home/oracle/zabbix/oracle_waitlockeventsnum.sh','oracle.oracle_waitlockeventsnum']]

for script in ScriptList:
        script_command = script[0] + ' \'' + oracle[0] + '\' \'' + oracle[1] + '\' \'' + oracle[2] + '\''
        if script[0] == '/home/oracle/zabbix/oracle_tablespace_check.sh':
                command_result = os.popen(script_command).read().rstrip('\n')
                command_result = command_result.replace('\n','<br/>')
        else:
                command_result = os.popen(script_command).read().rstrip('\n')
        zabbix_sender_command = zabbix_sender + ' -z 192.168.128.181 -s ' + oracle[3] + ' -k ' + script[1] + ' -o \'' + command_result + '\''
        print zabbix_sender_command
        os.system(zabbix_sender_command)
