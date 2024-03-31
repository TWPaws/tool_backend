# ./service/Oauth20.py

import requests as req
import config as cfg
from flask import current_app   


def get_access_token(authorization_code):
    url = cfg.oauth20_url
    client_id = cfg.client_id
    client_secret = cfg.client_secret
    redirect_url = cfg.redirect_url
    
    current_app.logger.debug(url)
    current_app.logger.debug(client_id)
    current_app.logger.debug(client_secret)
    current_app.logger.debug(redirect_url)

    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': authorization_code,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_url
    }
    response = req.post(url, data=data)
    current_app.logger.debug(response.text)
    data = response.json()
    return data

def validate_access_token(access_token):
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
    else :
        return False

def refresh_access_token(access_token):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
    'grant_type': 'refresh_token',
    'refresh_token': 'gdw3k62zpqi0kw01escg7zgbdhtxi6hm0155tiwcztxczkx17',
    'client_id': '<your client id goes here>',
    'client_secret': '<your client secret goes here>'
    }