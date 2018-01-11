Dockerize Imapsync
==================
Docker container with imapsync, dependences perl and helpfull script provides an opportunity to transfer many mailboxes at the same time

See imapsync on github for more information and options: https//github.com/imapsync/imapsync


Requirements
============

  * [Docker](https://docs.docker.com/installation/#installation)
  * [Docker Compose](https://docs.docker.com/compose/)


Configure and sync
==================

Configure the mailboxes that will be synced in the "data.txt" inside the "data" directory.


Run container
=============
 

```bash
    docker-compose up
```


Docker automatically run the sync script with the configured data in the "data" directory and write logs in the "data"
