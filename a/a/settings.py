import os
import boto3
from pathlib import Path

# Основная директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-#6xidc@0k*^+2k3t@qyw%19+c=+st46pj5pjwb$d^q!^jqiw-e'

DEBUG = False

ALLOWED_HOSTS = ['engil.ru', 'localhost', '127.0.0.1']

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
    'storages',
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

# Подключение к базе данных SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Загрузка базы данных из S3 перед запуском
AWS_ACCESS_KEY_ID = 'W9IPVPSXMBZ12O416SA7'
AWS_SECRET_ACCESS_KEY = 'oKKCaatpAzsLlBUFvOnbAH021mCJfa5WTxB5v64d'
AWS_STORAGE_BUCKET_NAME = '23b150f1-bc6e7174-c901-4463-91a6-db6756f1714d'
AWS_S3_REGION_NAME = 'ru-1'
AWS_S3_ENDPOINT_URL = 'https://s3.timeweb.cloud'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.timeweb.cloud'

# Настройка S3 для хранения статических и медиа файлов
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Функция для скачивания SQLite файла с S3
def download_sqlite_from_s3():
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    local_path = os.path.join(BASE_DIR, 'db.sqlite3')

    # Проверим, существует ли файл на S3 перед загрузкой
    try:
        s3.download_file(AWS_STORAGE_BUCKET_NAME, 'db.sqlite3', local_path)
        print(f"SQLite DB downloaded to {local_path}")
    except Exception as e:
        print(f"Error downloading SQLite DB: {e}")


# Функция для загрузки SQLite файла на S3
def upload_sqlite_to_s3():
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    local_path = os.path.join(BASE_DIR, 'db.sqlite3')

    try:
        s3.upload_file(local_path, AWS_STORAGE_BUCKET_NAME, 'db.sqlite3')
        print(f"SQLite DB uploaded to S3")
    except Exception as e:
        print(f"Error uploading SQLite DB: {e}")


# Вызываем функции для загрузки базы данных с S3
download_sqlite_from_s3()

# Можно добавить upload_sqlite_to_s3() для выгрузки данных в S3 после завершения работы приложения или при завершении процесса
