menjalankan program
------------------------
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python Phonebook_Service.py

testing

mendapatkan seluruh record
    curl -v http://localhost:5000/person

cek id - c7799c94-d897-11e9-9f2a-6480995fff24
    curl -v http://localhost:5000/person/c7799c94-d897-11e9-9f2a-6480995fff24



#Membangun virtualized & isolated environment dengan docker

1. bukalah tab terminal

   sudo docker build -t phonebook-docker-1:1.0 .

   phonebook-docker-1 merupakan nama image yang nantinya akan dijalankan sebagai container dengan tag versi 1.0

2. lihatlah daftar images yang ada dan pastikan phonebook-docker-1:1.0 ada dalam daftar tersebut
   sudo docker images

3. jalankan images tersebut untuk menjadi container
   sudo docker run -d --name phonebook-container phonebook-docker-1:1.0


