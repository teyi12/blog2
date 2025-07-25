import os


env = os.getenv("DJANGO_ENV", "local")  # par défaut : local

if env == "production":
    from .production import *
else:
    from .local import *
