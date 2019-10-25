#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
from sys import argv
import time
import cx_Oracle

oraname = argv[1]
orapasswd =  argv[2]
oratns = argv[3]

def oracle_check(uname,upasswd,tnsname):
    oracleln = uname + '/' + upasswd + '@' + tnsname
    con = cx_Oracle.connect(oracleln)
    cur = con.cursor()
    sql = '''select 	 decode(b.value, 0, '0', to_char(b.value)) connections_all,
			  decode(b.value-a.value, 0, '0', to_char(b.value-a.value)) connections_unused
		from (select count(*) value from v$session where status = 'ACTIVE' and type <> 'BACKGROUND') a,
			 (select count(*) value from v$session where type <> 'BACKGROUND') b'''
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    return result
    

try:
    checknum = oracle_check(oraname,orapasswd,oratns) 
    print checknum[1]
except cx_Oracle.DatabaseError as e:
    print(e) 
