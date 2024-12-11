#!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r ./requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver