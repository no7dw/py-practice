#coding: utf-8    
  
import smtplib    
from email.mime.multipart import MIMEMultipart    
from email.mime.text import MIMEText    
from email.mime.image import MIMEImage 
from email.header import Header   
    
smtpserver = 'smtp.vip.163.com'
username = 'sender@vip.163.com'
password='AUTHCODE'
sender='sender@vip.163.com'
receiver=['receiver@126.com','receiver@gmail.com','sender@vip.163.com']

subject = 'Python3 email test'

msg = MIMEMultipart('mixed') 
msg['Subject'] = subject
msg['From'] = 'sender@vip.163.com <sender@vip.163.com>'
msg['To'] = ";".join(receiver) 

text = "Hi!\nHow are you?"    
text_plain = MIMEText(text,'plain', 'utf-8')    
msg.attach(text_plain)    

smtp = smtplib.SMTP()    
smtp.connect('smtp.vip.163.com')
#打印出和SMTP服务器交互的所有信息。
#smtp.set_debuglevel(1)  
smtp.login(username, password)    
smtp.sendmail(sender, receiver, msg.as_string())    
smtp.quit()