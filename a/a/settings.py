from pathlib import Path
import os
from django.conf import settings
from django.conf.urls.static import static
import psycopg2
from psycopg2 import OperationalError

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-#6xidc@0k*^+2k3t@qyw%19+c=+st46pj5pjwb$d^q!^jqiw-e'

DEBUG = False

ALLOWED_HOSTS = ['engil.ru']

CSRF_TRUSTED_ORIGINS = [
    'https://engil.ru',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'data.apps.DataConfig',
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

ROOT_URLCONF = 'a.urls'

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

WSGI_APPLICATION = 'a.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'default_db',
        'USER': 'gen_user',
        'PASSWORD': r'R\4^=7n?q,Y\r<',
        'HOST': '176.124.213.20',
        'PORT': '5432',  # Default PostgreSQL port
        'CONN_MAX_AGE': 600,  # Увеличивает время жизни соединения до 600 секунд (10 минут)
        'OPTIONS': {
            'connect_timeout': 30,  # Время ожидания подключения (в секундах)
        },
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'data/static')]
urlpatterns = [
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
