from flask import Flask, request, jsonify
import json
import os

from model.redis_storage import Redis_storage
from model.auth import Auth_Model
from youtube import Youtube_Downloader

redis_addr = os.getenv("REDISADDR") or "localhost"
youtube_model = Redis_storage(address=redis_addr)
youtube_downloader = Youtube_Downloader()
storage_path = youtube_downloader.path

def auth_check(token):
    cek = Auth_Model().check_token(token)
    if (cek is None):
        return {'STATUS': 'Error Authentication'}
    return None

def youtube_list():
    token = request.headers.get('Authorization') or ''
    if (auth_check(token) is not None):
        return auth_check(token), 404

    pb_data = youtube_model.list()
    return jsonify(status='OK',data=pb_data), 200

def youtube_add(requests):
    token = request.headers.get('Authorization') or ''
    if (auth_check(token) is not None):
        return auth_check(token), 404

    if 'link' in requests:
        youtube_downloader.download(link = requests["link"])
        requests['path'] = storage_path
        pb_data = youtube_model.add(requests)
        return jsonify(status='OK',data=pb_data), 200

    return jsonify(status='Request not completed'), 501

def youtube_delete(id):
    pb_data = youtube_model.remove(id)
    return jsonify(status='OK',data=pb_data), 200
