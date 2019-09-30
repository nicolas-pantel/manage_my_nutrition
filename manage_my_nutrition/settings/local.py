"""
Settings for local dev server
"""
from manage_my_nutrition.settings.base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "!cz%0kktemx%j=0s*(l&9%)1nhn8+4)p%bop^^1ea^ztrp(a1#"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost"]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "../../db.sqlite3"),
    }
}
