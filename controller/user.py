# ./controller/user.py
from flask import Blueprint, request, redirect, current_app
from service.twitch_service import TwitchService
from service.Oauth20 import get_access_token, validate_access_token, refresh_access_token
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from repo.user_operations import add_user, search_user_by_username_password, search_user_by_username
from repo.user_operations import search_user_by_id, update_broadcaster_id, update_access_toekn
from model.user_model import User
import hashlib

user = Blueprint('user', __name__)
login_manager = LoginManager()


@user.route('/broadcasters', methods=['GET'])
@login_required
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

    access_token = current_user.access_token

    if access_token is None:
        return ({'error': 'Please connect to Twitch'}, 401)

    twitch_service = TwitchService(access_token)

    response = twitch_service.get_broadcaster_id()
    if response is not None:
        update_broadcaster_id(current_user.get_id(), response)
        return {'status': 'Broadcaster_id received and updated to database successfully', 'response': response}, 200
    else:
        return {'error': 'Failed to get broadcaster_id'}, 404


@user.route('/twitch_callback', methods=['GET'])
def twitch_callback():
    code = request.args.get('code')
    current_app.logger.debug("Received code:", code)

    user_id = current_user.get_id()

    data = get_access_token(code)
    access_token = data['access_token']
    refresh_token = data['refresh_token']
    update_access_toekn(user_id, access_token, refresh_token)

    return redirect('/')


@user.route('/register', methods=['POST'])
def register():
    data = request.json
    nickname = data.get('nickname')
    email = data.get('username')
    password = data.get('password')

    if nickname and email and password:
        if search_user_by_username(email):
            return {'error': 'User already exists'}, 401
        else:
            password = password.encode('utf-8')
            hash_password = hashlib.sha256(password).hexdigest()
            add_user(nickname, email, hash_password)
            return {'status': 'Success'}, 200
    else:
        return {'status': 'Registration failed'}, 400


@user.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    password = password.encode('utf-8')
    hash_password = hashlib.sha256(password).hexdigest()
    if username and hash_password:
        user_data = (search_user_by_username_password(username, hash_password))
        if user_data:
            user = User(
              user_data[0],
              user_data[1],
              user_data[2],
              user_data[3],
              user_data[4],
              user_data[5],
              user_data[6],
              user_data[7])
            login_user(user)
            if user.access_token is not None and validate_access_token(user.access_token):
                return {'status': 'Success'}, 200
            else:
                return {'status': 'You have not obtained an OAuth 2.0 access token or it has expired.\
                    Obtain a new one to use the service.'}, 200
        else:
            return {'error': 'User not found'}, 404


@user.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return {'status': 'Success'}, 200


@login_manager.user_loader
def load_user(user_id):
    user_data = search_user_by_id(user_id)
    user = User(
          user_data[0],
          user_data[1],
          user_data[2],
          user_data[3],
          user_data[4],
          user_data[5],
          user_data[6],
          user_data[7])
    return user


@user.route('/status', methods=['GET'])
@login_required
def status():
    if validate_access_token(current_user.access_token):
        nickname = current_user.nickname
        verified = current_user.verified
        return {
            'nickname': f'{nickname}',
            'verified': f'{verified}',
            'status': 'access_token is valid'}, 200
    else:
        data = refresh_access_token(current_user.refresh_token)
        if data:
            access_token = data['access_token']
            refresh_token = data['refresh_token']
            update_access_toekn(current_user.get_id(), access_token, refresh_token)
            token_valid = True

            return {
                'nickname': f'{nickname}',
                'verified': f'{verified}',
                'is token valid': f'{token_valid}',
                'status': 'access_token is valid'}, 200
        else:
            token_valid = False
            return {
                'nickname': f'{nickname}',
                'verified': f'{verified}',
                'is token valid': f'{token_valid}',
                'status': 'refresh token is invalid or ywou have not obtained an OAuth 2.0 access token '}, 200
