sudo docker rm -f myredis_db ; sudo docker run  --name myredis_db -p 0.0.0.0:6379:6379  -v $(pwd)/redisdata:/data -d redis
