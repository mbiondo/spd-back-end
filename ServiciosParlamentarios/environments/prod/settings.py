"""
Django settings for ServiciosParlamentarios project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from datetime import date
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c8qmje5ow7r5e)uri*t^baev!*rw-a&z*=om5&op&pn872h&!5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'sslserver',
    'apirest',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'ServiciosParlamentarios.urls'

WSGI_APPLICATION = 'ServiciosParlamentarios.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'servicios',    #name of the django database
        'USER': 'postgres',     #user of the django database
        'PASSWORD': 'hLsPLeYRSR',       #password of the django database
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'pap_nueva_pruebas': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dp_prod', #PROD
        'USER': 'postgres',
        'PASSWORD': 'XBdFBU3hDGZe',
        'HOST': '186.33.210.54',
        'PORT': '5432',
    },
    'pap_nueva_pruebas_test': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dp_prod_test', #TEST
        'USER': 'postgres',
        'PASSWORD': 'XBdFBU3hDGZe',
        'HOST': '186.33.210.54',
        'PORT': '5432',
    }
}


# This is defined here as a do-nothing function because we can't import
# django.utils.translation -- that module depends on the settings.
gettext_noop = lambda s: s

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('es', gettext_noop('Spanish')),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
#     'DEFAULT_PERMISSION_CLASSES': ('apirest.authorizers.authorizator.has_permission',),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
        'apirest.filters.coalesce_filter_backend.CoalesceFilterBackend',
    ), #pip install django-filter
    'DEFAULT_RENDERER_CLASSES': (
        'apirest.utils.JSONURenderer.JSONURenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'PAGINATE_BY': 20,
    'PAGINATE_BY_PARAM': 'page_size',
    'MAX_PAGINATE_BY': 100
}

DATABASE_ROUTERS = ['apirest.routers.apirest_router.ApirestRouter','apirest.routers.default_router.DefaultRouter']

# Authentication Server
AUTH_SERVER = {
    'HOST': 'oauth2.hcdn.gob.ar',
    'PORT': '9000',
    'RESOURCE_NAME': 'servicios-parlamentarios',
}

# Oauth2 client credentials
AUTH_CLIENT_CREDENTIALS = {
    'CLIENT_ID': '=yEvTDB6GU34syMA0n63RD8OQxgCec6w32KDC9Am',
    'CLIENT_SECRET': '4BxxY7C4_jM!l4JlYe!1f;LuFRMf=!M;iabG;Mjad:hmnZ.Ma.Go=@9hYqIc5fwKAWg=rr_fxXW6bAP-iRUoZrTDK!fILZ;1u-nf@@ksDHKlX;k!h2jrGMQJ;F70!abw',
}

AUTHENTICATION = True

from datetime import datetime

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/ServiciosParlamentarios/' + datetime.now().strftime('ServiciosParlamentarios_%d_%m_%Y.log'),
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': True
        },
        'apirest': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True
        },
    },

}

