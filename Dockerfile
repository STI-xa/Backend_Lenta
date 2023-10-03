FROM python:3.11.4-slim


ENV WORKDIR /app/backend

WORKDIR $WORKDIR

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000


CMD ["gunicorn", "foodgram_project.wsgi:application", "--bind", "0:8000" ]
