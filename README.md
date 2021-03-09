# Django LinkedIn OAuth
Social OAuth authentication in Django

## Technologies
- [Poetry](https://python-poetry.org/docs/): Python package manager
- [Django](https://www.djangoproject.com/): Python backend framework
- [Python Social Auth - Django](https://github.com/python-social-auth/social-app-django): Setup social authentication
- Docker

## Install packages
`poetry install`

## Run migration and run server
```shell
poetry shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Run the server in Docker container
* Build the Docker image with tag
* Run the built docker image and expose the container port
```shell
docker build -t django-linkedin-oauth .
docker run -p 3001:3001 django-linkedin-oauth python manage.py runserver 0.0.0.0:3001
```

## Using Docker compose
```shell
docker-compose up
```

Rebuild the docker containers (for instance after adding a new dependency):
```shell
docker-compose up --build app
```