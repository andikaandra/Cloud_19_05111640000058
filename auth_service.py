from flask import Flask,request,jsonify,make_response
from model.auth import Auth_Model
import json

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
