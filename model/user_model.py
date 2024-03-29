from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, username, email, password, access_token, broadcaster_id):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.access_token = access_token
        self.broadcaster_id = broadcaster_id

    def get_id(self):
        return str(self.id)
