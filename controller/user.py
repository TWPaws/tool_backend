# ./controller/user.py
from flask import Blueprint, request
from service.twitch_service import TwitchService
from service.Oauth20 import get_access_token
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from repo.user_operations import add_user, search_user_password, update_access_toekn, search_user_id
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from controller.user_model import Users

user = Blueprint('user', __name__)
login_manager = LoginManager()
login_manager.init_app(user)


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

    access_token = request.args.get('access_token')

    if access_token is None:
        return ({'status': '?error=Access Token is required'})

    twitch_service = TwitchService(access_token)

    response = twitch_service.get_broadcaster_id()
    if response is not None:
        return ({'status': '?success=access Token receive', 'response': response}), 200
    else:
        return ({'status': '?error = error'}), 404


@user.route('/twitch_callback/', methods=['POST'])
@login_required
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
        in: body
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
    username = current_user.username

    print("Received code:", code)

    access_token = get_access_token(code)
    update_access_toekn(username, access_token)

    return ({'status': 'Sign up successfully'}), 200


@user.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm-password']

    if username and email and password and confirm_password:
        if password == confirm_password:
            hashed_password = generate_password_hash(
                password, method='pbkdf2:sha256')
            if search_user_password(username, password):
                return ({'status': '?error=Username or hash_password already exists. Please modify again'}), 400
            else:
                add_user(username, email, hashed_password)
                return ({'status': '?success=account create success'}), 200
    else:
        return ({'status': 'fail'}), 400


@user.route('/login', methods=['POST'])
def login():
    username = request.form('username')
    password = request.form('password')
    if username and password:
        user_data = search_user_password(username, password)
        user = Users(
          user_data['id'],
          user_data['username'],
          user_data['password'],
          user_data['email'],
          user_data['access_token'])
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return ({'status': '?success=login'}), 200
            else:
                return ({'status': '?error=incorrect-password'}), 400
        else:
            return ({'status': '?error=user-not-found'}), 400


@user.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return ({'status': '?success=logut'}), 200


@login_manager.user_loader
def load_user(user_id):
    user_data = search_user_id(user_id)
    user = Users(
          user_data['id'],
          user_data['username'],
          user_data['password'],
          user_data['email'],
          user_data['access_token'])
    return user
