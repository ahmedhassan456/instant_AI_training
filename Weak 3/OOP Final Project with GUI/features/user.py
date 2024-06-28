<<<<<<< HEAD
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_credentials(self, input_username, input_password):
=======
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_credentials(self, input_username, input_password):
>>>>>>> b64c73be611407c03eaf6647be6f36ba75be5d14
        return self.username == input_username and self.password == input_password