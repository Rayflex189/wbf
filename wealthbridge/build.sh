#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py makemigrations

if ! python manage.py migrate; then
    echo "Normal migration failed. Attempting --fake migration..."
    python manage.py migrate --fake
fi
