# -*- coding: utf-8 -*-

# == ALBUM ======================================= #

"""
  A Lily - Wake:Sleep
  @url http://dynamophone.com/videos/a-lily-wakesleep/
"""

# == PROJECT ======================================= #

"""
  @project          nerdfiles.net
  @contributor      Aharon Alexander (nerdfiles@gmail.com)
  @datetime         19 2013 04 20:37:48
"""

# == IMPORTS ======================================= #

from django.conf import settings
import os, sys, datetime
import logging


# == UTIL ======================================= #

PROJECT_ROOT = os.path.dirname(__file__)
DIRNAME = os.path.dirname(os.path.abspath(__file__))
_ = lambda s: s


# == DEVELOPMENT/DEBUGGING ======================================= #

LOCAL_DEVELOPMENT = False
DEBUG = False
TEMPLATE_DEBUG = DEBUG


# == ADMIN/GENERAL ======================================= #

SITE_ID = 1

ADMINS = (
  ('nerdfiles', 'nerdfiles@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'

SITE_ID = 2

INTERNAL_IPS = ('127.0.0.1',)

if LOCAL_DEVELOPMENT:
  HOSTNAME = 'http://localhost:8000'
else:
  HOSTNAME = 'http://nerdfiles.net'


# == LANGUAGE ======================================= #

LANGUAGE_CODE = 'en-us'
LANGUAGES = [('en', 'en'),]
DEFAULT_LANGUAGE = 0


# == I18N ======================================= #

USE_I18N = True


# == LOCALIZATION ======================================= #

USE_L10N = True


# == URLCONF ======================================= #

ROOT_URLCONF = 'nerdfiles_net_dev.urls'


# == DB ======================================= #

'''DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2'
DATABASE_NAME = 'nerdfiles_website'
DATABASE_USER = 'nerdfiles_website'
DATABASE_PASSWORD = 'f0xf0x0!6'
#DATABASE_HOST = 'localhost'
#DATABASE_PORT = '5432'
DATABASE_HOST = ''
DATABASE_PORT = ''
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nerdfiles_website',
        'USER': 'nerdfiles_website',
        'PASSWORD': 'f0xf0x0!6',
        #'HOST': 'localhost',
        #'PORT': '1540',
    }
}


# == URL ======================================= #

# == media url == #

MEDIA_URL = '/_assets/'

# == admin media == #

ADMIN_MEDIA_PREFIX = '/_static/admin/'


# == THEME/TEMPLATE/MEDIA ======================================= #

THEME = "nerdfiles_net_dev"
THEME_DIR = os.path.join(PROJECT_ROOT, "themes", THEME)

TEMPLATE_DIRS = (
  #os.path.join(PROJECT_ROOT, "themes",),
  os.path.join(PROJECT_ROOT, "themes", THEME, "_templates"),
)

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "themes", THEME, "_assets")

STATIC_ROOT = os.path.join(PROJECT_ROOT, "themes", THEME, "_static")
STATIC_URL = '/_static/'

if LOCAL_DEVELOPMENT:
  ASSETS_URL = '/_assets/'
else:
  ASSETS_URL = '/_static/'


STATICFILES_DIRS = (
  #("_static", os.path.join(PROJECT_ROOT, "themes", THEME, "_assets")),
)

STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
  'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# == TEMPLATE LOADERS ======================================= #

TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
  'django.template.loaders.eggs.Loader',
)


# == TEMPLATE LOADERS ======================================= #

TEMPLATE_CONTEXT_PROCESSORS = (
 
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.request',
  #'django.core.context_processors.auth',

  #'django.core.context_processors.auth',
  #'django.contrib.auth.context_processors.auth',
 
  'django.core.context_processors.i18n',
  #'django.core.context_processors.request',
  'django.core.context_processors.media',
  'django.core.context_processors.static',

  'cms.context_processors.media',
  'sekizai.context_processors.sekizai',
  
  'context_processors.site_info',
  #'context_processors.lastfm',
  'context_processors.kippt_rss',

  #'context_processors.latest_tweet',
  #'context_processors.kippt_saves',
)


# == MIDDLEWARE CLASSES ======================================= #

MIDDLEWARE_CLASSES = (

  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',

  'cms.middleware.user.CurrentUserMiddleware',
  'cms.middleware.page.CurrentPageMiddleware',
  'cms.middleware.toolbar.ToolbarMiddleware',

  'django.middleware.cache.UpdateCacheMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.cache.FetchFromCacheMiddleware',

  #'cms.middleware.multilingual.MultilingualURLMiddleware',
  #'djangologging.middleware.LoggingMiddleware',
  #'djangologging.middleware.SuppressLoggingOnAjaxRequestsMiddleware',
)


# == INSTALLED APPS ======================================= #

INSTALLED_APPS = (

  #'south',

  # == core == #
  'django.contrib.auth',
  'django.contrib.admin',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.messages',
  'django.contrib.staticfiles',
 
  # == django cms == #
  'cms',
  'menus',
  'mptt',
  'cms.plugins.text',
  'cms.plugins.picture',
  'cms.plugins.link',
  'cms.plugins.file',
  'cms.plugins.snippet',
  'cms.plugins.googlemap',
  'sekizai',
 
  # == apps == #
  'notification',
  #'lastfm',
  #'south',
  'django_extensions',
  'django_memcached',

  # == admin == #
  'django.contrib.admin',
  'django.contrib.admindocs',

  'analytical',
  'utils',
  'templateaddons',

  'nerdfiles_net_dev',
)

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

CMS_MEDIA_PATH = 'cms/'
CMS_MEDIA_ROOT = MEDIA_ROOT + CMS_MEDIA_PATH
CMS_MEDIA_URL = MEDIA_URL + CMS_MEDIA_PATH
CMS_TEMPLATES = (
  
  # errors
  ('404.tmpl', 'Template: 404 (not found)'),
  ('500.tmpl', 'Template: 500 (generic error)'),
  
  # standards
  ('tmpl-base.tmpl', 'Template: Base'),

  # home
  ('tmpl-home-base.tmpl', 'Template: Homepage (landing)'),
  
  # pages
  ('tmpl-single-base.tmpl', 'Single Template: Base'), # presentation of generic single content
  
  # forms
  ('tmpl-form-base.tmpl', 'Form Template: Base'),
  ('tmpl-form-hello.tmpl', 'Form Template: Hello (contact)'),
  ('tmpl-form-locate.tmpl', 'Form Template: Locate (wtf iz dis?)'),
  
  # aggregates
  ('tmpl-list-base.tmpl', 'List Template: Base'),
  
)


# == APP: DEBUG TOOLBAR ======================================= #
"""
  @see http://pypi.python.org/pypi/django-debug-toolbar/
"""
if DEBUG:
  MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
  INSTALLED_APPS += ('debug_toolbar',)

  DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
  )

  def custom_show_toolbar(request):
    return True

  DEBUG_TOOLBAR_CONFIG = {
    'MEDIA_URL': '/_static/debug_toolbar/',
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
  }


# == APP: PIL ======================================= #
"""
  @see http://www.pythonware.com/products/pil/
"""

PIL_IMAGEFILE_MAXBLOCK = 1024 * 2 ** 10


# == EMAIL SETTINGS ======================================= #

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# == LOGGING ======================================= #

#import loggly_logger

LOGGING = {
  'version': 1,
  'disable_existing_loggers': True,
  'formatters': {
    'standard': {
      'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    },
    'verbose': {
      'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
    },
    'simple': {
      'format': '%(levelname)s %(message)s'
    },
  },
  'handlers': {
    'file': {
      'level': 'INFO',
      'class': 'logging.handlers.RotatingFileHandler',
      'filename': os.path.join(PROJECT_ROOT, 'log', 'requests.log'),
      'maxBytes': 1024*1024*5, # 5MB
      'backupCount': 10,
      'formatter': 'standard'
    },
    'file_userlogins': {              # define and name a handler
      'level': 'DEBUG',
      'class': 'logging.FileHandler', # set the logging class to log to a file
      'formatter': 'verbose',         # define the formatter to associate
      'filename': os.path.join(PROJECT_ROOT, 'log', 'userlogins.log') # log file
    },
    'file_usersaves': {               # define and name a second handler
      'level': 'DEBUG',
      'class': 'logging.FileHandler', # set the logging class to log to a file
      'formatter': 'verbose',         # define the formatter to associate
      'filename': os.path.join(PROJECT_ROOT, 'log', 'usersaves.log')  # log file
    },
  },
  'loggers': {
    'django.request': {
      'handlers': ['file'],
      'level': 'INFO',
      'propagate': False,
    },
    'logview.userlogins': {            # define a logger - give it a name
      'handlers': ['file_userlogins'], # specify what handler to associate
      'level': 'INFO',                 # specify the logging level
      'propagate': True,
    },     

    'logview.usersaves': {             # define another logger
      'handlers': ['file_usersaves'],  # associate a different handler
      'level': 'INFO',                 # specify the logging level
      'propagate': True,
    },        
  }       
}


# == CACHING ======================================= #

CACHES = {
  'default': {
    'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    'LOCATION': '127.0.0.1:11211',
  }
}

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_TIMEOUT = 3600*48/60 # 2880 minutes; two days (24 hours)
CACHE_PREFIX = "Z"
