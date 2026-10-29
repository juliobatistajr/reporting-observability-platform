import os
import smtplib
import time

from dotenv import load_dotenv

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()


def enviar_email(
    to,
    cc,
    assunto,
    html
):

    email = os.getenv("EMAIL_USER")
    senha = os.getenv("EMAIL_PASSWORD")

    msg = MIMEMultipart()

    msg["Subject"] = assunto
    msg["From"] = email
    msg["To"] = ";".join(to)

    if cc:
        msg["CC"] = ";".join(cc)

    msg.attach(
        MIMEText(
            html,
            "html",
            "utf-8"
        )
    )

    destinatarios = to + cc

    servidor = smtplib.SMTP(
        "smtp.office365.com",
        587
    )

    servidor.starttls()

    servidor.login(
        email,
        senha
    )

    servidor.sendmail(
        email,
        destinatarios,
        msg.as_string()
    )

    servidor.quit()

    print("✅ E-mail enviado com sucesso!")
    time.sleep(2)