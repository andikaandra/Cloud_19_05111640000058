from flask import Flask,request,jsonify,make_response
from flask_restful import Resource, Api, reqparse
import json
import os
import sys

sys.path.append('/home/andika/Documents/learn/python/Cloud_19_05111640000058')

# from model.local import *
from model.redis_storage import Phonebook_Model

#phonebook_model = Phonebook_Model()

redis_addr = os.getenv("REDISADDR") or "localhost"
phonebook_model = Phonebook_Model(address=redis_addr)

application = Flask(__name__)
api = Api(application)

class Phonebook_Service(Resource):
    def get_resp(self,pb_data):
        status = 'ERROR' if pb_data == False else 'OK'
        http_code = 404 if pb_data == False else 200
        return status,http_code

    def get(self,id=''):
        if (id==''):
            pb_data = phonebook_model.list()
        else:
            pb_data = phonebook_model.get(id)

        status, http_code = self.get_resp(pb_data)
        return dict(status=status,data=pb_data),http_code
    def post(self):
        args = request.get_json(force=True)
        pb_data = phonebook_model.add(args)
        status, http_code = self.get_resp(pb_data)
        return dict(status=status,data=pb_data),http_code
    def delete(self,id=''):
        if (id==''):
            pb_data=False
        else:
            pb_data = phonebook_model.remove(id)
        status, http_code = self.get_resp(pb_data)
        return dict(status=status,data=pb_data),http_code


api.add_resource(Phonebook_Service,'/person','/person/<id>')


if __name__ == '__main__':
    from gevent.pywsgi import WSGIServer
    http_server = WSGIServer(('',5000),application)
    http_server.serve_forever()


