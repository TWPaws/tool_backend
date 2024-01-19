from flask import Blueprint, jsonify, request
from service.twitch_service import TwitchService

point = Blueprint('redemption_route', __name__)


@point.route('/customRewards', methods=['GET'])
def get_custom_rewards(access_token, broadID):

    access_token = request.args.get('access_token')
    broadID = request.args.get('broadID')

    if access_token is None:
        return jsonify({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    respones = twitch_service.get_custom_rewards(broadID)

    if respones is not None:
        return jsonify(respones)
    else:
        return jsonify({'error': "Error"})


@point.route('/rewardRedemption', methods=['GET'])
def get_Rewards_Redemption():

    access_token = request.args.get('access_token')
    broadID = request.args.get('broadID')
    rewardID = request.args.get('rewardID')

    if access_token is None:
        return jsonify({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    respones = twitch_service.rewards_point(broadID, rewardID)

    if respones is not None:
        return jsonify(respones)
    else:
        return jsonify({'error': "Error"})


@point.route('/createRewards', methods=['POST'])
def create_custom_rewards():

    data = request.json
    data_as_list = list(data.values())
    access_token = data_as_list.pop()
    broadID = data_as_list.pop()
    if access_token is None:
        return jsonify({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    respones = twitch_service.create_custom_rewards(broadID, data_as_list)

    if respones is not None:
        return jsonify(respones)
    else:
        return jsonify({'error': "Error"})


@point.route('/deleteRewards', methods=['DELETE'])
def delete_rewards():

    data = request.json
    data_as_list = list(data.values())
    access_token = data_as_list.pop()
    broadID = data_as_list.pop()
    rewardID = data_as_list.pop()

    if access_token is None:
        return jsonify({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    respones = twitch_service.delete_rewards(broadID, rewardID)

    if respones is not None:
        return jsonify(respones)
    else:
        return jsonify({'error': "Error"})


@point.route('/updateRewardt', methods=['PATCH'])
def update_Reward():

    data = request.json
    data_as_list = list(data.values())
    access_token = data_as_list.pop()
    broadID = data_as_list.pop()
    rewardID = data_as_list.pop()

    if access_token is None:
        return jsonify({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    respones = twitch_service.update_Reward(broadID, rewardID, data_as_list)

    if respones is not None:
        return jsonify(respones)
    else:
        return jsonify({'error': "Error"})
