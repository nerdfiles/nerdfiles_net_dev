# -*- coding: utf-8 -*-

# == SETTINGS: ENVIRONMENT == #

try:
  from settings_pro import *
except ImportError:
  pass


# == SETTINGS: LOCAL == #

try:
  from settings_loc import *
except ImportError:
  pass


'''
  DEV
'''

# == DEBUG == #

LOCAL_DEVELOPMENT = True
DEBUG = False
TEMPLATE_DEBUG = DEBUG


