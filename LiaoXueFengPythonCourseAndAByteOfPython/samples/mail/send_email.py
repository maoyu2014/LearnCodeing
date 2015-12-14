from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(),addr))



from_addr = input('From:')
password = input('Password:')
to_addr = input('To:')
# smtp_server = input('SMTP server:')

smtp_server = 'smtp.sina.com'

# msg = MIMEText('hello, send by python...', 'plain', 'utf-8')

# msg = MIMEText('<html><body><h1>Hello</h1>'  +
#                 '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#                 '</body></html>', 'html', 'utf-8')

msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候', 'utf-8').encode()
msg['Subject'] = 'greeting from smtp'

msg.attach(MIMEText('hello, send with file...', 'plain', 'utf-8'))

with open('./test.jpg', 'rb') as f:
    mime = MIMEBase('image','jpg',filename='test.jpg')
    mime.add_header('Content-Disposition','attachment',filename='test.jpg')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment_Id','0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
    

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
