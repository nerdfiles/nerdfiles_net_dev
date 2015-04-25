# -*- coding: utf-8 -*-

#from prod import *
from core import *

LOCAL_DEVELOPMENT = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'nerdfiles_net_dev.db'
  }
}
