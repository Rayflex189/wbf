#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py makemigrations bank_app

if ! python manage.py migrate bank_app; then
    echo "Normal migration failed. Attempting --fake migration..."
    python manage.py migrate bank_app --fake-initial
fi
