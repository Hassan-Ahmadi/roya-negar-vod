# Project Setup

This is a [Docker][] setup for a sample vod backend based on Django.

- The [Django][] application is served by [Gunicorn][] (WSGI application).
- We use [NginX][] as reverse proxy and static files server. Static and media files are
  persistently stored in volumes.
- [Postgres][] database is used. Data are persistently stored in volumes.

## Requirements
You need to install [Docker][] and [Docker-Compose][].

## Build
`docker compose up --build`

## Migrate databases
```
docker compose backend exce sh -c "python manage.py makemigrations --no-input"
docker compose backend exce sh -c "python manage.py migrate --no-input" 
```


## Collect static files
```
docker compose backend exce sh -c "python manage.py collectstatic --no-input"
```

## Run
`docker compose up`

[Docker]: https://www.docker.com/
[Django]: https://www.djangoproject.com/
[Gunicorn]: http://gunicorn.org/
[NginX]: https://www.nginx.com/
[Postgres]: https://www.postgresql.org/
[Python]: https://www.python.org/
[Docker-Compose]: https://docs.docker.com/compose/

## Test
There is postman collection "Roya-Negar.postman_collection.json" in this repo which you can use it for test.

Also after creating a superuser you can also log in to django-admin panel and see more development details.

## License
Software licensed under the [ISC license](/LICENSE).