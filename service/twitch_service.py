import requests

class TwitchService:
    endpoint = 'https://api.twitch.tv/helix/users'

    def __init__(self, access_token, client_id):
        self.access_token = access_token
        self.client_id = client_id

    def get_broadcaster_id(self, access_token, client_id):
        headers = {
            "Authorization": f'Bearer {access_token}',
            "Client-ID": client_id
        }

        response = requests.get(self.endpoint, headers=headers)

        if response.status_code == 200:
            user_data = response.json()

            broadcaster_id = user_data["data"][0]["id"]
            return broadcaster_id
        else:
            return None