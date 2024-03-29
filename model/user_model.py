from flask_login import UserMixin


class Users(UserMixin):
    def __init__(self, id, username, email, password, access_token, broadcaster_id):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.access_token = access_token
        self.broadcaster_id = broadcaster_id

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_access_token(self):
        return self.access_token

    def get_broadcaster_id(self):
        return self.broadcaster_id

    def get_id(self):
        return str(self.id)
