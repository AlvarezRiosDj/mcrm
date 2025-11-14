python manage.py collectstatic --noinput
# python manage.py makemigrations thumbnails
python manage.py migrate

#python manage.py deleterevisions --days=550

#gunicorn illapasmart.wsgi --bind=0.0.0.0:80 --timeout 600
daphne -b 0.0.0.0 -p 80 mcrm.asgi:application

#celery -A mcrm worker -l INFO
#celery -A mcrm beat -l INFO