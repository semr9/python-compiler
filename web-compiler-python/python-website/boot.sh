#!/bin/sh
# called by Dockerfile

# go to directory where wsgi.py is
cd /app
# start gunicorn
exec gunicorn -b :5000 --access-logfile - --error-logfile - wsgi:app

ls /app