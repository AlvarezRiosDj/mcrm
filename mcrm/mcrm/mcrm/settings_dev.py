"""local runserver settings"""

import os
from .settings import BASE_DIR

SECRET_KEY = 'django-insecure-&^%$p@@676rrn(4^_f3ov@5eflfr)(*z&ux6__esa!ss9^c7^m'

ALLOWED_HOSTS = ['*']

DEBUG = True

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": "mcrm",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": 5432,
    }
}

# STATICFILES_DIRS = ( os.path.join('static'), )

# # Static Files
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATIC_URL = "/static/"


# wasabi
AWS_ACCESS_KEY_ID = '2UGQM56G7DYO8HD2IRHV'
AWS_SECRET_ACCESS_KEY = 'DzlHD9qbqAje5eA2eeSojNFVk7gkpEDvqDw0ZeSA'
AWS_STORAGE_BUCKET_NAME = 'otmprueba'
AWS_S3_ENDPOINT_URL = 'https://s3.us-central-1.wasabisys.com'

# AWS_DEFAULT_ACL = 'public-read'


CELERY_BROKER_URL = 'amqp://rabbitmq'
# CELERY_RESULT_BACKEND = 'django-db'
# CELERY_CACHE_BACKEND = 'django-cache'
# CELERY_BROKER_URL = 'amqp://usuario:contraseña@ip:puerto/virtual_host'


