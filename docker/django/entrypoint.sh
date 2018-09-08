#!/bin/bash

echo "Starting Django runserver"
dockerize -timeout 30s python /code/manage.py migrate;
dockerize -timeout 30s python /code/manage.py runserver 0.0.0.0:8000;
