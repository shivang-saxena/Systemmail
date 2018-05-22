import imapclient 
import pyzmail
import smtplib
def send():
 s  = smtplib.SMTP('smtp.gmail.com',587)
 s.ehlo()
 s.starttls()
 s.login('your_email_address','email_password')
 s.sendmail('your_email_address','your_email_address','subject- what is the next command sir')
def recv():
 time.sleep(20)
 i = imapclient.IMAPClient('imap.gmail.com',ssl=True)
 i.login('your_email_address','your_password')
 i.select_folder('INBOX',readonly=True)
 u = i.search('SINCE current_date','FROM your_email_address')
 for i in range(1,1000):
 if i==1:
  try:
   u[i]
  except:
   p = u[i-1]
   break
 m = pyzmail.PyzMessage.factory(r[p][b'BODY[]'])
 v = m.get_subject
 try:
  os.system(v)
  #command executed on remote mashine'
 except:
  pass
while True:
 send() 
 recv()