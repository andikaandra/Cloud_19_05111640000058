sudo docker rm -f myredis_db ; sudo docker run  --name myredis_db -p 0.0.0.0:6379:6379  -v $(pwd)/redisdata:/data -d redis

REDISADDR="10.151.31.54"
sudo docker rm -f p1 ; sudo docker run --name p1 -d -p 9991:5000 --env REDISADDR=${REDISADDR}  test:1.0