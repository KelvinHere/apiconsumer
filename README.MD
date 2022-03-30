# API Consumer

This website [LINK HERE](HTTP://46.101.60.151:8888) remotely consumes my [Random Word API](HTTP://46.101.13.65:8000).

## About

Hosted on a VPS inside a Docker container, this project is an example of a website which consumes an API located in another Docker container.

## Features

Website  consumes a remote API

## Layout

Below is a layout diagram of how the websites communicate and where they are placed.

![Layout](https://github.com/KelvinHere/apiconsumer/blob/master/app/static/images/layout.jpg)

## Deployment

* Pre-requisites
    * A machine with Docker installed

1. Clone the repo
1. Create a .env.compose file in the project root, populate with 
``` 
IN_DOCKER=TRUE
SECRET_KEY=PLACE_DJANGO_SECRET_KEY_HERE
DEBUG=FALSE
```
3. Build the docker image with ```docker-compose build```
4. Activate the container with ```docker-compose up```
5. The website should now be accessible through 'your IP' + :8888 as the port

## Technologies

* Docker
* Docker-compose
* Django
* Django Requests
* Gunicorn
* Whitenoise
