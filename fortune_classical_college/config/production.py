from .base import *
from decouple import config, Csv

# Production should be explicit about debug
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())

# Example PostgreSQL config (commented). Install psycopg2-binary and set env vars in production.
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('POSTGRES_DB'),
#         'USER': config('POSTGRES_USER'),
#         'PASSWORD': config('POSTGRES_PASSWORD'),
#         'HOST': config('POSTGRES_HOST', default='localhost'),
#         'PORT': config('POSTGRES_PORT', default='5432'),
#     }
# }
