# ./controller/user.py
from flask import Blueprint, request
from service.twitch_service import TwitchService
from service.Oauth20 import get_access_token
from repo.user_operations import add_user, search_user

user = Blueprint('user', __name__)


@user.route('/broadcasters', methods=['GET'])
def get_broadcaster_id():

    """
    get broadcaster id
    Return the user's broadcaster_id by sending a request to the Twitch API using an API
    ---
    tags:
      - user
    produces: application/json
    parameters: []
    responses:
      401:
        description: Unauthorized error or not logged in. Please authenticate
      200:
        description: Retrieve user's broadcaster_id and display name
        examples: |
          {
              "data": [
                  {
                    "broadcaster_id": "274637212",
                    "display_name": "torpedo09",
                    }
                  }
              ]
          }
    """

    access_token = request.args.get('access_token')

    if access_token is None:
        return ({'error': 'Access Token is required'})

    twitch_service = TwitchService(access_token)

    response = twitch_service.get_broadcaster_id()
    if response is not None:
        return response
    else:
        return 'False'


@user.route('/twitch_callback/', methods=['POST'])
def twitch_callback():

    """
    Receive and retrieve the authorization code from OAuth 2.0 to create an account
    As the Authorization code grant flow is used, after the user confirms authorization,
    redirect back to this link and use the authorization code to retrieve the user's credentials from the OAuth API,
    then store them in the database to create an account
    ---
    tags:
      - user
    produces: application/json
    parameters:
      - name: code
        in: bdoy
        type: string
        required: true
      - name: user_data
        in: body
        type: array
        required: true
    responses:
      401:
        description: Unauthorized error or not logged in. Please authenticate
      200:
        description: Sign Up sccuess
        examples: "Sign up successfully"
    """

    data = request.json
    code = data.get('code')
    user_data = data.get('user_data')

    print("Received code:", code)

    access_token = get_access_token(code)
    add_user(user_data, access_token)

    return 'Sign up successfully'

@register.route('/register', methods=['POST'])
def show():
    access_token = request.form['access_token']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm-password']

    if username and email and password and confirm_password:
        if password == confirm_password:
            hashed_password = generate_password_hash(
                password, method='sha256')
            if search_user(username, password):
              return ({'status': 'Username or password already exists. Please modify again'}), 400
              add_user(access_token, username, email, hashed_password)
              return ({'status': 'success'}), 200
    else:
        return ({'status': 'fail'}), 400

