import logging
import smtplib, ssl

class Mail:
    def __init__(self, config):
        self.server = None
        self.smtp_server = config["mail"]["smtpServer"]
        self.port = config["mail"]["mailPort"]
        self.address = config["mail"]["address"]
        self.password = config["mail"]["mailPwd"]

        # Create a secure SSL context
        self.context = ssl.create_default_context()

    def connect(self):
        # Try to log in to server and send email
        try:
            self.server = smtplib.SMTP(self.smtp_server, self.port)
            self.server.ehlo() # Can be omitted
            self.server.starttls(context=self.context) # Secure the connection
            self.server.ehlo() # Can be omitted
            self.server.login(self.address, self.password)
        except Exception as e:
            logging.error(e)

    def disConnect(self):
        if self.server != None:
            self.server.quit()

    def sendMessage(self, message):
        self.server.sendmail(self.address, self.address, message)
