#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import cx_Oracle

# zabbix sender path
zabbix_sender = '/usr/bin/zabbix_sender'

# oracle username,password,tnsname.hostname
OracleList = [['username1','password1','tnsname1','zabbix_hostname1'],
                ['username2','password2','tnsname2','zabbix_hostname2'],
                ['username3','password3','tnsname3','zabbix_hostname3'],
                ['username4','password4','tnsname4','zabbix_hostname4'],
                ['username5','password5','tnsname5','zabbix_hostname5']]


def session_check(uname,upasswd,tnsname):
    oracleln = uname + '/' + upasswd + '@' + tnsname
    con = cx_Oracle.connect(oracleln)
    cur = con.cursor()
    sql = '''select count(*) from v$session'''
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    return result
    

def process_check(uname,upasswd,tnsname):
    oracleln = uname + '/' + upasswd + '@' + tnsname
    con = cx_Oracle.connect(oracleln)
    cur = con.cursor()
    sql = '''select count(*) "procnum" from v$process'''
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    return result

for oracle in OracleList:
    session_used = session_check(oracle[0],oracle[1],oracle[2])
    os.system(zabbix_sender + ' -z 192.168.128.181 -s ' + oracle[3] + ' -k oracle.session.used -o ' + str(session_used[0]))
    process_used = process_check(oracle[0],oracle[1],oracle[2])
    os.system(zabbix_sender + ' -z 192.168.128.181 -s ' + oracle[3] + ' -k oracle.process.used -o ' + str(session_used[0]))