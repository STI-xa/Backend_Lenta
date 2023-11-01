FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y dos2unix

RUN pip install poetry==1.6.1

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . ./
COPY ./start_backend.sh ./

RUN chmod +x /app/start_backend.sh

RUN dos2unix /app/start_backend.sh

CMD ["/app/start_backend.sh"]