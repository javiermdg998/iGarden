import smtplib
from datetime import datetime
gmail_user = 'igarden.deusto@gmail.com'
gmail_password = 'igarden00'

sent_from = gmail_user
f = open ('servicio/horas_regado.txt','r')

to = 'igarden.deusto@gmail.com'
subject = "GRAFICOS DE REGADO"
body = f.read()
f.close
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, "".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print("Email sent")
except:
    print("Error")

f = open('servicio/horas_regado.txt','w')
f.write("HORAS DE REGADO EN " + datatime.today)
f.close()