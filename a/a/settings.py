import os
from pathlib import Path
from django.conf import settings

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-#6xidc@0k*^+2k3t@qyw%19+c=+st46pj5pjwb$d^q!^jqiw-e'

DEBUG = False

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = [
    'https://engil.ru',
]

# Приложения Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'data.apps.DataConfig',  # Ваше приложение
    'storages',  # Для работы с S3
    'django.contrib.sitemaps',
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
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# Настройки базы данных (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'default_db',
        'USER': 'gen_user',
        'PASSWORD': r'R\4^=7n?q,Y\r<',
        'HOST': '176.124.213.20',
        'PORT': '5432',
        'CONN_MAX_AGE': 600,  # 10 минут
        'OPTIONS': {
            'connect_timeout': 30,  # Время ожидания подключения
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Настройки Timeweb S3
AWS_ACCESS_KEY_ID = 'W9IPVPSXMBZ12O416SA7'  # Ваш Access Key
AWS_SECRET_ACCESS_KEY = 'oKKCaatpAzsLlBUFvOnbAH021mCJfa5WTxB5v64d'
AWS_STORAGE_BUCKET_NAME = '23b150f1-bc6e7174-c901-4463-91a6-db6756f1714d'
AWS_S3_REGION_NAME = 'ru-1'
AWS_S3_ENDPOINT_URL = 'https://s3.timeweb.cloud'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.timeweb.cloud'

# Переменная для хранения идентификатора сайта (может быть доменом, ID и т.д.)
SITE_ID = '001'  # Можете задать динамически, например, через конфигурацию сайта

# Кастомные классы для статики и медиафайлов с папкой ID сайта перед /static/ и /media/
STATICFILES_STORAGE = 'data.custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'data.custom_storages.MediaStorage'

# URLs для статики и медиа (с учетом переменной SITE_ID)
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{SITE_ID}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{SITE_ID}/media/'

# Локальная директория для статики (если нужно)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'data', 'static'),  # Путь к статическим файлам приложения
]

# Директория для статики (если DEBUG=True)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Указываем путь для медиафайлов
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Автоматическое создание ID для полей
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройки для формирования пути
STATICFILES_LOCATION = f'{SITE_ID}/static'
MEDIAFILES_LOCATION = f'{SITE_ID}/media'
