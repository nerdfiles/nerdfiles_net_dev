# -*- coding: utf-8 -*-

import os

# == VENV ======================================== #

VENV_ROOT = os.path.join('Users','nerdfiles','.virtualenvs','nerdfiles_net_dev')
# VENV_ROOT = os.path.join('')


# == SETTINGS: OVERRIDES ======================================= #

try:
  from settings_dev import *
except ImportError:
  pass


# == DEBUG == #

LOCAL_DEVELOPMENT = True
DEBUG = False
TEMPLATE_DEBUG = DEBUG


