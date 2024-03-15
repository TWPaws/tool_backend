# ./service/Oauth20.py

import requests as req


def get_access_token(self, authorization_code):
    headers = {
        'client_id': 'ecmnwqtzoa9c67bhtjunt7ne2vrog0',
        'client_secret': 'ogp3p9w1jcymu84ipoik9t2y2fy7en',
        'code': f'{authorization_code}',
        'grant_type': 'authorization_code',
        'redirect_uri': 'https://dev.twpaws.live/user/twitch_callback'
    }
    response = req.post(
        'https://id.twitch.tv/oauth2/token?',
        headers=headers
    )
    print(response)
