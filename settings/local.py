# -*- coding: utf-8 -*-

#from prod import *
from core import *

LOCAL_DEVELOPMENT = False
DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))


DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(PROJECT_PATH,'nerdfiles_net_dev.db'),
  }
}
