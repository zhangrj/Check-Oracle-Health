#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
from sys import argv
import time
import cx_Oracle
import os

oraname = argv[1]
orapasswd =  argv[2]
oratns = argv[3]
check_level = argv[4]

### read the tablespace list #######

TABLESPACE_LIST = []
filename = '/home/oracle/zabbix/zabbix/' + oratns + '.ini'

if not os.path.exists(filename):
	os.system("touch "+ filename)
else:
	fh = open(filename, 'r')
	for line in fh.readlines():
		temp1  =  line.strip('\n')
		TABLESPACE_LIST.append(temp1)
	fh.close()

#### login oracle and check the tablespace used ratio #####
def oracle_check(uname,upasswd,tnsname):
    oracleln = uname + '/' + upasswd + '@' + tnsname
    con = cx_Oracle.connect(oracleln)
    sql = '''SELECT a.tablespace_name, total, free, ( total - free ), Round(( total - free ) / total, 4) * 100
             FROM   (SELECT tablespace_name,
                       Sum(bytes) free
                       FROM   DBA_FREE_SPACE
                       GROUP  BY tablespace_name) a,
                    (SELECT tablespace_name,
                       Sum(bytes) total
             FROM   DBA_DATA_FILES
                   GROUP  BY tablespace_name) b
                 WHERE  a.tablespace_name = b.tablespace_name'''
    cur = con.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    return result
    
alarmlist1 = []
alarmlist2 = []
normallist1 = []
normallist2 = []
try:
    checknum = oracle_check(oraname,orapasswd,oratns) 
    for row in checknum :
       if row[0] not in TABLESPACE_LIST :
          if row[4] > int(check_level):
             alarmlist1.append(row[0])
             alarmlist2.append(row[4])
          else :
             normallist1.append(row[0])
             normallist2.append(row[4])
    if len(alarmlist1) > 0 :
       for i in range(len(alarmlist1)):
          print "ALARM:" +  alarmlist1[i] + ':表空间利用率' + str(alarmlist2[i]) + '%'
    else :
       print "OK"
       for i in range(len(normallist1)):
          print normallist1[i] + ':表空间利用率' + str(normallist2[i]) + '%'
      #print row
except cx_Oracle.DatabaseError as e:
    print(e) 
