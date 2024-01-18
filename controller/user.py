from flask import Blueprint, jsonify
from service.twitch_service import TwitchService

access_token = 'zzphl0ev6dtb1v9heg7s9rpngvgh69'
client_id = 'fhc0ko2asch2gf7ya4ame220yahpka'
broadcaster_id = "29127270"
twitch_service = TwitchService(access_token, client_id)

user = Blueprint('user_route', __name__)


@user.route('/broadcasters', methods=['GET'])
def get_broadcaster_id():
    if access_token is None:
        return jsonify({'error': 'Access Token is required'}), 400

    response = twitch_service.get_broadcaster_id(access_token, client_id)
    if response is not None:
        return jsonify({'broadcaster_id': response})
    else:
        return jsonify({f"Error: {response.status_code}, {response.text}"})
