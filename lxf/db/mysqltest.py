#!/usr/bin/env python
#coding:utf-8

import mysql.connector
#连接数据库是传入参数use_unicode=Tree让mysql的DB-API始终返回unicode
conn = mysql.connector.connect(user='root',password='',host='localhost',database='test',use_unicode=True)
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
cursor.execute('insert into user (id,name) values (%s,%s)',['1','Michael'])
cursor.rowcount
#提交事务
conn.commit()
cursor.close()
#运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id = %s',('1',))
values = cursor.fetchall()
print values
cursor.close()
conn.close()


