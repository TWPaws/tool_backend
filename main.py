from flask import Flask,jsonify,request
import requests
from controller import 

app = Flask(__name__)

access_token = "zzphl0ev6dtb1v9heg7s9rpngvgh69"
broadcaster_id = "29127270"

@app.route('/')
def hello():
    authorization_code = request.url
    # 在这里处理授权码，例如交换令牌等
    print(type(authorization_code))
    print(authorization_code)
    return f'test'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)