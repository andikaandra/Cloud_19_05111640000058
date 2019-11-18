# Cloud_19_05111640000058

```
Nama : Andika Andra
NRP : 05111640000058
```

### How To 

- on [redis_storage.py](/model/redis_storage.py#L7), change address by your ip address
- on [run.sh](/run.sh#L3), change address by your ip address
- build images if not exists `sudo docker build -t phonebook-docker-2:1.0 .`
- `sh run.sh`


### Test
- login : `curl -v http://[ip_address]:[port docker container]/auth -X POST -d '{"username": "andika", "password": "andika123"}'`
- access resouces : `curl http://[ip_address]:[port docker container]/phonebook -H "Authorization: [auth code from login]"`
- add record to redis : `curl http://[ip_address]:[port docker container]/phonebook -H "Authorization: " -XPOST -d '{"nama" : "andika", "alamat": "melbourne"}'`


ps: fastest way to get your ip addres by `hostname -I`