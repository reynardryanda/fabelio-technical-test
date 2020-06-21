release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn technical_test.wsgi --log-file -