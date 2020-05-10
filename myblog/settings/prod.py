import dj_database_url

from myblog.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY','*g=cd&_vkcq*&a_*3git5qi-f(w^sr+egwat4if4ux3&z3^t5(')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'myblog-amsada.herokuapp.com',
    'amadousy.pythonanywhere.com',
    'www.dev-up.tech',
]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {'default': dj_database_url.config(conn_max_age=600)}

print("secret key", SECRET_KEY)