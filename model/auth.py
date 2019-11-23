import jwt
import datetime
import time

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
		self.USERS=[]
		self.USERS.append({'username' : 'andika', 	'password': 'andika123', 'nama': 'Andika Andra'})

	def check_user(self, username, password):
		ketemu=None
		for x in self.USERS:
			if ((x['username']==username) and (x['password']==password)):
				ketemu=x
				break
		return ketemu

	def login(self, username, password):
		user_detail = self.check_user(username,password)
		if (user_detail is not None):
			token_expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
			user_detail['exp'] = token_expiration
			return Token_Model(user_detail).get_encoded()
		else:
			return None
	def check_token(self, data):
		if data=='':
			return None
		try:
			return Token_Model(data).get_decoded()
		except jwt.ExpiredSignatureError:
			return None
		except jwt.exceptions.InvalidSignatureError:
			return None