import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()

# Configurar el servidor SMTP
smtp_server = "smtp.example.com"  # Reemplaza con el servidor SMTP real
smtp_port = 587  # Puerto SMTP común para TLS
sender_email = os.getenv("EMAIL_USER")  # Tu dirección de correo electrónico (REMITENTE)
password = os.getenv("PASSWORD_APP")  # Tu contraseña de correo electrónico
email_example = "example@example.com" # direccion de correo electrónico del DESTINATARIO 

# Crear el mensaje de correo electrónico
mensaje = MIMEText("Este es un correo electrónico de prueba enviado con smtplib.")
mensaje["From"] = sender_email
mensaje["To"] = "example@example.com"  # Reemplaza con el correo electrónico del destinatario
mensaje["Subject"] = "Correo de prueba de smtplib"

server = smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.login(sender_email,password)
server.sendmail(sender_email,email_example , mensaje.as_string())
server.quit()

print("Correo electrónico enviado correctamente.")
