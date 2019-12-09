from flask import Flask, request, jsonify
import json
import os
import uuid
import uuid

from model.redis_storage import Redis_storage
from model.auth import Auth_Model
from youtube import Youtube_Downloader
from queue import Queue
from threading import Thread, Lock

youtube_model = Redis_storage()
youtube_downloader = Youtube_Downloader()
youtube_queue = Queue()

def auth_check(token):
    cek = Auth_Model().check_token(token)
    if (cek is None):
        return {'STATUS': 'Error Authentication'}
    return None

def get_auth_data(token):
    return Auth_Model().check_token(token)

def youtube_list():
    token = request.headers.get('Authorization') or ''
    if (auth_check(token) is not None):
        return auth_check(token), 404

    user_data = get_auth_data(token)
    videos = []
    pb_data = youtube_model.list()
    for data in pb_data:
        for d, v in data.items():
            v = json.loads(v)
            if v['username'] == user_data['username']:
                videos.append({
                    'link' : v['link']
                })

    return jsonify(status='OK',data=videos), 200

def youtube_file(uid):
    pb_data = youtube_model.get(uid)
    return pb_data

def youtube_add(requests):
    token = request.headers.get('Authorization') or ''
    if (auth_check(token) is not None):
        return auth_check(token), 404

    if 'link' in requests:
        username = get_auth_data(token)['username']
        uid = uuid.uuid1()
        youtube_queue.put({
            'username' : username,
            'request' : requests,
            'id' : uid
        })
        resolution = ''
        extension = ''
        if 'resolution' in requests:
            res, resolutions = youtube_downloader.get_resolution(requests["link"])
            if requests["resolution"] not in resolutions:
                return jsonify(status='Resolution not available, available : {}'.format(resolutions)), 400
            else:
                resolution = requests["resolution"]

        if 'extension' in requests:
            res, extensions = youtube_downloader.get_type(requests["link"])
            if 'video/'+requests["extension"] not in extensions:
                return jsonify(status='Extension not available, available : {}'.format(extensions)), 400
            else:
                extension = requests["extension"]

        res, path = youtube_downloader.download(link = requests["link"], quality=resolution, extension=extension)
        if res:
            requests['filename'] = path
            requests['username'] = get_auth_data(token)['username']
            pb_data = youtube_model.add(requests)
            size = os.path.getsize(path)

            users_data = youtube_model.list("users")
            res = []
            for user in users_data:
                user = json.loads(user)
                if user['username'] == username:
                    user["usage"] = user["usage"] + size
                res.append(user)
            ok = youtube_model.remove('users')
            ok = youtube_model.update(key='users', data= res)
            return jsonify(status='OK',data=pb_data), 200
        else:
            return jsonify(status='Failed Download Video'), 400
    return jsonify(status='Request not completed'), 501

def youtube_delete(id):
    pb_data = youtube_model.remove(id)
    return jsonify(status='OK',data=pb_data), 200

def youtube_flush():
    pb_data = youtube_model.empty()
    return jsonify(status='OK',data=pb_data), 200

def job_download_video():
    data = youtube_queue.get()
    requests = data["request"]
    uid = data["uid"]
    username = data["username"]
    res, path = youtube_downloader.download(link = requests["link"])
    if res:
        requests['filename'] = path
        requests['username'] = username
        pb_data = youtube_model.add_video(requests, uid)
        size = os.path.getsize(path)

        users_data = youtube_model.list("users")
        res = []
        for user in users_data:
            user = json.loads(user)
            if user['username'] == username:
                user["usage"] = user["usage"] + size
            res.append(user)
        ok = youtube_model.remove('users')
        ok = youtube_model.update(key='users', data= res)
        return 'ok'
    return 'not ok'