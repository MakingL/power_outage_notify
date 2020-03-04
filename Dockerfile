FROM ubuntu:18.04
MAINTAINER michallee104@126.com

ENV LANG C.UTF-8

RUN mkdir /code
WORKDIR /code
COPY . /code

RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list && \
    apt-get clean && \
    apt-get update && apt-get install -y python3 python3-pip cron chromium-chromedriver && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    pip3 install  -i https://pypi.tuna.tsinghua.edu.cn/simple  -r requirement.txt && \
    python3 manage.py crontab add && \
    python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    python3 manage.py collectstatic --no-input


EXPOSE 9019 9019
