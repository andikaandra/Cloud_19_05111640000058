# Cloud_19_05111640000058

```
Nama : Andika Andra
NRP : 05111640000058
```

### How To 

##### Docker Based Environment
- `sudo docker-compose up -d`
- open [http://localhost:3000/d/cloud](http://localhost:3000/d/cloud) to see metrics

### Grafana Monitoring
![grafana](docs/11006468159522.png)

### Test
1. login [POST] :
    http://localhost:5000/auth
    header:
    ```
        Authorization : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFuZGlrYTEiLCJwYXNzd29yZCI6ImFuZGlrYTEyMyIsIm5hbWEiOiJidXp6ZXJidWZmIiwidXNhZ2UiOjAsImV4cCI6MTU3NTkwMjYwN30.-LdHs--I7u7tpENo2I1l0aknSNXLSmIBxFlaF7a050E
    ```

    request: 
    ```
    {
        "username" : "buzzerbuff",
        "password" : "buzzerbuff123"
    }
    ```
    
    response: 
    ```
    {
        "status": "OK",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFuZGlrYSIsInBhc3N3b3JkIjoiYW5kaWthMTIzIiwibmFtYSI6IkFuZGlrYSBBbmRyYSIsImV4cCI6MTU3NDUzMjAyM30.GJ2R4IdhBTnTxIdK1b-rlBy6uXYKJ_ZdAMzuFQ8TwVE"
    }
    ```
1. register [POST] :
    http://localhost:5000/register
    header:
    ```
        Authorization : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFuZGlrYTEiLCJwYXNzd29yZCI6ImFuZGlrYTEyMyIsIm5hbWEiOiJidXp6ZXJidWZmIiwidXNhZ2UiOjAsImV4cCI6MTU3NTkwMjYwN30.-LdHs--I7u7tpENo2I1l0aknSNXLSmIBxFlaF7a050E
    ```

    request: 
    ```
    {
        "username" : "buzzerbuff",
        "password" : "buzzerbuff123",
        "name" : "okabe rintarou"
    }
    ```
    
    response: 
    ```
    {
        "data": {
            "nama": "okabe rintarou",
            "password": "buzzerbuff123",
            "usage": 0,
            "username": "buzzerbuff"
        },
        "status": "OK"
    }
    ```
1. convert video [POST] :
    http://localhost:5000/youtube/add
    header:
    ```
        Authorization : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFuZGlrYTEiLCJwYXNzd29yZCI6ImFuZGlrYTEyMyIsIm5hbWEiOiJidXp6ZXJidWZmIiwidXNhZ2UiOjAsImV4cCI6MTU3NTkwMjYwN30.-LdHs--I7u7tpENo2I1l0aknSNXLSmIBxFlaF7a050E
    ```

    request: 
    ```
    {
        "link" : "https://www.youtube.com/watch?v=ePfX5lOs8sI",
        "extension" : "mp4" [optional][default :mp4],
        "resolution" : "360p" [optional][default : lowest resolution],
    }
    ```

    response: 
    ```
    {
        "data": "c9f61102-0e19-11ea-a8a8-386077a7ef2b",
        "status": "OK"
    }
    ```
1. download your video [GET]
    header:
    ```
        Authorization : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFuZGlrYTEiLCJwYXNzd29yZCI6ImFuZGlrYTEyMyIsIm5hbWEiOiJidXp6ZXJidWZmIiwidXNhZ2UiOjAsImV4cCI6MTU3NTkwMjYwN30.-LdHs--I7u7tpENo2I1l0aknSNXLSmIBxFlaF7a050E
    ```

    browser : `http://localhost:5000/download/c9f61102-0e19-11ea-a8a8-386077a7ef2b`
    curl : `curl -O http://localhost:5000/download/c9f61102-0e19-11ea-a8a8-386077a7ef2b`
1. user info [GET] :
    http://localhost:5000/user-info
    header:
    ```
        Authorization : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFuZGlrYTEiLCJwYXNzd29yZCI6ImFuZGlrYTEyMyIsIm5hbWEiOiJidXp6ZXJidWZmIiwidXNhZ2UiOjAsImV4cCI6MTU3NTkwMjYwN30.-LdHs--I7u7tpENo2I1l0aknSNXLSmIBxFlaF7a050E
    ```

    response: 
    ```
    {
        "data": {
            "name": "okabe rintarou",
            "price": 171.7896,
            "usage": 17178960,
            "username": "buzzerbuff"
        },
        "status": "OK"
    }
    ```
1. user info [GET] :
    http://localhost:5000/youtube/list
    header:
    ```
        Authorization : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFuZGlrYTEiLCJwYXNzd29yZCI6ImFuZGlrYTEyMyIsIm5hbWEiOiJidXp6ZXJidWZmIiwidXNhZ2UiOjAsImV4cCI6MTU3NTkwMjYwN30.-LdHs--I7u7tpENo2I1l0aknSNXLSmIBxFlaF7a050E
    ```

    response: 
    ```
    {
        "data": [
            {
                "link": "https://www.youtube.com/watch?v=rLoivO2nW54"
            },
            {
                "link": "https://www.youtube.com/watch?v=ePfX5lOs8sI"
            },
            {
                "link": "https://www.youtube.com/watch?v=xbhCPt6PZIU&list=RDSgXSomPE_FY&index=5"
            }
        ],
        "status": "OK"
    }
    ```

ps : token expires in 5 minutes