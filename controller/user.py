# ./controller/user.py
from flask import Blueprint, request
from service.twitch_service import TwitchService

user = Blueprint('user', __name__)


@user.route('/broadcasters', methods=['GET'])
def get_broadcaster_id():

    access_token = request.args.get('access_token')

    if access_token is None:
        return ({'error': 'Access Token is required'})

    twitch_service = TwitchService(access_token)

    response = twitch_service.get_broadID()
    if response is not None:
        return response
    else:
        return 'False'


@user.route('/twitch_callback', methods=['GET'])
def twitch_callback():
    data = request.json
    access_token = data.get('access_token')

    print(access_token)

    return json('Hello world')
