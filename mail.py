#coding: utf-8    
  
import smtplib    
from email.mime.multipart import MIMEMultipart    
from email.mime.text import MIMEText    
from email.mime.image import MIMEImage 
from email.header import Header   
    
sender_name='xxx'    

smtpserver = 'smtp.vip.163.com'
username = sender_name+'@vip.163.com'
# vip 163 客户授权码，非登录密码
password='AUTHCODE' 
sender= sender_name+'@vip.163.com'
receiver=['yyy@gmail.com',sender_name+'@vip.163.com']

def send(msg):
  smtp = smtplib.SMTP()    
  smtp.connect('smtp.vip.163.com')
  #打印出和SMTP服务器交互的所有信息。
  #smtp.set_debuglevel(1)  
  smtp.login(username, password)    
  smtp.sendmail(sender, receiver, msg.as_string())    
  smtp.quit()

def construct_msg():
  subject = 'Python3 email test'
  msg = MIMEMultipart('mixed') 
  msg['Subject'] = subject
  msg['From'] = sender_name+'@vip.163.com '+ '<' + sender_name + '@vip.163.com>'
  msg['To'] = ";".join(receiver) 
  text = "Hi!\nHow are you?"    
  text_plain = MIMEText(text,'plain', 'utf-8')    
  msg.attach(text_plain)  
  return msg  
  
if __name__ == '__main__':
  msg = construct_msg()
  send(msg)
