#!/bin/bash

python manage.py migrate
python manage.py import_fixtures
python manage.py collectstatic --clear --no-input

# Start supervisor
echo "[Web Application] Starting supervisor"
supervisord -n
