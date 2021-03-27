
## Assignment 4
As last part of Database Advanced we need to transform or scraper project into a docker container. Docker container makes it easier to run all the needed import,dependencies in 1 environment. Dockers containers ae used because it easy to deploy anywhere. You don't need to install a new environment. It does everything for you in an automated way.

### Installation
sudo apt install docker.io

```
docs.docker.com/compose/gettingstarted/
```
1. Define all out docker dependencies.
2. Create a Dockerfile. The dockerfile builds the docker image. The image contains all the dependencies our python applications needs. We build the docker on a Python environment.

```
# Image
FROM python:3.7-alpine 
MAINTAINER diegoborghgraef
WORKDIR /code


# Dependencies
RUN pip3 install pymongo
RUN pip3 install requests
RUN pip3 install redis
RUN pip3 install beautifulsoup4

COPY scraper.py scraper.py
CMD ["python3", "scraper.py"]
```
3. Define services in our docker-compose file.
```
version : '3.3'

services: 
  mongo: 
    image: mongo
    # container_name: mongoDB
    restart: always
    ports: 
      # Host / Docker container
      - 30000:27017

  redis:
    image: redis
    # container_name: redis
    restart: always
    ports:
      - 7000:6379

  mongoexpress:
    image: mongo-express
    environment:
      - ME_CONFIG_MONGODBSERVER=mongo
    ports:
      - 8081:8081

  scraper:
     build: .
     ports:
      - 5000:5000
```

4. Bash script to build/run our docker compose.
```
# !/bin/bash

sudo apt install docker.io docker-compose -y
sudo docker-compose build
sudo docker-compose up 
```

5. MongoExpress

![alt text](https://i.imgur.com/6IFsMgz.png)
