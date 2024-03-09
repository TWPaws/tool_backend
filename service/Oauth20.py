# ./service/Oauth20.py

import requests as req


class TwitchService:
    Protocol = 'https://id.twitch.tv/oauth2/token?'

    def __init__(self, access_token):
        self.client_id = 'ecmnwqtzoa9c67bhtjunt7ne2vrog0'
        self.client_secret = 'ogp3p9w1jcymu84ipoik9t2y2fy7en'

    def get_access_token(self, authorization_code):
        headers = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': f'{authorization_code}',
            'grant_type': 'authorization_code',
            'redirect_uri': 'https://dev.twpaws.live/user/twitch_callback'
        }

        response = req.post(
            self.Protocol,
            headers=headers
        )

        print(response)
