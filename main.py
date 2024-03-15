from flask import Flask
from controller.redemption_controller import point
from controller.user import user
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)

app.config['SWAGGER'] = {
    "title": "圖奇後端管理API",
    "version": "1.0.0",
    "hide_top_bar": True
}

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(point, url_prefix='/redemption')

CORS(app)
Swagger(app)


@app.route('/')
def hello():
    return ('Hello World')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
