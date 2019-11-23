from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import auth_service
import youtube_service
import os

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def __get_response(response, code):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, code

@app.route('/auth', methods = ['POST'])
def route_auth():
    if request.method == 'POST':
        post_data = request.get_json(force=True)
        result, code = auth_service.auth(post_data)
        return __get_response(result, code)


@app.route('/youtube/list', methods = ['GET'])
def route_youtube_list():
    if request.method == 'GET':
        result, code = youtube_service.youtube_list()
        return __get_response(result, code)


@app.route('/youtube/add', methods = ['POST'])
def route_youtube_add():
    if request.method == 'POST':
        post_data = request.get_json(force=True)
        result, code = youtube_service.youtube_add(post_data)
        return __get_response(result, code)


if __name__ == "__main__":
    if not os.path.exists('storage'):
        os.makedirs('storage')
    app.run(host='0.0.0.0', port=5000)