FROM python:3.7-alpine
USER root
RUN apt-get update && apt-get -y install build-essential libsasl2-dev
COPY . /usr/src/app
WORKDIR /usr/src/app
COPY src/ /app
WORKDIR /app
RUN python3 -m venv venv &&\
 venv/bin/pip3 install --upgrade pip &&\
 venv/bin/pip3 install -e '.[all]'
