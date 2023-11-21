from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["localhost"]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True
