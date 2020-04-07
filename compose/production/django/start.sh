#!/bin/sh

python manage.py collectstatic --noinput&&
python manage.py makemigrations&&
python manage.py migrate&&
#gunicorn blogproject.wsgi:application -w 4 -k gthread -b 0.0.0.0:8000 --chdir=/app
gunicorn blogproject.wsgi:application -c ./compose/production/django/gunicorn.conf