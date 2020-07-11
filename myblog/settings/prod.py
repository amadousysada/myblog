import dj_database_url

from myblog.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY','*g=cd&_vkcq*&a_*3git5qi-f(w^sr+egwat4if4ux3&z3^t5(')

# Setting for redirecting all unsecure connections (http) to https
# https://docs.djangoproject.com/en/2.2/topics/security/#ssl-https
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'myblog-amsada.herokuapp.com',
    'amadousy.pythonanywhere.com',
    'www.dev-up.tech',
]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}

CKEDITOR_UPLOAD_PATH = '/media/upload/'

#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_DEFAULT_ACL = 'public-read'
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False

