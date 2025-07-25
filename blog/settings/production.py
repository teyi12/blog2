from .base import *

DEBUG = get_bool("DEBUG", False)
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

DATABASES = {
    'default': dj_database_url.parse(get_env("DATABASE_URL"), conn_max_age=600)
}
