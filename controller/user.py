# ./controller/user.py
from flask import Blueprint, request
from service.twitch_service import TwitchService
from service.Oauth20 import get_access_token
from repo.user_operations import add_user

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
    user_data = request.args.get('user_data')

    print("Received code:", code)

    access_token = get_access_token(code)
    add_user(user_data, access_token)

    return 'Sign up successfully'
