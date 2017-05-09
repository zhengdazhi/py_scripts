#!/usr/bin/env python
#coding:utf-8

import logging
import platform
import sys
import os

#设置日志输出文件
log_filename = "logging.txt"
#设置日志输出格式
log_format =  ' [%(asctime)s] %(message)s'
#将日志格式化
logging.basicConfig(format=log_format,datafmt='%Y-%m-%d %H:%M:%S %p',level=logging.DEBUG,filename=log_filename,filemod='w')

s = '0'
n = int(s)
logging.info('n = %d' %n)
print 10 / n


