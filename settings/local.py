# -*- coding: utf-8 -*-
import os
VENV_ROOT = os.path.join('Users','nerdfiles','.virtualenvs','nerdfiles_net_dev')
ROOT_URLCONF = 'nerdfiles_net_dev.urls'
INSTALLED_APPS += ('nerdfiles_net_dev',)
LOCAL_DEVELOPMENT = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG
DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASE_NAME = 'nerdfiles_net_dev.db'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'nerdfiles_net_dev.db'
  }
}
