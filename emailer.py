import smtplib, ssl
from email.message import EmailMessage

class ProgressEmail():
    def __init__(self, sender, recipient, subject, password):
        '''Init method requires sender and recipient email address, the email subject
        and the password'''
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.password = password

    def sendEmail(self, content):
        '''sendEmail creates and sends an email to the recipient, using content provided
        as an argument'''
        port = 465  
        message = EmailMessage()
        message['Subject'] = self.subject
        message['From'] = self.sender
        message['To'] = self.recipient
        message.set_content(content)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(self.sender, self.password)
        server.send_message(message, self.recipient)
        server.close()

if __name__=='__main__':
    sender = input('Please enter the sender: ')
    password = input('Please enter password: ')
    recipient = input('Please enter recipient: ')
    subject = input('Please enter subject')
    email = ProgressEmail(sender, recipient, subject, password)
    email.sendEmail('This is the email content.')
