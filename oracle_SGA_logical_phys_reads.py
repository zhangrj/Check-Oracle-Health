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
    sql = '''select to_char(round((1 - physical_reads / (db_block_gets + consistent_gets)), 5),'0.00000') HitRatio_DataCache   
		from (select value as physical_reads
				from v$sysstat
			   where name = 'physical reads'),
			 (select value as db_block_gets
				from v$sysstat
			   where name = 'db block gets'),
			 (select value as consistent_gets
				from v$sysstat
			   where name = 'consistent gets')''' 
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    return result
    

try:
    checknum = oracle_check(oraname,orapasswd,oratns) 
    print checknum[0]
except cx_Oracle.DatabaseError as e:
    print(e) 
