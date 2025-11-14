

"""caprover specific django settings"""

import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured
from .settings import BASE_DIR


SECRET_KEY = os.environ.get("CR_SECRET_KEY") or ImproperlyConfigured("CR_DB_NAME not set")
DEBUG = False


# allowed hosts get parsed from a comma-separated list
hosts = os.environ.get("CR_HOSTS") or ImproperlyConfigured("CR_HOSTS not set")
try:
    ALLOWED_HOSTS = hosts.split(",")
except:
    raise ImproperlyConfigured("CR_HOSTS could not be parsed")

# Database
if os.environ.get("CR_USESQLITE"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
else:
    name = os.environ.get("CR_DB_NAME") or ImproperlyConfigured("CR_DB_NAME not set")
    user = os.environ.get("CR_DB_USER") or ImproperlyConfigured("CR_DB_USER not set")
    password = os.environ.get("CR_DB_PASSWORD") or ImproperlyConfigured("CR_DB_PASSWORD not set")
    host = os.environ.get("CR_DB_HOST") or ImproperlyConfigured("CR_DB_HOST not set")
    port = os.environ.get("CR_DB_PORT") or ImproperlyConfigured("CR_DB_PORT not set")

    DATABASES = {
        "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": name,
        "USER": user,
        "PASSWORD": password,
        "HOST": host,
        "PORT": port,
        }
    }


# Static Files
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATIC_URL = "/static/"



# wasabi
AWS_ACCESS_KEY_ID = os.environ.get("CR_AWS_ACCESS_KEY_ID") or ImproperlyConfigured("CR_AWS_ACCESS_KEY_ID not set")
AWS_SECRET_ACCESS_KEY = os.environ.get("CR_AWS_SECRET_ACCESS_KEY") or ImproperlyConfigured("CR_AWS_SECRET_ACCESS_KEY not set")
AWS_STORAGE_BUCKET_NAME = os.environ.get("CR_AWS_STORAGE_BUCKET_NAME") or ImproperlyConfigured("CR_AWS_STORAGE_BUCKET_NAME not set")
AWS_S3_ENDPOINT_URL = os.environ.get("CR_AWS_S3_ENDPOINT_URL") or ImproperlyConfigured("CR_AWS_S3_ENDPOINT_URL not set")


CELERY_BROKER_URL = os.environ.get("CR_CELERY_BROKER_URL") or ImproperlyConfigured("CR_CELERY_BROKER_URL not set")
# CELERY_RESULT_BACKEND = 'django-db'
# CELERY_CACHE_BACKEND = 'django-cache'