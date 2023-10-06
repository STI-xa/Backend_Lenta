#!/bin/bash

python manage.py makemigrations users
python manage.py makemigrations sales
python manage.py migrate
python manage.py migrate --run-syncdb
python manage.py collectstatic
cp -r ../app/collected_static/. ../backend_static/static/
python manage.py createsuperuser --noinput
python manage.py load_sku_data
python manage.py load_shop_data

exec gunicorn backend.wsgi:application --bind 0.0.0.0:8000
