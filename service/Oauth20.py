# ./service/Oauth20.py

import requests as req


def get_access_token(authorization_code):
    url = 'https://id.twitch.tv/oauth2/token'
    client_id = 'ecmnwqtzoa9c67bhtjunt7ne2vrog0'
    client_secret = 'ogp3p9w1jcymu84ipoik9t2y2fy7en'
    redirect_uri = 'https://dev.twpaws.live/api/user/twitch_callback'

    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': authorization_code,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri
    }

    response = req.post(url, data=data)
    data = response.json()
    return data["access_token"]

def validate_access_token(access_token):
    headers = {
        'Authorization': f'OAuth {self.access_token}',
    }

    url = 'https://id.twitch.tv/oauth2/validate'
    
    response = req.get(
       url,
       headers=headers 
    )

    if response.status_code == 200:
        return True
    else :
        return False