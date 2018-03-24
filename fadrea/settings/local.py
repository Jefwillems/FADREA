from .base import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fadrea',
        'USER': 'fadreauser',
        'PASSWORD': 'fadreapass',
        'HOST': 'localhost',
        'PORT': '',
    }
}
