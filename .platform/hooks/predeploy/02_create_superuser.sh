#!/bin/bash

source /var/app/venv/*/bin/activate
python manage.py createsuperuser --noinput || :