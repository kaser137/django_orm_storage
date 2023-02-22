import os
from pathlib import Path
from environs import Env

env = Env()
env.read_env(Path('venv', '.env'))
user = env.str('USER')
password = env.str('PASSWORD')
engine = env.str('ENGINE')
host = env.str('HOST')
port = env.str('PORT')
name = env.str('NAME')

DATABASES = {
    'default': {
        'ENGINE': engine,
        'HOST': host,
        'PORT': port,
        'NAME': name,
        'USER': user,
        'PASSWORD': password
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str('SECRET_KEY', default='')

DEBUG = env.bool('DEBUG', default=True)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
