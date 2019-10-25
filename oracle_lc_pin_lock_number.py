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
    cur.execute("select decode(count(*), 0, '0', to_char(count(*))) lc_pin_lock_number	from v$session_wait where event in ('library cache pin', 'library cache lock')")
    result = cur.fetchone()
    cur.close()
    return result
    

try:
    checknum = oracle_check(oraname,orapasswd,oratns) 
    print checknum[0]
except cx_Oracle.DatabaseError as e:
    print(e) 
