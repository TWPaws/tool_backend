from flask import Flask
from controller.redemption_controller import point
from controller.user import user
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(point, url_prefix='/redemption')


@app.route('/')
def hello():
    return ('Hello World')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
