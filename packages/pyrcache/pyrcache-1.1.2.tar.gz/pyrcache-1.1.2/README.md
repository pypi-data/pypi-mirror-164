## Pyrcache
#### Setup
1. Install Docker + Docker Desktop
2. Open a terminal and enter: 
    ```
        git clone github.com/yamaceay/rediscache
        cd rediscache
        docker-compose up --build
    ```
3. Now you are ready to go!

#### Get Started

```
    import rcache
    print(rcache.keys()) # prints all keys from the database
    if len(rcache.keys()) == 0:
        exit()
    key = rcache.keys()[0]
    print(rcache.rget(key)) # print the value of key
    value = "{\"name\": \"mike\", \"surname\": \"smith\"}"
    rcache.rset(key, value) # updates the key-value pair
```