from flask_login import UserMixin


class Users(UserMixin):
    def __init__(self, id, username, password, email, access_token):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.access_token = access_token

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_access_token(self):
        return self.access_token

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
