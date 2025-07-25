from pathlib import Path
import os
import sys
from dotenv import load_dotenv
import dj_database_url

# === Base ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === .env : Chargement dynamique selon contexte ===
default_env = BASE_DIR / ".env"
local_env = BASE_DIR / ".env.local"
env_file = local_env if local_env.exists() else default_env
load_dotenv(dotenv_path=env_file)

# === Fonction utilitaire pour les variables d’environnement ===
def get_env(key, required=True, default=None):
    value = os.getenv(key, default)
    if required and value is None:
        raise Exception(f"❌ Variable d'environnement manquante : {key}")
    return value

# === Clés sensibles ===
SECRET_KEY = get_env('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")
if not DEBUG and not any(ALLOWED_HOSTS):
    raise Exception("❌ ALLOWED_HOSTS doit être défini en production.")

# === Applications ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'widget_tweaks',
    'articles.apps.ArticlesConfig',
]

# === Cloudinary (prod uniquement) ===
if not DEBUG:
    cloud_name = get_env('CLOUD_NAME')
    api_key = get_env('CLOUDINARY_API_KEY')
    api_secret = get_env('CLOUDINARY_API_SECRET')

    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': cloud_name,
        'API_KEY': api_key,
        'API_SECRET': api_secret,
    }

# === Middleware ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# === Sécurité renforcée en production ===
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# === Fichiers statiques et médias ===
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# === URLs ===
ROOT_URLCONF = 'blog.urls'
WSGI_APPLICATION = 'blog.wsgi.application'

# === Templates ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# === Base de données ===
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': get_env('DB_NAME'),
            'USER': get_env('DB_USER'),
            'PASSWORD': get_env('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST', 'localhost'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }

# === Validation de mot de passe ===
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# === Internationalisation ===
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# === Email ===
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = get_env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = get_env("DEFAULT_FROM_EMAIL", required=False)
CONTACT_EMAIL = get_env("CONTACT_EMAIL", required=False)

# === Auth redirects ===
LOGIN_REDIRECT_URL = 'profil'
LOGOUT_REDIRECT_URL = 'login'

# === Logging (basique mais utile en prod) ===
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

# === Clé primaire auto ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
