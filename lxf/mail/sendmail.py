#!/usr/bin/env python
#coding:utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
import email.mime.
from email.utils import parseaddr,formataddr
import smtplib

#定义内部函数，用于格式输入的数据
def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr(( \
			Header(name,'utf-8').encode(), \
			addr.encode('utf-8') if isinstance(addr,unicode) else addr))

#输入发件箱
#from_addr = raw_input('From:')
from_addr = "zhengdz@cnfol.net"
#输入发件箱密码
#password = raw_input('Password:')
password = "zhengdazhi123"
#输入收件件箱地址
#to_addr = raw_input('To:')
to_addr = "zhengdazhikof@126.com"
#输入发件箱的smtp邮件服务器
#smtp_server = raw_input('SMTP server:')
smtp_server = "smtp.exmail.qq.com"

#构造邮件对象

#msg = MIMEText('hello,send by Python...','plain','utf-8')
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自smtp的问候....','utf-8').encode()

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()



