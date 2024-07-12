class User:
    def __init__(self, mail, pwd, pid=None):
        self.mail = mail
        self.password = pwd
        self.pid = pid

    def get_mail(self):
        return self.mail

    def get_password(self):
        return self.password

    def get_pid(self):
        return self.pid