import requests as req
from flask import jsonify


class TwitchService:
    Protocol = 'https://api.twitch.tv/helix/'

    def __init__(self, access_token):
        self.access_token = access_token
        self.client_id = 'fhc0ko2asch2gf7ya4ame220yahpka'

    def get_broadID(self):
        headers = {
            "Authorization": f'Bearer {self.access_token}',
            "Client-ID": self.client_id
        }
        Query = 'users'
        response = req.get(self.Protocol + Query, headers=headers)

        if response.status_code == 200:
            user_data = response.json()

            broadcasterID = user_data["data"][0]["id"]
            return jsonify({'broadcasterId': broadcasterID})
        else:
            return None

    def get_custom_rewards(self, broadcasterID):
        headers = {
            "Authorization": f'Bearer {self.access_token}',
            "Client-ID": self.client_id
        }
        Query = f'channel_points/custom_rewards?broadcaster_id={broadcasterID}&only_manageable_rewards=True'
        response = req.get(
            self.Protocol + Query,
            headers = headers
        )
        if response.status_code == 200:
            return (response.json())
        else:
            return None

    def rewards_redemption(self, broadID, rewardID):
        headers = {
            "Authorization": f'Bearer {self.access_token}',
            "Client-ID": self.client_id
        }

        Path = '/channel_points/custom_rewards/redemptions?'
        Query = (
            f'broadcasterID={broadID}&'
            f'rewardID={rewardID}&'
            f'status=UNFULFILLED'
        )

        response = req.get(
            self.Protocol + Query + Path,
            headers=headers
        )

        if response.status_code == 200:
            reward_fulfill_data = response.json()

            return jsonify(reward_fulfill_data)
        else:
            return None

    def create_custom_rewards(self, broadcasterID, data):
        headers = {
            'Client-ID': self.client_id,
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        Query = f'channel_points/custom_rewards?broadcaster_id={broadcasterID}'
        print(data)
        response = req.post(
            self.Protocol + Query,
            headers=headers,
            json=data
        )
        if response.status_code == 200:
            return (response.json())
        else:
            return None

    def delete_rewards(self, broadID, rewardID):
        headers = {
            'Client-ID': self.client_id,
            'Authorization': f'Bearer {self.access_token}',
        }

        Path = 'channel_points/custom_rewards?'
        Query = f'broadcaster_id={broadID}&id={rewardID}'

        response = req.delete(self.Protocol + Path + Query, headers=headers)

        if response.status_code == 204:
            return jsonify({'status' : 'success'})
        else:
            return None

    def update_Reward(self, broadcasterID, rewardID, data):
        headers = {
            'Client-ID': 'fhc0ko2asch2gf7ya4ame220yahpka',
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        Path = 'channel_points/custom_rewards'
        Query = f'?broadcaster_id={broadcasterID}&id={rewardID}'

        response = req.patch(
            self.Protocol + Path + Query,
            headers=headers,
            json=data
        )
        if response.status_code == 200:
            return response.json()
        else:
            return None
