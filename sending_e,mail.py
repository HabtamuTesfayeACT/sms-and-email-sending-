import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(receiver_email):
    # Set up the SMTP server
    # Data
    sender_email = 'Alazardg881@gmail.com'
    sender_password = 'romrkuidpyfnwuti'
    smtp_server = 'smtp.gmail.com'
    subject = 'Hello from Python!'
    message = 'This is a test email sent from Python.'

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message to the body of the email
    msg.attach(MIMEText(message, 'plain'))

    # Start the SMTP server session
    with smtplib.SMTP(smtp_server, 587) as server:
        server.starttls()  # Enable secure connection
        server.login(sender_email, sender_password)
        server.send_message(msg)
    print('Email sent successfully to {}'.format(receiver_email))


receiver_emails = ['habtamutesfaye678@gmail.com','habtamupro@gmail.com','habtamutesfaye.com.@gmail.com']  

# Call the send_email function for each email address
list(map(send_email, receiver_emails))
