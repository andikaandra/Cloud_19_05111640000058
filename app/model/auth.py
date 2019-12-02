import jwt
import datetime
import time
import os
import json

from model.redis_storage import Redis_storage

user_model = Redis_storage()

class Token_Model(object):
	def __init__(self,data={}):
		self.key='buzzerbuff123'
		self.data = data
	def get_encoded(self):
		encoded = jwt.encode(self.data,self.key,'HS256')
		return encoded
	def get_decoded(self):
		decoded = jwt.decode(self.data,self.key,'HS256')
		return decoded

class Auth_Model(object):
	def __init__(self):
		self.username = ''
		self.password = ''
		self.USERS=user_model.list('users')
		# self.USERS.append({'username' : 'andika', 	'password': 'andika123', 'nama': 'Andika Andra'})

	def check_user(self, username, password):
		found=None
		for x in self.USERS:
			x = json.loads(x)
			if ((x['username']==username) and (x['password']==password)):
				found=x
				break
		return found

	def login(self, username, password):
		user_detail = self.check_user(username,password)
		if (user_detail is None):
			return None
		token_expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
		user_detail['exp'] = token_expiration
		return Token_Model(user_detail).get_encoded()

	def register(self, username, password, name = ''):
		user_detail = self.check_user(username, password)
		if (user_detail is not None):
			return None
		data = {'username' : username, 	'password': password, 'nama': name, 'usage': 0}
		# self.USERS.append(data)
		user_model.add(data, 'users')
		return data

	def check_token(self, data):
		if data=='':
			return None
		try:
			return Token_Model(data).get_decoded()
		except jwt.ExpiredSignatureError:
			return None
		except jwt.exceptions.InvalidSignatureError:
			return None