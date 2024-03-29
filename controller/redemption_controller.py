# ./controller/redemption_controller.py
from flask import Blueprint, request
from service.twitch_service import TwitchService
from flask_login import LoginManager, login_required, current_user

point = Blueprint('point', __name__)


@point.route('/rewards', methods=['GET'])
@login_required
def get_custom_rewards():

    """
    Get All custom rewards List
    Return detailed information of all custom points created within this application
    ---
    tags:
      - redemption_controller
    produces: application/json,
    parameters: []
    responses:
      401:
        description: Unauthorized error or not logged in. Please authenticate
      200:
        description: Retrieve custom rewards list
        examples:
            node-list: [{
                "data": [
                    {
                        "broadcaster_name": "torpedo09",
                        "broadcaster_login": "torpedo09",
                        "broadcaster_id": "274637212",
                        "id": "afaa7e34-6b17-49f0-a19a-d1e76eaaf673",
                        "image": null,
                        "background_color": "#00E5CB",
                        "is_enabled": true,
                        "cost": 50000,
                        "title": "game analysis 1v1",
                        "prompt": "",
                        "is_user_input_required": false,
                        "max_per_stream_setting": {
                          "is_enabled": false,
                          "max_per_stream": 0
                        },
                        "max_per_user_per_stream_setting": {
                          "is_enabled": false,
                          "max_per_user_per_stream": 0
                        },
                        "global_cooldown_setting": {
                          "is_enabled": false,
                          "global_cooldown_seconds": 0
                        },
                        "is_paused": false,
                        "is_in_stock": true,
                        "default_image": {
                          "url_1x": "https://static-cdn.jtvnw.net/custom-reward-images/default-1.png",
                          "url_2x": "https://static-cdn.jtvnw.net/custom-reward-images/default-2.png",
                          "url_4x": "https://static-cdn.jtvnw.net/custom-reward-images/default-4.png"
                        },
                        "should_redemptions_skip_request_queue": false,
                        "redemptions_redeemed_current_stream": null,
                        "cooldown_expires_at": null
                        }
                    ]
            }]
    """

    access_token = current_user.get_access_token()
    broadcaster_id = current_user.get_broadcaster_id()

    if access_token is None:
        return ({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    response = twitch_service.get_custom_rewards(broadcaster_id)

    if response is not None:
        return (response)
    else:
        return ({'error': "Error"})


@point.route('/rewards-redemption', methods=['GET'])
@login_required
def get_Rewards_Redemption():

    """
    get rewards Redemption List
    Return the current redemption list for a specific loyalty point
    ---
    tags:
      - redemption_controller
    produces: application/json
    parameters:
      - name: rewardID
        in: path
        type: string
        required: true
    responses:
      401:
        description: Unauthorized error or not logged in. Please authenticate
      200:
        description: Retrieve custom reward redemption list
        examples: |
          {
              "data": [
                  {
                    "broadcaster_name": "torpedo09",
                    "broadcaster_login": "torpedo09",
                    "broadcaster_id": "274637212",
                    "id": "17fa2df1-ad76-4804-bfa5-a40ef63efe63",
                    "user_login": "torpedo09",
                    "user_id": "274637212",
                    "user_name": "torpedo09",
                    "user_input": "",
                    "status": "CANCELED",
                    "redeemed_at": "2020-07-01T18:37:32Z",
                    "reward": {
                      "id": "92af127c-7326-4483-a52b-b0da0be61c01",
                      "title": "game analysis",
                      "prompt": "",
                      "cost": 50000
                    }
                  }
              ],
                  "pagination": {
                     "cursor": "eyJiIjpudWxsLCJRTFOMW89In19..."
              }
          }
    """

    access_token = current_user.get_access_token()
    broadcaster_id = current_user.get_broadcaster_id()
    rewardID = request.args.get('rewardID')

    if access_token is None:
        return ({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    response = twitch_service.rewards_redemption(broadcaster_id, rewardID)

    if response is not None:
        return ("Success")
    else:
        return ({'error': "Unauthorized error or not logged in. Please authenticate "})


@point.route('/rewards', methods=['POST'])
@login_required
def create_custom_rewards():

    """
    create custom rewards
    Used to create new points
    ---
    tags:
      - redemption_controller
    produces: application/json
    parameters:
      - name: title
        in: body
        type: string
        required: true
      - name: cost
        in: body
        type: int64
        required: true
      - name: prompt
        in: body
        type: string
        required: false
      - name: is_enabled
        in: body
        type: boolean
        required: false
      - name: background_color
        in: body
        type: string
        required: false
      - name: is_user_input_required
        in: body
        type: boolean
        required: false
      - name: is_max_per_stream_enabled
        in: body
        type: boolean
        required: false
      - name: max_per_stream
        in: body
        type: integer
        required: false
      - name: is_max_per_user_per_stream_enabled
        in: body
        type: boolean
        required: false
      - name: max_per_user_per_stream
        in: body
        type: integer
        required: false
      - name: is_global_cooldown_enabled
        in: body
        type: boolean
        required: false
      - name: global_cooldown_seconds
        in: body
        type: integer
        required: false
      - name: should_redemptions_skip_request_queue
        in: body
        type: boolean
        required: false
    responses:
      401:
        description: Unauthorized error or not logged in. Please authenticate
      200:
        description: Retrieve custom reward redemption list
        examples: |
          {
            "data": [
                {
                    "broadcaster_name": "torpedo09",
                    "broadcaster_login": "torpedo09",
                    "broadcaster_id": "274637212",
                    "id": "17fa2df1-ad76-4804-bfa5-a40ef63efe63",
                    "user_login": "torpedo09",
                    "user_id": "274637212",
                    "user_name": "torpedo09",
                    "user_input": "",
                    "status": "CANCELED",
                    "redeemed_at": "2020-07-01T18:37:32Z",
                    "reward": {
                      "id": "92af127c-7326-4483-a52b-b0da0be61c01",
                      "title": "game analysis",
                      "prompt": "",
                      "cost": 50000
                    }
                }
            ],
                "pagination": {
                    "cursor": "eyJiIjpudWxsLCJRTFOMW89In19..."
            }
          }
    """
    access_token = current_user.get_access_token()
    broadcaster_id = current_user.get_broadcaster_id()
    data = request.json
    if access_token is None:
        return ({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)
    response = twitch_service.create_custom_rewards(broadcaster_id, data)

    if response is not None:
        return (response)
    else:
        return ({'error': "Error"})


@point.route('/rewards/<rewardID>', methods=['DELETE'])
@login_required
def delete_rewards(rewardID):

    """
    Delete custom rewards
    Used to delete points for a specific ID
    ---
    tags:
      - redemption_controller
    produces: application/json
    parameters:
      - name: rewardID
        in: body
        type: string
        required: true
    responses:
      401:
        description: Unauthorized error or not logged in. Please authenticate
      200:
        description: delete custom rewards list
        examples: "Success"
    """

    access_token = current_user.get_access_token()
    broadcaster_id = current_user.get_broadcaster_id()
    rewardID = request.args.get('rewardID')

    if access_token is None:
        return ({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    response = twitch_service.delete_rewards(broadcaster_id, rewardID)

    if response is not None:
        return response
    else:
        return ({'error': "Error"})


@point.route('/rewards/<rewardID>', methods=['PATCH'])
@login_required
def update_Reward(rewardID):

    """
    Update custom rewards List
    Used to modify redemption point information for a specific ID
    ---
    tags:
      - redemption_controller
    produces: application/json
    parameters:
      - name: rewardID
        in: body
        type: string
        required: true
      - name: title
        in: body
        type: string
        required: false
      - name: cost
        in: body
        type: int64
        required: false
      - name: prompt
        in: body
        type: string
        required: false
      - name: is_enabled
        in: body
        type: boolean
        required: false
      - name: background_color
        in: body
        type: string
        required: false
      - name: is_user_input_required
        in: body
        type: boolean
        required: false
      - name: is_max_per_stream_enabled
        in: body
        type: boolean
        required: false
      - name: max_per_stream
        in: body
        type: integer
        required: false
      - name: is_max_per_user_per_stream_enabled
        in: body
        type: boolean
        required: false
      - name: max_per_user_per_stream
        in: body
        type: integer
        required: false
      - name: is_global_cooldown_enabled
        in: body
        type: boolean
        required: false
      - name: global_cooldown_seconds
        in: body
        type: integer
        required: false
      - name: should_redemptions_skip_request_queue
        in: body
        type: boolean
        required: false
    responses:
      401:
        description: Unauthorized error or not logged in. Please authenticate
      200:
        description: modify custom rewards list
        examples: "Success"
    """

    access_token = current_user.get_access_token()
    broadcaster_id = current_user.get_broadcaster_id()
    data = request.json
    if access_token is None:
        return ({'error': 'Access Token is required'}, 400)

    twitch_service = TwitchService(access_token)

    response = twitch_service.update_Reward(broadcaster_id, rewardID, data)
    if response is not None:
        return response
    else:
        return ({'error': "Error"})