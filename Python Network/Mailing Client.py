import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#server = smtplib.SMTP('smtp.gmail.com', 25)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.ehlo()

server.login('resetpassforflasksite@gmail.com', 'dogdogdog')

msg = MIMEMultipart()
msg['From'] = 'Aghilan'
msg['To'] = 'hhk444@gmail.com'
msg['Subject'] = 'Just a test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'dog.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()

for n in range(1):
    server.sendmail('resetpassforflasksite@gmail.com', 'hhk444@gmail.com', text)
