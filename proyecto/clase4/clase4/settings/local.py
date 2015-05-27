from .base import *

DEBUG = True
ALLOWED_HOSTS = []

WSGI_APPLICATION = 'clase4.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE'   : 'django.db.backends.postgresql_psycopg2',
        'NAME'     : 'clase4',
        'USER'     : 'root',
        'PASSWORD' : '123',
        'HOST'     : 'localhost',
        'PORT'     : '5432',

    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
