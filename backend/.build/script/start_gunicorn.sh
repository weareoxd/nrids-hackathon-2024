#!/bin/bash
NAME="django_app"                                      # Name of the application
DJANGODIR=/var/www/html/                               # Django project directory

if [[ -z "${GUNICORN_WORKERS}" ]]; then
  NUM_WORKERS=2                                          # How many worker processes should Gunicorn spawn (2-4 workers per core)
else
  NUM_WORKERS="${GUNICORN_WORKERS}"
fi

if [[ -z "${GUNICORN_MAXREQUESTS}" ]]; then
  MAX_REQUESTS=1000                                          # How many requests a worker can handle
else
  MAX_REQUESTS="${GUNICORN_MAXREQUESTS}"
fi

if [[ -z "${GUNICORN_MAXREQUESTSJITTER}" ]]; then
  MAX_REQUESTS_JITTER=50
else
  MAX_REQUESTS_JITTER="${GUNICORN_MAXREQUESTSJITTER}"
fi

TIMEOUT=600
DJANGO_SETTINGS_MODULE=app.config.settings             # Which settings file should Django use
DJANGO_CONFIGURATION=Production                        # Django configuration name
DJANGO_WSGI_MODULE=wsgi                                # WSGI module name

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export DJANGO_CONFIGURATION=$DJANGO_CONFIGURATION
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

echo "[Web Application] Starting gunicorn"
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --max-requests $MAX_REQUESTS \
  --max-requests-jitter $MAX_REQUESTS_JITTER \
  --timeout $TIMEOUT \
  --bind localhost:8081 \
  --enable-stdio-inheritance \
  --error-logfile /var/log/gunicorn/error.log \
  --access-logfile /var/log/gunicorn/access.log \
  --capture-output \
  --log-level=info \
  --log-file=-
