import jwt
import datetime
import time
import hashlib

class Token_Model(object):
	def __init__(self,data={}):
		self.key='kaoskakibiru12345'
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
		self.USERS.append({'username' : 'leomessi', 	'password': 'kaoskakimerah123', 'nama': 'Lionel Messi'})
		self.USERS.append({'username' : 'rakitic', 		'password': 'kaoskakimerah456', 'nama': 'Ivan Rakitic'})
		self.USERS.append({'username' : 'iniesta',		'password': 'kaoskakimerah789', 'nama': 'Iniesta'})

	def cek_user(self,username,password):
		ketemu=None
		for x in self.USERS:
			if ((x['username']==username) and (x['password']==password)):
				ketemu=x
				break
		return ketemu

	def login(self,username,password):
		user_detail = self.cek_user(username,password)
		if (user_detail is not None):
			token_expiration = datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
			user_detail['exp'] = token_expiration
			return Token_Model(user_detail).get_encoded()
		else:
			return None
	def cek_token(self,data):
		if data=='':
			return None
		try:
			return Token_Model(data).get_decoded()
		except jwt.ExpiredSignatureError:
			return None
		except jwt.exceptions.InvalidSignatureError:
			return None


if __name__ == '__main__':
	auth = Auth_Model()
	token = auth.login('slamet','kaoskakimerah')
	print(token)
	token = auth.login('leomessi','kaoskakimerah123')
	print(token.decode())
	#time.sleep(10)
	token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imxlb21lc3NpIiwicGFzc3dvcmQiOiJrYW9za2FraW1lcmFoMTIzIiwibmFtYSI6Ikxpb25lbCBNZXNzaSIsImV4cCI6MTU3MzUxNjI5Nn0.KuEO9EPwQ2esSsyFWZ-dn8rKTkp0MAXhIuu3SpigUSg'
	cek = auth.cek_token(token)
	print(cek)
	#cek will be None if token is expired
