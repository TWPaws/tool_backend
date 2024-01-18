from flask import Flask
from controller.redemption_controller import redemption_route
from controller.user import user_route

app = Flask(__name__)

access_token = "zzphl0ev6dtb1v9heg7s9rpngvgh69"
broadcaster_id = "29127270"
app.register_blueprint(user_route, url_prefix='/user')
app.register_blueprint(redemption_route, url_prefix='/redemption')


@app.route('/')
def hello():
    return ('Hello World')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
