from flask import Blueprint, jsonify
from service.twitch_service import TwitchService

access_token = 'zzphl0ev6dtb1v9heg7s9rpngvgh69'
clientID = 'fhc0ko2asch2gf7ya4ame220yahpka'
broadcasterID = "29127270"
twitch_service = TwitchService(access_token, clientID)

redemption = Blueprint('redemption_route', __name__)


@redemption.route('/customRewards/broadcasterID', methods=['GET'])
def get_custom_rewards(broadcasterID):
    if access_token is None:
        return jsonify({'error': 'Access Token is required'}, 400)

    respones = twitch_service.get_custom_rewards(broadcasterID)

    if respones is not None:
        return jsonify(respones)
    else:
        return jsonify({'error': "Error"})


@redemption.route('/RewardRedemption/broadcasterID/rewardID', methods=['GET'])
def get_Rewards_Redemption(broadcasterID, rewardID):
    if access_token is None:
        return jsonify({'error': 'Access Token is required'}, 400)

    respones = twitch_service.rewards_redemption(broadcasterID, rewardID)

    if respones is not None:
        return jsonify(respones)
    else:
        return jsonify({'error': "Error"})


@redemption.route('/createRewards/broadcasterID/title/cost', methods=['POST'])
def create_custom_rewards(title, cost):
    if access_token is None:
        return jsonify({'error': 'Access Token is required'}, 400)

    respones = twitch_service.create_custom_rewards(broadcasterID, title, cost)

    if respones is not None:
        return jsonify(respones)
    else:
        return jsonify({'error': "Error"})


@redemption.route('/deleteRewards/broadcasterID/rewardID', methods=['DELETE'])
def delete_rewards(broadcasterID, rewardID):
    if access_token is None:
        return jsonify({'error': 'Access Token is required'}, 400)

    respones = twitch_service.delete_rewards(broadcasterID, rewardID)

    if respones is not None:
        return jsonify(respones)
    else:
        return jsonify({'error': "Error"})


@redemption.route('/updateReward/broadID/rewardID/cost', methods=['PATCH'])
def update_Reward(broadcasterID, rewardID, cost):
    if access_token is None:
        return jsonify({'error': 'Access Token is required'}, 400)

    respones = twitch_service.update_Reward(broadcasterID, rewardID, cost)

    if respones is not None:
        return jsonify(respones)
    else:
        return jsonify({'error': "Error"})
