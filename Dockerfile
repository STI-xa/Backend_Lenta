FROM python:3.11

ENV WORKDIR /app

WORKDIR $WORKDIR

COPY requirements.txt .

RUN pip3 install -r ./requirements.txt --no-cache-dir

COPY . .

CMD ["backend.wsgi.application", "--bind", "0:8000" ]
