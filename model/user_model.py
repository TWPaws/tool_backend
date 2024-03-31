from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, nickname, username, email, password, access_token, broadcaster_id, verified, refresh_token):
        self.id = id
        self.nickname = nickname
        self.username = username
        self.password = password
        self.email = email
        self.access_token = access_token
        self.broadcaster_id = broadcaster_id
        self.verified = verified
        self.refresh_token = refresh_token

    def get_id(self):
        return str(self.id)
