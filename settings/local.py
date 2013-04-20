# -*- coding: utf-8 -*-

import os
from prod import *

LOCAL_DEVELOPMENT = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

VENV_ROOT = os.path.join('Users','nerdfiles','.virtualenvs','nerdfiles_net_dev')
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
