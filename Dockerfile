# 1 start docker kernal & python
FROM python:3.12-slim-bullseye

# show logs : python
ENV PYTHONUNBUFFERED=1

# update kernal & install
RUN apt-get update && apt-get -y install gcc libpq-dev

# folder for my project
WORKDIR /app

# copy requirements.txt /app/requirements.txt
COPY requirements.txt /app/requirements.txt

# install requirements.txt
RUN pip install -r /app/requirements.txt

# copy project
COPY . /app/