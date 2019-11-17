untuk menjalankan model dengan backend db redis,
redis adalah key-value storage
https://redis.io/


jalankan redis terlebih dahulu dengan
sh run-redis.sh
perintah tersebut akan menjalankan redis yang di bind ke any address di port 6379 (insecure)

untuk bahasa pemrograman python
library dapat dilihat di 
https://pypi.org/project/redis/


-----------------------------------------

untuk build lakukan hal yang mirip pada readme.txt
1. bukalah tab terminal
   sudo docker build -t phonebook-docker-2:1.0 .
   phonebook-docker-2 merupakan nama image yang nantinya akan dijalankan sebagai container dengan tag versi 1.0

2. lihatlah daftar images yang ada dan pastikan phonebook-docker-2:1.0 ada dalam daftar tersebut
   sudo docker images

3. jalankan container
   sudo docker rm -f pservice2 && sudo docker run --name pservice2 -p 9999:5000 --env REDISADDR=<alamat ip>  phonebook-docker-2:1.0
   gunakan alamat ip dari komputer anda
   sebelumnya redis service harus dijalankan terlebih dahulu seperti pada poin diatas dengan sh run-redis

4. container akan berjalan sebagai service di port 9999

5. untuk testing gunakan curl
   curl -v http://localhost:9999/person
   atau cobalah lakukan curl dari komputer lain
   curl -v http://<ipaddres>:9999/person



