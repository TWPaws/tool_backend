# ./service/twitch_service.py

import requests as req
from flask import jsonify


class TwitchService:
    Protocol = 'https://api.twitch.tv/helix/'

    def __init__(self, access_token):
        self.access_token = access_token
        self.client_id = 'ecmnwqtzoa9c67bhtjunt7ne2vrog0'

    def get_broadcaster_id(self):
        headers = {
            "Authorization": f'Bearer {self.access_token}',
            "Client-ID": self.client_id
        }
        Query = 'users'
        response = req.get(self.Protocol + Query, headers=headers)

        if response.status_code == 200:
            user_data = response.json()

            return jsonify({'broadcaster_id': user_data["data"][0]["id"], 'display_name': user_data["data"][0]["display_name"]})
        else:
            return None

    def get_custom_rewards(self, broadcaster_id):
        headers = {
            "Authorization": f'Bearer {self.access_token}',
            "Client-ID": self.client_id
        }
        Path = 'channel_points/custom_rewards?'
        Query = f'broadcaster_id={broadcaster_id}&only_manageable_rewards=True'
        response = req.get(
            self.Protocol + Path + Query,
            headers=headers
        )
        if response.status_code == 200:
            while 'cursor' in response.json().get('pagination', {}):
                cursor = response['pagination']['cursor']
                Path = 'streams?'
                Query = f'first=20&after={cursor}'
                response += req.get(
                    self.Protocol + Path + Query,
                    headers=headers
                )
            return (response.json())
        else:
            return None

    def rewards_redemption(self, broadcaster_id, reward_id):
        headers = {
            "Authorization": f'Bearer {self.access_token}',
            "Client-ID": self.client_id
        }

        Path = 'channel_points/custom_rewards/redemptions?'
        Query = (
            f'broadcaster_id={broadcaster_id}&'
            f'reward_id={reward_id}&'
            f'status=UNFULFILLED'
        )

        response = req.get(
            self.Protocol + Path + Query,
            headers=headers
        )

        if response.status_code == 200:
            reward_fulfill_data = response.json()

            return (reward_fulfill_data)
        else:
            return None

    def create_custom_rewards(self, broadcaster_id, data):
        headers = {
            'Client-ID': self.client_id,
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        Query = f'channel_points/custom_rewards?broadcaster_id={broadcaster_id}'
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

    def delete_rewards(self, broadcaster_id, reward_id):
        headers = {
            'Client-ID': self.client_id,
            'Authorization': f'Bearer {self.access_token}',
        }

        Path = 'channel_points/custom_rewards?'
        Query = f'broadcaster_id={broadcaster_id}&id={reward_id}'

        response = req.delete(self.Protocol + Path + Query, headers=headers)

        if response.status_code == 204:
            return ({'status': 'success'})
        else:
            return None

    def update_Reward(self, broadcaster_id, reward_id, data):
        headers = {
            'Client-ID': 'fhc0ko2asch2gf7ya4ame220yahpka',
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        Path = 'channel_points/custom_rewards'
        Query = f'?broadcaster_id={broadcaster_id}&id={reward_id}'

        response = req.patch(
            self.Protocol + Path + Query,
            headers=headers,
            json=data
        )
        if response.status_code == 200:
            return response.json()
        else:
            return None
