FROM python:3.4
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get install -y wget build-essential

# setup and install dockerize
ENV DOCKERIZE_VERSION v0.6.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# install project requirements
ADD ./requirements/base.txt /requirements/base.txt
RUN pip install -r /requirements/base.txt

# cleanup apt repos
RUN rm -rf /var/lib/apt/lists/*
