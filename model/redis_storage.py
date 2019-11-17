from typing import List, Any
import uuid
import redis
import json

class Phonebook_Model(object):
    def __init__(self,address='10.151.252.177'):
        self.redis_address = address
        self.db = redis.Redis(self.redis_address,port=6379,decode_responses=True)
        #localhost harus diganti ke ip address yang dibind oleh container redis
        #True ==> untuk bisa disimpan
    def add(self,p):
        if not isinstance(p,dict):
            return False
        uid = uuid.uuid1()
        self.db.set(str(uid) ,  json.dumps(p) )
        return "{}" . format(str(uid))
    def list(self):
        hasil = []
        for x in self.db.keys():
            hasil.append({x: self.db.get(x)})
        return hasil
    def get(self,id):
        try:
            return json.loads(self.db.get(id))
        except:
            return False
    def empty(self):
        try:
            for x in self.db.keys():
                #print(x)
                self.db.delete(x)
        except:
            return True
        return True
    def remove(self,id):
        try:
            self.db.delete(id)
        except KeyError:
            return False
        return True


if __name__ == '__main__':
    p = Phonebook_Model()
    p.empty()
    print(p.list())
    p.add({'nama': 'Royyana', 'alamat': 'Ketintang', 'telp' : '+62813013'})
    p.add({'nama': 'Ananda', 'alamat': 'SMP 6 Surabaya', 'telp' : '+62813012'})
    p.add({'nama': 'Ibrahim', 'alamat': 'TK Perwanida', 'telp' : '+62813011'})
    print(p.list())
