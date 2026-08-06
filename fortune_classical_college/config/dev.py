from .base import *
from decouple import config

DEBUG = config("DEBUG", default=True, cast=bool)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(BASE_DIR / "db.sqlite3"),
    }
}

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
