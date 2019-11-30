from flask import Flask, request, send_file, jsonify
from flask_cors import CORS, cross_origin
import json
import auth_service
import youtube_service
import os
import wget
from prometheus_flask_exporter import PrometheusMetrics
import redis

redis_addr = os.getenv("REDISADDR") or "localhost"

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['STORAGE'] = os.path.dirname(os.path.realpath(__file__)) + '/storage'

metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Application info', version='1.0.1')

path_counter = metrics.counter(
    'path_counter', 'Request count by request paths',
    labels={'path': lambda: request.path}
)

def __get_response(response, code):
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response, code

@app.route('/')
def main():
    return redis_addr, 200

# @app.route('/check-redis')
# def check_redis():
#     r = redis.Redis('localhost',port=6379,decode_responses=True)
#     return str(r.ping()), 200

@app.route('/auth', methods = ['POST'])
@path_counter
def route_auth():
    if request.method == 'POST':
        post_data = request.get_json(force=True)
        result, code = auth_service.auth(post_data)
        return __get_response(result, code)


@app.route('/register', methods = ['POST'])
def route_register():
    if request.method == 'POST':
        post_data = request.get_json(force=True)
        result, code = auth_service.register_user(post_data)
        return __get_response(result, code)

@app.route('/youtube/list', methods = ['GET'])
@path_counter
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

@app.route('/download/<uid>')
@path_counter
def route_download(uid):
    filename = youtube_service.youtube_file(uid)
    if filename:
        full_filename = os.path.join(app.config['STORAGE'], filename['filename'])
        if os.path.exists(full_filename):
            return send_file(full_filename, as_attachment=True)
    return __get_response(jsonify(status="Video Not found"), 500)


if __name__ == "__main__":
    if not os.path.exists('storage'):
        os.makedirs('storage')
    app.run(host='0.0.0.0', port=5000)