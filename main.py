from flask import Flask
from controller.redemption_controller import point
from controller.user import user
from flask_cors import CORS
from flasgger import Swagger
from flask_login import LoginManager

app = Flask(__name__)

app.config['SWAGGER'] = {
    "title": "圖奇後端管理API",
    "version": "1.0.0",
    "hide_top_bar": True
}

app.secret_key = b'c1798eb7bba563e1409fc6d404d98f70a8f22c1e177599849524fb851efa34a7'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"
login_manager.login_view = 'login'
login_manager.login_message = '請先登入才可使用網頁 謝謝'

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(point, url_prefix='/redemption')

CORS(app)
Swagger(app)


@app.route('/')
def hello():
    return ('Hello World')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
