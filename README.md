# API_DRF

#### Cоздайте файл Dockerfile в текущей директории с содержимым, приведенным ниже:
```
FROM python:3.12-slim

WORKDIR /api

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/typicalstandard/Api-DRF.git /app

RUN pip install -r /app/project/requirements.txt
RUN pip install gunicorn

WORKDIR /api/project/

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi:application"]
```
#### Выполните команду для создания Docker-образа в текущей директории 
```
docker build -t apidrf .
```
#### После создания Docker-образа запустите контейнер, используя следующую команду:
```
docker run -p 8000:8000 apidrf
```
#### После выполнения этих команд, ваше приложение будет доступно по URL-адресу:
```
http://localhost:8000
```
