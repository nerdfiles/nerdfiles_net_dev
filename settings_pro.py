# -*- coding: utf-8 -*-

# == ALBUM ======================================= #

"""
  ARTIST_NAME - ABLUM_NAME
  LINK
"""

# == PROJECT ======================================= #

"""
  @project          nerdfiles_net_dev
  @contributor      Aaron Alexander (nerdfiles@gmail.com)
  @datetime         11.4.2011.11.56.a
  @devlogin         admin/admin
"""

# == IMPORTS ======================================= #

from django.conf import settings
import os, sys, datetime
import posixpath
import logging


# == UTIL ======================================= #

PROJECT_ROOT = os.path.dirname(__file__)
DIRNAME = os.path.dirname(os.path.abspath(__file__))
_ = lambda s: s


# == pythonpath inserts == #

# local
 
#sys.path.insert(0, PROJECT_ROOT)
#sys.path.insert(1, os.path.join(PROJECT_ROOT, "djangologging"))

# apache mod_wsgi

#sys.path.append(PROJECT_ROOT)
#sys.path.append(os.path.join(PROJECT_ROOT, "djangologging"))


# == VENV ======================================== #

# VENV_ROOT = os.path.join('Users','nerdfiles','.virtualenvs','nerdfiles_net_dev')
# VENV_ROOT = os.path.join('')
#
# @note Not sure where wf sets this. $ $HOME/virtualenv most likely.


# == DEVELOPMENT/DEBUGGING ======================================= #

LOCAL_DEVELOPMENT = False
DEBUG = False
TEMPLATE_DEBUG = DEBUG


# == ADMIN/GENERAL ======================================= #

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

ROOT_URLCONF = 'nerdfiles_net.urls'


# == URL ======================================= #

# == media url == #

MEDIA_URL = '/_assets/'

# == admin media == #

ADMIN_MEDIA_PREFIX = '/_static/admin/'


# == THEME/TEMPLATE/MEDIA ======================================= #

# == theme == #

THEME = "nerdfiles_net_dev"
THEME_DIR = os.path.join(PROJECT_ROOT, "_themes", THEME)

# == template == #

TEMPLATE_DIRS = (
  #os.path.join(PROJECT_ROOT, "_themes",),
  os.path.join(PROJECT_ROOT, "_themes", THEME, "_templates"),
)

# == media == #

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "_themes", THEME, "_assets")

# == static == #

STATIC_ROOT = os.path.join(PROJECT_ROOT, "_themes", THEME, "_static")
STATIC_URL = '/_static/'

if LOCAL_DEVELOPMENT:
  ASSETS_URL = '/_assets/'
else:
  ASSETS_URL = '/_static/'


# == STATIC ======================================= #

STATICFILES_DIRS = (
  ("_static", os.path.join(PROJECT_ROOT, "_themes", THEME, "_assets")),
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
  'django.core.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'django.core.context_processors.media',
  'django.core.context_processors.static',
  'cms.context_processors.media',
  'sekizai.context_processors.sekizai',
  'context_processors.site_info',
)


# == MIDDLEWARE CLASSES ======================================= #

MIDDLEWARE_CLASSES = (
  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  #'cms.middleware.multilingual.MultilingualURLMiddleware',
  'cms.middleware.page.CurrentPageMiddleware',
  'cms.middleware.user.CurrentUserMiddleware',
  'cms.middleware.toolbar.ToolbarMiddleware',
    
  #'djangologging.middleware.LoggingMiddleware',
  #'djangologging.middleware.SuppressLoggingOnAjaxRequestsMiddleware',
)


# == INSTALLED APPS ======================================= #

INSTALLED_APPS = (

  #'south',

  # == core == #
  'django.contrib.admin',
  'django.contrib.auth',
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
  'south',
  'django_extensions',

  # == admin == #
  'django.contrib.admin',
  'django.contrib.admindocs',

  'analytical',

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
  ('tmpl-home-base.tmpl', 'Template: Homepage'),
  
  # pages
  ('tmpl-single-base.tmpl', 'Single Template: Base'), # presentation of generic single content
  
  # forms
  ('tmpl-form-base.tmpl', 'Form Template: Base'),
  
  # aggregates
  ('tmpl-list-base.tmpl', 'List Template: Base'),
  
)


# == APP: LASTFM ======================================= #

LASTFM_USER = 'wittysense'
LASTFM_API_KEY = '4c84847605bf2fd159d3aa5277ef2f32'
# Available types: recent_tracks, weekly_top_artists, top_artists
LASTFM_CHART_TYPE = 'weekly_top_artists'
LASTFM_WIDGET_TITLE = 'This Week'
LASTFM_NUM_IMAGES = '5'
LASTFM_TOP_ARTISTS_PERIOD = '7day'
# Available sizes: small, medium, large, extralarge
LASTFM_IMG_SIZE = 'medium'


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
      'filename': os.path.join(PROJECT_ROOT, '_log', 'requests.log'),
      'maxBytes': 1024*1024*5, # 5MB
      'backupCount': 10,
      'formatter': 'standard'
    },
    'file_userlogins': {              # define and name a handler
      'level': 'DEBUG',
      'class': 'logging.FileHandler', # set the logging class to log to a file
      'formatter': 'verbose',         # define the formatter to associate
      'filename': os.path.join(PROJECT_ROOT, '_log', 'userlogins.log') # log file
    },
    'file_usersaves': {               # define and name a second handler
      'level': 'DEBUG',
      'class': 'logging.FileHandler', # set the logging class to log to a file
      'formatter': 'verbose',         # define the formatter to associate
      'filename': os.path.join(PROJECT_ROOT, '_log', 'usersaves.log')  # log file
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
CACHE_TIMEOUT = 60*30
CACHE_PREFIX = "Z"


# == DEBUG == #

LOCAL_DEVELOPMENT = False
DEBUG = False
TEMPLATE_DEBUG = DEBUG


# == SETTINGS: OVERRIDES ======================================= #

try:
  from settings_dev import *
except ImportError:
  pass

try:
  from settings_loc import *
except ImportError:
  pass

INSTALLED_APPS += ('nerdfiles_net',)
