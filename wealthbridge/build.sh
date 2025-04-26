#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install requirements
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Make migrations
python manage.py makemigrations

# Migrate database
python manage.py migrate

# Fix missing columns if any
python manage.py fix_db_columns
