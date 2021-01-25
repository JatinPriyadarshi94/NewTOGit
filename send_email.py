
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

#from string import Template
#from pathlib import Path 

#html = Template(Path('index.html').read_text())

html = Template(Path('index.html').read_text())
msg = EmailMessage()
msg['from'] = 'Jatin Priyadarshi'
msg['to'] = 'shivangividyarthi1@gmail.com'
msg['subject'] = 'You\'re Awesome and Beautiful'

msg.set_content(html.substitute({'name':'Dudu'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('jatin1994.jp94@gmail.com', 'kinjal1994')
  smtp.send_message(msg)
  print('all good boss!')

