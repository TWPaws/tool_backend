# ./service/twitch_service.py

import requests as req
from flask import current_app
import config as cfg


class TwitchService:
    base_url = str(cfg.twitch_api)

    def __init__(self, access_token):
        self.access_token = access_token
        self.client_id = cfg.client_id

    def get_broadcaster_id(self):
        headers = {
            "Authorization": f'Bearer {self.access_token}',
            "Client-ID": self.client_id
        }
        query = 'users'
        response = req.get(self.base_url + query, headers=headers)

        if response.status_code == 200:
            user = response.json()

            return user["data"][0]["id"]
        else:
            return None

    def get_custom_rewards(self, broadcaster_id):
        headers = {
            "Authorization": f'Bearer {self.access_token}',
            "Client-ID": self.client_id
        }
        path = cfg.get_custom_reward
        query = f'?broadcaster_id={broadcaster_id}&only_manageable_rewards=True'
        response = req.get(
            self.base_url + path + query,
            headers=headers
        )
        if response.status_code == 200:
            while 'cursor' in response.json().get('pagination', {}):
                cursor = response['pagination']['cursor']
                path = 'streams?'
                query = f'first=20&after={cursor}'
                response += req.get(
                    self.base_url + path + query,
                    headers=headers
                )
            return response.json()
        else:
            return None

    def rewards_redemption(self, broadcaster_id, reward_id):
        headers = {
            "Authorization": f'Bearer {self.access_token}',
            "Client-ID": self.client_id
        }

        path = cfg.rewards_redemption
        query = (
            f'?broadcaster_id={broadcaster_id}&'
            f'reward_id={reward_id}&'
            f'status=UNFULFILLED'
        )

        response = req.get(
            self.base_url + path + query,
            headers=headers
        )

        if response.status_code == 200:
            reward_fulfill_data = response.json()

            return reward_fulfill_data
        else:
            return None

    def create_custom_rewards(self, broadcaster_id, data):
        headers = {
            'Client-ID': self.client_id,
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        path = cfg.create_custom_reward
        query = (
            f'?broadcaster_id={broadcaster_id}'
        )
        response = req.post(
            self.base_url + path + query,
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            return response.json()
        else:
            return None

    def delete_rewards(self, broadcaster_id, reward_id):
        headers = {
            'Client-ID': self.client_id,
            'Authorization': f'Bearer {self.access_token}',
        }

        path = cfg.delete_reward
        query = f'?broadcaster_id={broadcaster_id}&id={reward_id}'

        response = req.delete(self.base_url + path + query, headers=headers)
        current_app.logger.debug(response.text)

        if response.status_code == 204:
            return {'status': 'success'}
        else:
            return None

    def update_Reward(self, broadcaster_id, reward_id, data):
        headers = {
            'Client-ID': self.client_id,
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        path = cfg.update_reward
        query = f'?broadcaster_id={broadcaster_id}&id={reward_id}'

        response = req.patch(
            self.base_url + path + query,
            headers=headers,
            json=data
        )

        current_app.logger.debug(response.text)
        if response.status_code == 200:
            return response.json()
        else:
            return None
