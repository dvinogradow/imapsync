Dockerize Imapsync
==================


Description
===========

Утилитка imapsync для переноса почтовых ящиков, удобна в том случае, когда ящиков как навоза, да и вцелом удобна:)
Устанавливать ее локально немного затруднительно, поэтому для удобства она будет крутится в Docker:)


Install
=======
 
 1. Нужен предустановленный Docker

 2. Билдим образ 

```bash
    docker build -t dvinogradow/imapsync:latest .
```
 
 3. Юзаем примерно так:

```bash
        docker run dvinogradow/imapsync:latest \
            --host1 server1 \
            --user1 user1@server1 \
            --password1 user1password \
            --host2 server2 \
            --user2 user1@server2 \
            --password2 user2password
```
