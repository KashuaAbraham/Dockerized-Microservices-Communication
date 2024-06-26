from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "API-2: Use /call-api-1 to get response from API-1", 200

@app.route('/call-api-1', methods=['GET'])
def call_api_1():
    response = requests.get('http://api-1:5000/hello')
    return jsonify(response.text), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
