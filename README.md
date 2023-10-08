# **Hackathon_lenta_backend** 

Backend часть для проекта хакатона Практикум х Лента. Основной функционал проекта- создать интерфейс и алгоритм прогноза спроса на 14 дней для товаров собственного производства сети Лента.

**Как работает:**

1. Бэкенд отдаёт данные на фронтенд. По запросу от фронта идёт в БД, выбирает необходимые данные, подгототавливает (если требуется), отдаёт в ответе на запрос.
2. Добавление фактических данных. Принимает входящий запрос на добавление исторических данных по продажам, обрабатывает их и складывает в БД. 
3. Запускает и управляет процессом инференса. По расписанию (раз в день) или после обновления исторических данных начинает процесс прогнозирования. Для этого идёт в БД, выбирает необходимые данные, передаёт их в ML сервис, получает прогноз и складывает его в БД.
___

## **Что внутри**:
* API сервис для взаимодействия с фронтендом и ML моделью.
* Контейнеризация для организации микросервисной структуры, связь фронтенда и модели прогнозирования.
___
## **Как запустить проект**:

### **Для Windows, локально, только бэкенд :**

* Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Anstane/hackathon_lenta_backend.git

cd backend
```

* Cоздать и активировать виртуальное окружение:
```
python -m venv venv

source venv/Scripts/activate
```

* Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

* Выполнить миграции:
```
python manage.py migrate
```

* Запустить проект:
```
python manage.py runserver
```

### **Запуск из контейнера (все части проекта):**
* Клонировать репозиторий и перейти в папку infra в командной строке:
```
git clone https://github.com/anstane/lenta_backend

cd infra
```

* Создание и запуск контейнеров:
```
docker-compose up -d --build
```

* Создаем дамп БД:
```
docker-compose exec backend python manage.py dumpdata > fixtures.json
```
* Создаем в папке infra .env файл и записываем переменные окружения.
## Шаблон наполнения env-файла:
```
DB_ENGINE=django.db.backends.postgresql # указывает, с какой БД работать
DB_NAME=postgres # имя БД
POSTGRES_USER=postgres # логин для подключения к БД
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

### **Образ доступен на** [DockerHub](https://hub.docker.com/repository/docker/)
___
## **Примеры запросов**:

____
# **Разработчики:**
[Михаил Московкин](https://github.com/Anstane) - Разработчик
[Полина Николаева](https://github.com/STI-xa) - Разработчик
___
## **Стэк технологий**:
* ![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
* ![image](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
* ![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
* ![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
* ![image](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
* ![image](https://img.shields.io/badge/Djoser-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)
* ![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
* ![image](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
