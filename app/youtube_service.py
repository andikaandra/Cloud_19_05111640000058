from flask import Flask, request, jsonify
import json
import os
import uuid

from model.redis_storage import Redis_storage
from model.auth import Auth_Model
from youtube import Youtube_Downloader

youtube_model = Redis_storage()
youtube_downloader = Youtube_Downloader()

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

def youtube_file(uid):
    pb_data = youtube_model.get(uid)
    return pb_data

def youtube_add(requests):
    token = request.headers.get('Authorization') or ''
    if (auth_check(token) is not None):
        return auth_check(token), 404

    if 'link' in requests:
        res, path = youtube_downloader.download(link = requests["link"])
        if res:
            requests['filename'] = path
            pb_data = youtube_model.add(requests)
            return jsonify(status='OK',data=pb_data), 200
        else:
            return jsonify(status='Failed Download Video'), 204
    return jsonify(status='Request not completed'), 501

def youtube_delete(id):
    pb_data = youtube_model.remove(id)
    return jsonify(status='OK',data=pb_data), 200
