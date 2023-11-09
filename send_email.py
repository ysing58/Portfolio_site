import smtplib
import ssl
import os

def Send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "yadvendra187@gmail.com"
    password = os.getenv("PASSWORD")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, message)

