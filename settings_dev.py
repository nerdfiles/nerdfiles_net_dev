# -*- coding: utf-8 -*-

import os

# == VENV ======================================== #

VENV_ROOT = os.path.join('home','nerdfiles','.virtualenvs','nerdfiles_net_dev')
# VENV_ROOT = os.path.join('')


# == DEBUG == #

LOCAL_DEVELOPMENT = False
DEBUG = False
TEMPLATE_DEBUG = DEBUG


# == DB ======================================= #

DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2'
DATABASE_NAME = 'nerdfiles_website'
DATABASE_USER = 'nerdfiles_website'
DATABASE_PASSWORD = 'f0xf0x0!6'
#DATABASE_HOST = 'localhost'
#DATABASE_PORT = '5432'
DATABASE_HOST = ''
DATABASE_PORT = ''


