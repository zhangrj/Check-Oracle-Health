#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os
from sys import argv
import time
import cx_Oracle

os.system('source ~/.bash_profile')
oraname = argv[1]
orapasswd =  argv[2]
oratns = argv[3]


def oracle_check(uname,upasswd,tnsname):
    oracleln = uname + '/' + upasswd + '@' + tnsname
    con = cx_Oracle.connect(oracleln)
    cur = con.cursor()
    sql = ''' select decode(trunc(1 - a.value / b.value),
					0,
					to_char(1 - a.value / b.value, '0.0000'),
					to_char(1 - a.value / b.value)) UsedPer_SGA   
		from (select sum(bytes) value from v$SGASTAT where pool = 'shared pool' and name like '%free%') a,
			 (select sum(bytes) value from v$SGASTAT where pool = 'shared pool') b'''
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    return result
    

try:
    checknum = oracle_check(oraname,orapasswd,oratns) 
    print checknum[0]
except cx_Oracle.DatabaseError as e:
    print(e) 
