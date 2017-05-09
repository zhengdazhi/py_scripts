#!/usr/bin/env python
#coding:utf-8

from email import encoders
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.MIMEBase import MIMEBase
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

# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()


# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('mail.png','rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='mail.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='mail.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

