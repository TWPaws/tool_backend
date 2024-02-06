# ./controller/user.py
from flask import Blueprint, request, jsonify
from service.twitch_service import TwitchService
from urllib.parse import urlparse, parse_qs 

user = Blueprint('user', __name__)


@user.route('/broadcasters', methods=['GET'])
def get_broadcaster_id():

    access_token = request.args.get('access_token')

    if access_token is None:
        return ({'error': 'Access Token is required'})

    twitch_service = TwitchService(access_token)

    response = twitch_service.get_broadcaster_id()
    if response is not None:
        return response
    else:
        return 'False'


@user.route('/twitch_callback/', methods=['GET'])
def twitch_callback():
    code = request.args.get('code')

    print("Received code:", code)

    return 'Received code successfully'