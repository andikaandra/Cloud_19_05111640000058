import uuid
import pickledb

class Phonebook_Model(object):
	def __init__(self):
		self.db = pickledb.load('phone.db',True)
		#True ==> untuk bisa disimpan
		try:
			self.list()
		except KeyError:
			self.db.dcreate('phone')
	def add(self,p):
		if not isinstance(p,dict):
			return False
		uid = uuid.uuid1()
		self.db.dadd('phonedb',( "{}" .  format(str(uid)) ,  p ))
		return "{}" . format(str(uid))
	def list(self):
		return self.db.dgetall('phonedb')
	def get(self,id):
		try:
			return self.db.dget('phonedb',id)
		except KeyError:
			return False
	def empty(self):
		try:
			self.db.drem('phonedb')
			self.db.dcreate('phonedb')
		except KeyError:
			self.db.dcreate('phonedb')
		return True
	def remove(self,id):
		try:
			self.db.dpop('phonedb',id)
		except KeyError:
			return False
		return True


if __name__ == '__main__':
	#untuk ujicoba model
	p = Phonebook_Model()
	p.empty()
	print(p.list())
	p.add({'nama': 'Royyana', 'alamat': 'Ketintang', 'telp' : '+62813013'})
	p.add({'nama': 'Ananda', 'alamat': 'SMP 6 Surabaya', 'telp' : '+62813012'})
	p.add({'nama': 'Ibrahim', 'alamat': 'TK Perwanida', 'telp' : '+62813011'})
	print(p.list())
