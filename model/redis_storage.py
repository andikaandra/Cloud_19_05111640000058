import uuid
import redis
import json

class Redis_storage(object):
    def __init__(self,address='localhost'):
        self.redis_address = address
        self.db = redis.Redis(self.redis_address,port=6379,decode_responses=True)
    def add(self,p):
        if not isinstance(p,dict):
            return False
        uid = uuid.uuid1()
        self.db.set(str(uid) ,  json.dumps(p) )
        return "{}" . format(str(uid))
    def list(self):
        res = []
        for x in self.db.keys():
            res.append({x: self.db.get(x)})
        return res
    def get(self,id):
        try:
            return json.loads(self.db.get(id))
        except:
            return False
    def empty(self):
        try:
            for x in self.db.keys():
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

if __name__ == "__main__":
    storage = Redis_storage()
    storage.empty()