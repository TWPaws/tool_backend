from flask import Blueprint, jsonify, request
from service.twitch_service import TwitchService

point = Blueprint('point', __name__)


@point.route('/rewards', methods=['GET'])
def get_custom_rewards():

    access_token = request.args.get('access_token')
    broadID = request.args.get('broadID')

    if access_token is None:
        return jsonify({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    response = twitch_service.get_custom_rewards(broadID)

    if response is not None:
        return jsonify(response)
    else:
        return jsonify({'error': "Error"})


@point.route('/rewards-redemption', methods=['GET'])
def get_Rewards_Redemption():

    access_token = request.args.get('access_token')
    broadID = request.args.get('broadID')
    rewardID = request.args.get('rewardID')

    if access_token is None:
        return jsonify({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    response = twitch_service.rewards_redemption(broadID, rewardID)

    if response is not None:
        return jsonify(response)
    else:
        return jsonify({'error': "Error"})


@point.route('/rewards', methods=['POST'])
def create_custom_rewards():

    data = request.json
    access_token = data.get('access_token')
    broadID = data.get('broadID')
    del data['access_token']
    del data['broadID']
    if access_token is None:
        return jsonify({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)
    response = twitch_service.create_custom_rewards(broadID, data)

    if response is not None:
        return jsonify(response)
    else:
        return jsonify({'error': "Error"})


@point.route('/rewards/<rewardID>', methods=['DELETE'])
def delete_rewards(rewardID):

    access_token = request.args.get('access_token')
    broadID = request.args.get('broadID')

    if access_token is None:
        return jsonify({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    response = twitch_service.delete_rewards(broadID, rewardID)

    if response is not None:
        return response
    else:
        return jsonify({'error': "Error"})


@point.route('/rewards/<rewardID>', methods=['PATCH'])
def update_Reward(rewardID):

    data = request.json
    access_token = data.get('access_token')
    broadID = data.get('broadID')
    del data['access_token']
    del data['broadID']
    if access_token is None:
        return jsonify({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    response = twitch_service.update_Reward(broadID, rewardID, data)
    if response is not None:
        return response
    else:
        return jsonify({'error': "Error"})
