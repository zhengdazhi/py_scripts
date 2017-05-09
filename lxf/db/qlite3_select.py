#!/usr/bin/env python
#coding:utf-8

import sqlite3


#查询记录
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#执行查询语句
#cursor.execute('select * from user where id=?',('1',))
cursor.execute('select * from user')
#获得查询结果
values = cursor.fetchall()
print values
cursor.close()
conn.close()





