FROM python:3.9.13-slim-bullseye

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

COPY . /tmp
WORKDIR /tmp

RUN pip3 install -e .

RUN apt-get update && apt-get install make libgomp1 -y
