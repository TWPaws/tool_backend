from flask import app, request, jsonify
import requests
from service.twitch_service import TwitchService

access_token = None
client_id = 'fhc0ko2asch2gf7ya4ame220yahpka'
twitch_service = TwitchService(access_token, client_id)

# Twitch OAuth2.0 callback URL
@app.route('/callback')
def callback():
    access_token = request.args.get('code')
    return f'Authorization Code: {access_token}'

@app.route('/broadcasters', methods=['GET'])
def get_broadcaster_id():
    if access_token is None:
        return jsonify({'error': 'Access Token is required'}), 400

    broadcaster_id = twitch_service.get_broadcaster_id(access_token, client_id)
    if broadcaster_id is not None:
        return jsonify({'broadcaster_id': broadcaster_id})
    else:
        return jsonify({'error': f"Error: {response.status_code}, {response.text}"}), response.status_code









@app.route('/getCustomRewards')
def get_custom_rewards():
    
    if not access_token:
        return jsonify({'error': 'Access Token is required'}), 400

    broadcaster_id = "29127270"
    endpoint = f'https://api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id={broadcaster_id}'

    headers = {
        'Client-ID': 'fhc0ko2asch2gf7ya4ame220yahpka',
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(endpoint,headers=headers)

    if response.status_code == 200:
        user_data = response.json()

        broadcaster_id = user_data["data"][0]["id"]
        return jsonify(user_data)
    else:
        return jsonify({'error': f"Error: {response.status_code}, {response.text}"}), response.status_code

@app.route('/getCustomRewardRedemption')
def get_Custom_Rewards_Redemption():
    
    if not access_token:
        return jsonify({'error': 'Access Token is required'}), 400
    
    broadcaster_id = "29127270"
    endpoint = f'https://api.twitch.tv/helix/channel_points/custom_rewards/redemptions?broadcaster_id={broadcaster_id}&reward_id=abccbb16-adcc-4fc9-9579-a96b9be431ce&status=UN FULFILLED'

    headers = {
        'Client-ID': 'fhc0ko2asch2gf7ya4ame220yahpka',
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(endpoint,headers=headers)

    if response.status_code == 200:
        user_data = response.json()

        return jsonify(user_data)
    else:
        return jsonify({'error': f"Error: {response.status_code}, {response.text}"}), response.status_code

@app.route('/createCustomRewards')
def create_custom_rewards():
    
    if not access_token:
        return jsonify({'error': 'Access Token is required'}), 400

    broadcaster_id = "29127270"
    endpoint = f'https://api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id={broadcaster_id}'

    headers = {
        'Client-ID': 'fhc0ko2asch2gf7ya4ame220yahpka',
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    data = {
        "title": "API_test1",
        "cost": 100
    }
    
    response = requests.post(endpoint,headers=headers,json=data)

    if response.status_code == 200:
        user_data = response.json()

        broadcaster_id = user_data["data"][0]["id"]
        return jsonify({'broadcaster_id': broadcaster_id})
    else:
        return jsonify({'error': f"Error: {response.status_code}, {response.text}"}), response.status_code

@app.route('/deleteCustomRewards')
def delete_custom_rewards():

    if not access_token:
        return jsonify({'error': 'Access Token is required'}), 400

    broadcaster_id = "29127270"
    reward_id = "abccbb16-adcc-4fc9-9579-a96b9be431ce"

    endpoint = f"https://api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id={broadcaster_id}&id={reward_id}"

    headers = {
        'Client-ID': 'fhc0ko2asch2gf7ya4ame220yahpka',
        'Authorization': f'Bearer {access_token}',
    }

    response = requests.delete(endpoint, headers=headers)

    if response.status_code == 200:
        user_data = response.json()

        broadcaster_id = user_data["data"][0]["id"]
        return jsonify({'broadcaster_id': broadcaster_id})
    else:
        return jsonify({'error': f"Error: {response.status_code}, {response.text}"}), response.status_code

@app.route('/updateCustomReward')
def update_Custom_Reward():

    if not access_token:
        return jsonify({'error': 'Access Token is required'}), 400

    broadcaster_id = "29127270"
    reward_id = "abccbb16-adcc-4fc9-9579-a96b9be431ce"

    endpoint = f"https://api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id={broadcaster_id}&id={reward_id}"

    headers = {
        'Client-ID': 'fhc0ko2asch2gf7ya4ame220yahpka',
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    data = {
        "cost": 200
    }

    response = requests.patch(endpoint, headers=headers,json=data)

    if response.status_code == 200:
        user_data = response.json()

        return jsonify(user_data)
    else:
        return jsonify({'error': f"Error: {response.status_code}, {response.text}"}), response.status_code