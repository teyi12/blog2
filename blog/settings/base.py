"""
Django settings sécurisés avec logique .env/.env.local, validation stricte,
et contrôle renforcé en environnement de production.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# === Base ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === Chargement du bon fichier .env ===
default_env = BASE_DIR / ".env"
local_env = BASE_DIR / ".env.local"
env_file = local_env if local_env.exists() else default_env
load_dotenv(dotenv_path=env_file)

# === Fonctions utilitaires ===
def get_env(key, required=True, default=None):
    value = os.getenv(key, default)
    if required and value is None:
        raise Exception(f"❌ Variable d'environnement manquante : {key}")
    return value

def get_bool(key, default=False):
    val = os.getenv(key)
    if val is None:
        return default
    return val.strip().lower() in ("1", "true", "yes", "on")

# === Sécurité ===
SECRET_KEY = get_env('SECRET_KEY')
DEBUG = get_bool('DEBUG', default=False)
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

if not DEBUG:
    if not any(ALLOWED_HOSTS):
        raise Exception("❌ ALLOWED_HOSTS doit être défini en production.")
    if SECRET_KEY.startswith("django-insecure-"):
        raise Exception("❌ Clé secrète de développement utilisée en production.")
