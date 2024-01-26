#./controller/redemption_controller.py
from flask import Blueprint, request
from service.twitch_service import TwitchService

point = Blueprint('point', __name__)


@point.route('/rewards', methods=['GET'])
def get_custom_rewards():

    access_token = request.args.get('access_token')
    broadcaster_id = request.args.get('broadcaster_id')

    if access_token is None:
        return ({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    response = twitch_service.get_custom_rewards(broadcaster_id)

    if response is not None:
        return (response)
    else:
        return ({'error': "Error"})


@point.route('/rewards-redemption', methods=['GET'])
def get_Rewards_Redemption():

    access_token = request.args.get('access_token')
    broadcaster_id = request.args.get('broadcaster_id')
    rewardID = request.args.get('rewardID')

    if access_token is None:
        return ({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    response = twitch_service.rewards_redemption(broadcaster_id, rewardID)

    if response is not None:
        return (response)
    else:
        return ({'error': "Error"})


@point.route('/rewards', methods=['POST'])
def create_custom_rewards():

    data = request.json
    access_token = data.get('access_token')
    broadcaster_id = data.get('broadcaster_id')
    del data['access_token']
    del data['broadcaster_id']
    if access_token is None:
        return ({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)
    response = twitch_service.create_custom_rewards(broadcaster_id, data)

    if response is not None:
        return (response)
    else:
        return ({'error': "Error"})


@point.route('/rewards/<rewardID>', methods=['DELETE'])
def delete_rewards(rewardID):

    access_token = request.args.get('access_token')
    broadcaster_id = request.args.get('broadcaster_id')

    if access_token is None:
        return ({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    response = twitch_service.delete_rewards(broadcaster_id, rewardID)

    if response is not None:
        return response
    else:
        return ({'error': "Error"})


@point.route('/rewards/<rewardID>', methods=['PATCH'])
def update_Reward(rewardID):

    data = request.json
    access_token = data.get('access_token')
    broadcaster_id = data.get('broadcaster_id')
    del data['access_token']
    del data['broadcaster_id']
    if access_token is None:
        return ({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    response = twitch_service.update_Reward(broadcaster_id, rewardID, data)
    if response is not None:
        return response
    else:
        return ({'error': "Error"})
