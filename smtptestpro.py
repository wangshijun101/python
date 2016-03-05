#!/usr/bin/env python
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib
def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr(( 
			Header(name,'utf-8').encode(), 
			addr.encode('utf-8') if isinstance(addr,unicode) else addr))
	
from_addr = '631715271@qq.com'
password = 'wawdngt7758521!@'
smtp_server = 'smtp.qq.com'
to_addr = 'wfeiyangvip@163.com'

#msg = MIMEText('<html><body><h1>HELLO! EveryOne...</h1><a href="#">Joseph ###</a></body></html>','html','utf-8')
#msg['From'] = _format_addr(u'Python message <%s>' % from_addr)
#msg['To'] = _format_addr(u'Administrator <%s>' % to_addr)
#msg['Subject'] = Header(u'From SMTP\'s question','utf-8').encode()
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python I love u <%s>' % from_addr)
msg['To'] = _format_addr(u'Administrator <%s>' % to_addr)
msg['Subject'] = Header(u'From Waixingren de mimim','utf-8').encode()
msg.attach(MIMEText('send with file...','plan','utf-8'))


with open('~/Downloads/rujia.png','rb') as f:
	mime = MIMEBase('image','png',filename = 'rujia.png')
	mime.add_header('Content-Disposition','attachment',filename='rujia.png')
	mime.add_header('Content-ID','<0>')
	mime.add_header('X-Attachment-Id','0')
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)
server = smtplib.SMTP(smtp_server ,25)
#server.set_debuglever(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
