import os
import smtplib

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def send_email(subject, text, receiver_email):
    """
    Send an email with gmail. 
    """
    smtp_server = "127.0.0.1"
    sender_email = "spot_admin@noaa.gov"  # Enter your address

    # context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server) as server:
        server.set_debuglevel(1)
        server.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{text}")
    
