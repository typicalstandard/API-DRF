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
