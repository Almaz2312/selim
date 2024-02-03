#!/bin/bash

# Move to project directory
cd /app

source "$(poetry env info --path)/bin/activate"

poetry install --no-interaction --no-ansi

# Run necessary commands
python3 manage.py collectstatic --no-input
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
