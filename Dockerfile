#Running commands on the docker image
FROM python:3.7-alpine
LABEL maintainer="Biohazard"  

ENV PYTHONUNBUFFERED 1

#copy the requirements for our dir to docker image
COPY ./requirements.txt /requirements.txt

#install the req on docker image
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
#copy the source code to app folder in docker image
COPY ./app /app


#create a new user and switch to user
#otherwise root will be the default user
#limits attack within the docker container
RUN adduser -D user
USER user 
