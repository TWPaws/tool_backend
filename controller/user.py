from flask import Blueprint, jsonify, request
from service.twitch_service import TwitchService

user = Blueprint('user', __name__)


@user.route('/broadcasters', methods=['GET'])
def get_broadcaster_id():

    access_token = request.args.get('access_token')

    if access_token is None:
        return jsonify({'error': 'Access Token is required'}), 400

    twitch_service = TwitchService(access_token)

    response = twitch_service.get_broadID()
    if response is not None:
        return response
    else:
        return 'False'
