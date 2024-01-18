import requests as req
from flask import jsonify


class TwitchService:
    Protocol = 'https://api.twitch.tv/helix/'

    def __init__(self, access_token, client_id):
        self.access_token = access_token
        self.client_id = client_id

    def get_broadcasterID(self):
        headers = {
            "Authorization": f'Bearer {self.access_token}',
            "Client-ID": self.client_id
        }
        Query = 'users'
        response = req.get(self.Protocol + Query, headers=headers)

        if response.status_code == 200:
            user_data = response.json()

            broadcasterID = user_data["data"][0]["id"]
            return jsonify(broadcasterID)
        else:
            return None

    def get_custom_rewards(self, broadcasterID):
        headers = {
            "Authorization": f'Bearer {self.access_token}',
            "Client-ID": self.client_id
        }
        Query = f'channel_points/custom_rewards?broadcasterID={broadcasterID}'
        response = req.get(
            self.Protocol + Query,
            headers=headers
        )

        if response.status_code == 200:
            reward_data = response.json()

            return jsonify(reward_data)
        else:
            return None

    def rewards_redemption(self, broadID, rewardID):
        headers = {
            "Authorization": f'Bearer {self.access_token}',
            "Client-ID": self.client_id
        }
        Path = '/channel_points/custom_rewards/redemptions?'
        Query = f'broadcasterID={broadID}&rewardID={rewardID}&status=FULFILLED'
        response = req.get(
            self.Protocol + Query + Path,
            headers=headers
        )

        if response.status_code == 200:
            reward_fulfill_data = response.json()

            return jsonify(reward_fulfill_data)
        else:
            return None

    def create_custom_rewards(self, broadcasterID, title, cost):
        headers = {
            'Client-ID': self.client_id,
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        data = {
            "title": title,
            "cost": cost
        }

        Query = f'channel_points/custom_rewards?broadcasterID={broadcasterID}'
        response = req.post(
            self.Protocol + Query,
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            create_state = response.json()

            broadcasterID = create_state["data"][0]["id"]
            return jsonify({'Reward_id': broadcasterID})
        else:
            return None

    def delete_rewards(self, broadID, rewardID):
        headers = {
            'Client-ID': self.client_id,
            'Authorization': f'Bearer {self.access_token}',
        }

        Path = 'channel_points/custom_rewards?'
        Query = f'broadcasterID={broadID}&id={rewardID}'

        response = req.delete(self.Protocol + Path + Query, headers=headers)

        if response.status_code == 200:
            return jsonify('success')
        else:
            return None

    def update_Reward(self, broadcasterID, rewardID, cost):
        headers = {
            'Client-ID': 'fhc0ko2asch2gf7ya4ame220yahpka',
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        data = {
            "cost": int(cost)
        }

        Path = 'channel_points/custom_rewards'
        Query = f'?broadcasterID={broadcasterID}&id={rewardID}'

        response = req.patch(
            self.Protocol + Path + Query,
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            return jsonify('success')
        else:
            return None
