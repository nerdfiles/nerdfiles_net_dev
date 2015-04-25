import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    )
}

SECRET_KEY = '&9u2v1iwln==r#ld$pbkvjjh$)ek^-k8(e7nzbx9*qt(dqm64*'

LASTFM_API_KEY = '4c84847605bf2fd159d3aa5277ef2f32'
LASTFM_API_SECRET = '15097744590f54e0f9df2c8c5bee4cd0'
LASTFM_USER = 'wittysense'
LASTFM_PASS = 'sfeO46NcYmavPA=='

ALLOWED_HOSTS = []

LANGUAGE_CODE = 'en'

SITE_ID = 1

USE_I18N = False

USE_L10N = True

USE_TZ = True

THEME = 'nerdfiles_net_dev'

MEDIA_ROOT = os.path.join(PROJECT_PATH, "..", "themes", THEME, "assets")
MEDIA_URL = '/assets/'
STATIC_ROOT = os.path.join(PROJECT_PATH, '..', 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    MEDIA_ROOT,
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'cms.context_processors.cms_settings',
    'sekizai.context_processors.sekizai',
    'app.context_processors.site_info',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'corsheaders.middleware.CorsMiddleware',

    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',

    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, '../themes/%s/templates' % THEME),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'django.contrib.admin',
    'debug_toolbar',
    'rest_framework.authtoken',
    'rest_framework',
    'analytical',
    'sekizai',
    'treebeard',

    'cms',
    'menus',
    'mptt',

    'sorl.thumbnail',
    #'djangocms_text_ckeditor',
    #'djangocms_picture',
    #'djangocms_link',
    #'djangocms_file',
    #'djangocms_snippet', #potential security hazard @see http://docs.django-cms.org/en/latest/getting_started/installation/integrate.html
    #'djangocms_googlemap',
    #'djangocms_inherit',
    'django_extensions',

    'filer',
    'easy_thumbnails',
    'corsheaders',
    'utils',

    'app',
)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
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
    ('tmpl-single-base.tmpl', 'Single Template: Base'),
    # presentation of generic single content

    # forms
    ('tmpl-form-base.tmpl', 'Form Template: Base'),
    ('tmpl-form-hello.tmpl', 'Form Template: Hello (contact)'),
    ('tmpl-form-locate.tmpl', 'Form Template: Locate (wtf iz dis?)'),

    # aggregates
    ('tmpl-list-base.tmpl', 'List Template: Base'),

)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_TIMEOUT = 2880  # two days (24 hours)
CACHE_PREFIX = "Z"

DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False, }


try:
    from db_settings import *
except ImportError:
    pass

#try:
    #from local_settings import *
    #INSTALLED_APPS += DEBUG_APPS
#except ImportError:
    #pass

