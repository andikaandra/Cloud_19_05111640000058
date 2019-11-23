# Cloud_19_05111640000058

```
Nama : Andika Andra
NRP : 05111640000058
```

### How To 
##### Local Environment (tested)
- `sh scripts/run-redis.sh`
- `pip install -r requirements.txt`
- `python3 app.py`

##### Docker Based Environment (ongoing)


### Test
1. login : `curl -v http://localhost:5000/auth -X POST -d '{"username": "andika", "password": "andika123"}'`
    response: 
    ```
    {
        "status": "OK",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFuZGlrYSIsInBhc3N3b3JkIjoiYW5kaWthMTIzIiwibmFtYSI6IkFuZGlrYSBBbmRyYSIsImV4cCI6MTU3NDUzMjAyM30.GJ2R4IdhBTnTxIdK1b-rlBy6uXYKJ_ZdAMzuFQ8TwVE"
    }
    ```
1. convert video : `curl http://[ip_address]:[port docker container]/phonebook -H "Authorization: [token from step 1]" -XPOST -d '{"link" : "https://www.youtube.com/watch?v=WRz2MxhAdJo"}'`
    response: 
    ```
    {
        "data": "c9f61102-0e19-11ea-a8a8-386077a7ef2b",
        "status": "OK"
    }
    ```
2. download your video (use your browser for best experience :))
    use browser `http://localhost:5000/download/[data from process 2]`
    use curl `curl -O http://localhost:5000/download/[data from process 2]`

ps : token expires in 5 minutes