"""
Django settings for ServiciosParlamentarios project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c8qmje5ow7r5e)uri*t^baev!*rw-a&z*=om5&op&pn872h&!5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


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
    'rest_framework_swagger',
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
        'NAME': '', 	#name of the django database
        'USER': '',	#user of the django database
        'PASSWORD': '',	#password of the django database
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'pap_nueva_pruebas': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pap_nueva_folio', #PROD
        'USER': 'migracion',
        'PASSWORD': 'migr4ci@n',
        'HOST': '186.33.210.21',
        'PORT': '5432',
    },
    'pap_nueva_pruebas_test': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pap_nueva_folio', #TEST
        'USER': 'migracion',
        'PASSWORD': 'migr4ci@n',
        'HOST': '186.33.210.21',
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

TIME_ZONE = 'UTC'

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
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ), #pip install django-filter
    'DEFAULT_RENDERER_CLASSES': (
        'apirest.utils.JSONURenderer.JSONURenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'PAGINATE_BY': 20,
    'PAGINATE_BY_PARAM': 'page_size',
    'MAX_PAGINATE_BY': 100
}

SWAGGER_SETTINGS = {
    "exclude_namespaces": [], # List URL namespaces to ignore
    "api_version": '0.1',  # Specify your API's version
    "api_path": "/",  # Specify the path to your API not a root level
    "enabled_methods": [  # Specify which methods to enable in Swagger UI
        'get',
        'post',
        'put',
        'patch',
        'delete'
    ],
    "api_key": '', # An API key
    "is_authenticated": False,  # Set to True to enforce user authentication,
    "is_superuser": False,  # Set to True to enforce admin only access
}

DATABASE_ROUTERS = ['apirest.routers.apirest_router.ApirestRouter','apirest.routers.default_router.DefaultRouter']

# Authentication Server
AUTH_SERVER = {
    'HOST': '10.105.5.55',
    'PORT': '9000',
    'RESOURCE_NAME': 'servicios-parlamentarios',    
}

# Oauth2 client credentials
AUTH_CLIENT_CREDENTIALS = {
    'CLIENT_ID': 'b=5ScaFmagIxpaAriSV;.?P@AfzMdh7Y9LnRDukY',
    'CLIENT_SECRET': 'hyZGfL58D?K4hIeKvGx@9@QGFeKqpYq:GuPuynHTIEuie?:!SJOG!IYszh;=@ph1I4He0-.QZ:r=lWBAB1cr2a9nhp8iAySuNgDTcgn=C!pZHb7wiPPU!5Pim0k8apnk',
}

AUTHENTICATION = True

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },    
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    }
           
}
