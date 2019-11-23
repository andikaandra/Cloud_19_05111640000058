sudo docker rm -f myredis_db ; sudo docker run  --name myredis_db -p 0.0.0.0:6379:6379  -v $(pwd)/redisdata:/data -d redis

REDISADDR="10.151.253.121"
sudo docker rm -f p1 ; sudo docker run --name p1 -d -p 9991:5000 --env REDISADDR=${REDISADDR}  phonebook-docker-2:1.0
sudo docker rm -f p2 ; sudo docker run --name p2 -d -p 9992:5000 --env REDISADDR=${REDISADDR}  phonebook-docker-2:1.0
sudo docker rm -f p3 ; sudo docker run --name p3 -d -p 9993:5000 --env REDISADDR=${REDISADDR}  phonebook-docker-2:1.0
sudo docker rm -f p4 ; sudo docker run --name p4 -d -p 9994:5000 --env REDISADDR=${REDISADDR}  phonebook-docker-2:1.0
