from flask import Flask,request,jsonify,make_response
from model.auth import Auth_Model
import json

def auth(requests):
    data = requests
    username = data['username']
    password = data['password']
    a_model = Auth_Model()
    auth_result = a_model.login(username,password)
    if (auth_result is not None):
        return jsonify(status='OK',token=auth_result.decode()), 200
    else:
        return jsonify(status='ERROR',token=None), 501