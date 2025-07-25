from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-dev-key")


# Exemple DB locale
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
