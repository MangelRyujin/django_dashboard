from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

ALTERNATIVE_DBS = {
    "postgres": {
        "ENGINE": config("ENGINE",default="django.db.backends.postgresql"),
        "NAME": config("DB_NAME", default="postgres"),
        "USER": config("DB_USER", default="postgres"),
        "PASSWORD": config("DB_PASSWORD", default="postgres"),
        "HOST": config("DB_HOST", default="127.0.0.1"),
        "PORT": config("DB_PORT", default=5432),
    },
    
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES = {
    "default": ALTERNATIVE_DBS[config("USERDB", default="sqlite3")],
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [
    BASE_DIR / "static",
]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')



# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')