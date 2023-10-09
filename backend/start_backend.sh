#!/bin/bash
python3 manage.py makemigrations users
python3 manage.py makemigrations sales
python3 manage.py migrate
python3 manage.py migrate --run-syncdb
python3 manage.py collectstatic
cp -r ../app/collected_static/. ../backend_static/static/
python3 manage.py createsuperuser --noinput
python3 manage.py load_sku_data
python3 manage.py load_shop_data
python3 manage.py load_sales_data
exec gunicorn backend.wsgi:application --bind 0.0.0.0:8000