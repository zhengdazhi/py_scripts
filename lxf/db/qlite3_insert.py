#!/usr/bin/env python
#coding:utf-8

import sqlite3

#连接到SQLite数据库
#数据库文件是test.db
#如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('test.db')
#创建一个cursor(游标)
cursor = conn.cursor()
#执行一条sql语句，创建user表
cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
#插入记录
cursor.execute('insert into user (id,name) values (\'1\',\'Micheal\')')
#通过rowcount活动插入的行数
cursor.rowcount
#关闭cursor
cursor.close()
#提交事务
conn.commit()
#关闭connections
conn.close()
