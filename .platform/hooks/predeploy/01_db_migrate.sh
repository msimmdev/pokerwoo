#!/bin/bash

source /var/app/venv/*/bin/activate
POKERWOO_MIGRATE=1 python manage.py migrate --noinput