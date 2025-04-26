#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input

# Only make migrations if there are model changes
if python manage.py makemigrations --check --dry-run | grep 'Migrations for'; then
    echo "Model changes detected. Creating migrations..."
    python manage.py makemigrations
fi

python manage.py migrate --fake-initial

echo "Deployment complete!"
