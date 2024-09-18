#!/bin/bash

python manage.py migrate
python manage.py loaddata fixtures/seed.json
python manage.py collectstatic --clear --no-input

# Start supervisor
echo "[Web Application] Starting supervisor"
supervisord -n
