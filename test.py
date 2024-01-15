from flask import Flask,jsonify,request
import requests

app = Flask(__name__)

access_token = "zzphl0ev6dtb1v9heg7s9rpngvgh69"
broadcaster_id = "29127270"

@app.route('/')
def hello():
    authorization_code = request.url
    # 在这里处理授权码，例如交换令牌等
    print(type(authorization_code))
    print(authorization_code)
    return f'test'

@app.route('/callback')
def callback():
    authorization_code = request.args.get('code')
    # 在这里处理授权码，例如交换令牌等
    return f'Authorization Code: {authorization_code}'

@app.route('/getBroadcasterId')
def get_broadcaster_id():

    if not access_token:
        return jsonify({'error': 'Access Token is required'}), 400

    endpoint = "https://api.twitch.tv/helix/users"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Client-ID": "fhc0ko2asch2gf7ya4ame220yahpka"  # 请用你的 Twitch 应用程序的 Client ID 替换
    }

    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        user_data = response.json()

        broadcaster_id = user_data["data"][0]["id"]
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
