FROM python:3.11

ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_PASSWORD=adminpassword
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com

ENV WORKDIR /lenta_app

WORKDIR $WORKDIR

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

RUN python manage.py migrate

RUN python manage.py collectstatic --noinput

RUN python manage.py createsuperuser --noinput


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
