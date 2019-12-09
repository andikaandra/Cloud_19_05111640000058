from flask import Flask,request,jsonify,make_response
from model.auth import Auth_Model
import json

def auth_check(token):
    cek = Auth_Model().check_token(token)
    if (cek is None):
        return {'STATUS': 'Error Authentication'}
    return None

def get_auth_data(token):
    return Auth_Model().check_token(token)

def auth(requests):
    data = requests
    username = data['username']
    password = data['password']
    a_model = Auth_Model()
    auth_result = a_model.login(username,password)
    if (auth_result is None):
        return jsonify(status='ERROR',token=None), 403
    return jsonify(status='OK',token=auth_result.decode()), 200

def register_user(requests):
    data = requests
    username = data['username']
    password = data['password']
    name = data['name']
    if username == None or password == None or name == None:
        return jsonify(status='ERROR',message='request failed'), 501
    a_model = Auth_Model()
    register_result = a_model.register(username, password, name)
    if register_result is None:
        return jsonify(status='ERROR',message='users already exixts'), 501
    return jsonify(status='OK',data=register_result), 201

def user_info():
    token = request.headers.get('Authorization') or ''
    if (auth_check(token) is not None):
        return auth_check(token), 404

    username = get_auth_data(token)['username']
    a_model = Auth_Model()
    users = a_model.user_info(username)
    data = ""
    for user in users:
        user = json.loads(user)
        if user['username'] == username:
            data = {
                "username" : user["username"],
                "name" : user["nama"],
                "usage" : user["usage"],
                "price" : (user["usage"]/1000000)/1000 * 10000,
            }
            return jsonify(status='OK',data=data), 200
    return jsonify(status='ERROR'), 501