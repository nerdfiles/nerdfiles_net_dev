# -*- coding: utf-8 -*-

import os

# == VENV ======================================== #

# VENV_ROOT = os.path.join('','nerdfiles','.virtualenvs','nerdfiles_net_dev')
# VENV_ROOT = os.path.join('')


# == DEBUG == #

LOCAL_DEVELOPMENT = True
DEBUG = False
TEMPLATE_DEBUG = DEBUG


# == DB ======================================= #

"""
  @engines 'postgresql_psycopg2'|'postgresql'|'mysql'|'sqlite3'|'oracle'
  @note If using local settings, this will be overridden.
"""

DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASE_NAME = 'dev.db'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

'''
DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2'
DATABASE_NAME = 'nerdfiles_website'
DATABASE_USER = 'nerdfiles'
DATABASE_PASSWORD = 'cbc8416e'
'''


