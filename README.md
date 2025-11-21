
# Info

### Stack

    django, tailwind, daisyui, postgresql

# Dev

### Setup

#### .env

    Create file .env in the root and fill the data like in "example.env"

#### db

    python3 manage.py migrate

#### python

    python3 -m pip install -r requirements.txt

#### tailwind

    python3 manage.py tailwind install

### Run

Run in first terminal
    
    python3 manage.py tailwind start

Run in second terminal

    python3 manage.py runserver 127.0.0.1:8000

You can access web on 127.0.0.1:8000

# Production
Production working via CI/CD: github actions -> ssh -> docker compose

