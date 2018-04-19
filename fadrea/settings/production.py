from .base import *
import dj_database_url

DEBUG = False

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = ['*']

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = ('rest_framework.renderers.JSONRenderer',)

SECRET_KEY = env('DJANGO_SECRET_KEY', default='w0s^mlsma#ryx@h+vu5qea^@im-u)50xvud&swa68)sv8kax9g')
