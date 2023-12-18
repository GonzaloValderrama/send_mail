import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del correo electrónico
remitente = "ggonzalovalderrama@gmail.com"
destinatario = ("ggonzalovalderrama@gmail.com")
asunto = "Buena Machucao"
mensaje = "SPAM! JAJAJA\n TE MEO!\n USANDO PYTHON!!\n :D"

# Configuración de la conexión SMTP con Gmail
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "ggonzalovalderrama@gmail.com"
smtp_password = "dhpy badk wmsu aaaz --> contraseña de ejemplo"  # Genera una contraseña de aplicación desde la configuración de seguridad de tu cuenta de Google

# Crear el objeto del mensaje
msg = MIMEMultipart()
msg["From"] = remitente
msg["To"] = destinatario
msg["Subject"] = asunto

# Añadir el cuerpo del mensaje
msg.attach(MIMEText(mensaje, "plain"))

try:
    # Iniciar la conexión SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Habilitar el modo seguro
        server.starttls()
        
        # Iniciar sesión en la cuenta de correo electrónico
        server.login(smtp_username, smtp_password)
        
        # Enviar el correo electrónico
        server.sendmail(remitente, destinatario, msg.as_string())
        
    print("Correo electrónico enviado exitosamente.")

except Exception as e:
    print(f"Error al enviar el correo electrónico: {e}")
