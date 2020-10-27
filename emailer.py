import smtplib, ssl
from email.message import EmailMessage

#Simple class that will notify me upon completion of a long script.
class ProgressEmail():
    def __init__(self, sender, recipient, password):
        self.recipient = recipient
        self.sender = sender
        self.password = password


    def sendEmail(self, subject, content):
        '''sendEmail creates and sends an email to the recipient, using content provided
        as an argument'''   
        port = 465  
        message = EmailMessage()
        message['Subject'] = subject
        message['From'] = self.sender
        message['To'] = self.recipient
        message.set_content(content)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(self.sender, self.password)
        server.send_message(message, self.recipient)
        server.close()