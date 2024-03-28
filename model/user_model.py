from flask_login import UserMixin
from repo.user_operations import search_user


class Users(UserMixin):
    def __init__(self, username, password):
        user = search_user(username, password)
        self.username = user['username']
        self.password = user['password']
        self.email = user['email']
        self.access_token = user['access_token']

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_access_token(self):
        return self.access_token
