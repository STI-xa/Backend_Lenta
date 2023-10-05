FROM python:3.11-slim

ENV WORKDIR /app
WORKDIR $WORKDIR

COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000