
# Info

### Stack

    django, tailwind, daisyui, postgresql

# Dev

### Setup
Create file .env and fill the data like in "example.env"

Setup python

    python -m pip install -r requirements.txt

Setup tailwind

    python manage.py tailwind install

### Run

Run in first terminal
    
    python manage.py tailwind start

Run in second terminal

    python manage.py runserver 127.0.0.1:8000

You can access web on 127.0.0.1:8000

# Production
Production working via CI/CD: github actions -> ssh -> docker compose

