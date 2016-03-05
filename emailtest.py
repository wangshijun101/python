#!/usr/bin/env python
from email.mime.text import MIMEText
msg = MIMEText('hello,send by Python...','plan','utf-8')
from_addr = '631715271@qq.com'
password = 'wawdngt7758521!@'
smtp_server = 'smtp.qq.com'
to_addr = 'wfeiyangvip@163.com'


import smtplib
server = smtplib.SMTP(smtp_server ,25)
#server.set_debuglever(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

