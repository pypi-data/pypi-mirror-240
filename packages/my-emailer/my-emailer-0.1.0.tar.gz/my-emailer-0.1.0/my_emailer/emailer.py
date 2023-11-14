import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from validate_email_address import validate_email

def setup_email_server(server, port, sender_email, password):
    return {'server': server, 'port': port, 'sender_email': sender_email, 'password': password}

def is_valid_email(email):
    try:
        result = validate_email(email, verify=False)
        return result and '@' in email
    except Exception as e:
        print(f"Error validating email: {e}")
    return False

def send_email(recipient, subject, body, server=None):
    if server is None:
        raise ValueError("Sèvè imel la dwe konfigire avan ou voye yon imèl.")

    if not is_valid_email(recipient):
        raise ValueError("Imèl sa pa valide.")

    sender_email = server['sender_email']
    password = server['password']
    server_addr = server['server']
    port = server['port']

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(server_addr, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient, msg.as_string())

recipient_email = input("Entrez l'adresse email du destinataire : ")
email_subject = input("Entrez le sujet de l'email : ")
email_body = input("Entrez le contenu de l'email : ")

server = setup_email_server(server="smtp.gmail.com", port=587, sender_email="marcdonaldtech40@gmail.com", password="msbx kmxx omit uthm ")
send_email(recipient=recipient_email, subject=email_subject, body=email_body, server=server)
