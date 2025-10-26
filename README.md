
# Info

### Stack

    django, tailwind, daisyui, postgresql

# Dev
Create file .env and fill the data like in "example.env"

Then setup python

    python -m pip install -r requirements.txt

Run in 1 terminal
    
    python manage.py tailwind start

Run in 2 terminal

    python manage.py runserver 127.0.0.1:8000

You can access web on 127.0.0.1:8000

# Production
Production working via github actions and docker
