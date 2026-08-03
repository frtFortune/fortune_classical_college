from .base import *
from decouple import config

# In development it's common to enable debug via env
DEBUG = config('DEBUG', default=True, cast=bool)

# Use SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}
