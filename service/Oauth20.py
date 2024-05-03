# ./service/Oauth20.py

import requests as req
import config as cfg


def get_access_token(authorization_code):
    url = cfg.oauth20_url
    client_id = cfg.client_id
    client_secret = cfg.client_secret
    redirect_url = cfg.redirect_url

    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': authorization_code,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_url
    }
    response = req.post(url, data=data)
    data = response.json()
    return data


def validate_access_token(access_token):
    if (access_token is not None):
        headers = {
            'Authorization': f'OAuth {access_token}'
        }

        url = cfg.oauth20_valid

        response = req.get(
           url,
           headers=headers
        )

        if response.status_code == 200:
            return True
        else:
            return False
    else:
        return False


def refresh_access_token(refresh_token):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': cfg.client_id,
        'client_secret': cfg.client_secret
    }

    url = cfg.oauth20_url

    response = req.post(
        url,
        headers=headers,
        data=data
    )

    if response.status_code == 200:
        return response.json()
    else:
        return False
