"""
Django settings for efs project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ts-q2k)i!dmia=a_manz0@(is)f#y^6ss^%xypert6&2dl9ihv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'students',
    'courses',
    'cart',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
    'feedback',
    'embed_video',
    'instructors',
    'storages',
    'social_django',
]



AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',

)


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'educa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # custom
                'courses.context_processors.categories_processor',
                'cart.context_processors.cart',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'educa.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd3q720d1sgtnt6',
        'USER': 'knviwnpolowqoc',
        'PASSWORD': '9d9cf4ca6eb3de4df096a426699a827556da2fa563586db24ec55c3e4bb8084e',
        'HOST': 'ec2-54-243-208-234.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "static"),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
DATABASES['default'] = dj_database_url.config()

AUTH_USER_MODEL = 'account.User'

CART_SESSION_SLUG = 'cart'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL_HOST = 'smtp.mailtrap.io'
# EMAIL_HOST_USER = 'c111ea088cc2c8'
# EMAIL_HOST_PASSWORD = '46c051c8a44daf'
# EMAIL_PORT = '2525'

SEND_GRID_API_KEY = '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'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'Priya0318'
EMAIL_HOST_PASSWORD = 'Priya@0318' #sendgrid email
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'MYEMAIL'

# Braintree settings
BRAINTREE_MERCHANT_ID = 'cypz6hm4gv5z79gk'
BRAINTREE_PUBLIC_KEY = 'bqytzq85md6mfnpb'
BRAINTREE_PRIVATE_KEY = '7f0a9bf1133c4a72ea9e11b58e29aac5'

from braintree import Configuration, Environment

Configuration.configure(
    Environment.Sandbox,
    # Environment.Production,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)

try:
    from .local_settings import *
except ImportError:
    pass

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '612615452253-s84u3ebk5cn4scufnqiumqo5lagf6vqt.apps.googleusercontent.com'

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'QThrD35QGGHdkJX47MU-eCva'

SOCIAL_AUTH_FACEBOOK_KEY = '441884003206783'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '9a5927cfb87e14d64694e030426e9e62'  # App Secret

LOGIN_URL = '/auth/login/google-oauth2/'


# AWS_ACCESS_KEY_ID = 'AKIAIYIJ43FDMKTHUMNQ'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'fablab-t3'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = 'static'
#
# AWS_DEFAULT_ACL = None
#
#
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
#
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'