FROM ubuntu:18.04
MAINTAINER michallee104@126.com

ENV LANG C.UTF-8

RUN mkdir /code
WORKDIR /code
COPY . /code

RUN apt-get update && apt-get install -y python3 python3-pip cron chromium-chromedriver && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    pip3 install -r requirement.txt && \
    python3 manage.py crontab add && \
    python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    python3 manage.py collectstatic --no-input


EXPOSE 9019 9019
