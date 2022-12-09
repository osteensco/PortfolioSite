"""
Django settings for portfolio_site project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""


import os
import django_heroku
import subprocess
import dj_database_url
from pathlib import Path





# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')


if os.environ.get('DJANGO_DEBUG_VALUE') == 'False':
    DEBUG = False
    SECURE_SSL_REDIRECT = True
else:
    DEBUG = True
    

# DEBUG_PROPAGATE_EXCEPTIONS = True #use for reading error messages if DEBUG = False

ALLOWED_HOSTS = [
    'osteensco-portfolio-site.herokuapp.com',
    'scottosteen.com',
    'www.scottosteen.com',
    '127.0.0.1.'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio_site.wsgi.application'



DATABASES = {}

cmd = "heroku config:get DATABASE_URL" #heroku cli has to be configured for your project, otherwise need to add -a [app name]

heroku_db = subprocess.run(cmd, capture_output=True, shell=True, text=True, input="y")#if manage.py commands get hung up with no error until cancelling(crtl+c), manually log into heroku cli('heroku login' in terminal) and retry

DATABASES['default'] = dj_database_url.config(default=heroku_db.stdout, conn_max_age=600, ssl_require=True) #pulls in env variable and sets default connection to heroku DB automatically



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True










AWS_ACCESS_KEY_ID = os.environ.get('DJAWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('DJAWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('DJAWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = f'''{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'''

AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {'Access-Control-Allow-Origin': '*'}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'


STATIC_URL = f'''https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'''
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


django_heroku.settings(locals(), staticfiles=False)
