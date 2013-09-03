import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    )
}

ALLOWED_HOSTS = []

LANGUAGE_CODE = 'en'

SITE_ID = 1

USE_I18N = False

USE_L10N = True

USE_TZ = True

THEME = 'nerdfiles_net_dev'

MEDIA_ROOT = os.path.join(PROJECT_PATH, "..", "themes", THEME, "assets")
MEDIA_URL = '/assets/'
STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, '../static/'),
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
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'context_processors.site_info',
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

    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',

    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

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
    'app',
    'rest_framework.authtoken',
    'rest_framework',
    'south',
    'analytical',
    'sekizai',

    'cms',
    'menus',
    'mptt',

    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.teaser',
    'cms.plugins.text',
    'cms.plugins.video',
    'cms.plugins.twitter',

    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',

    'corsheaders',
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

try:
    from db_settings import *
except ImportError:
    pass

try:
    from local_settings import *
    INSTALLED_APPS += DEBUG_APPS
except ImportError:
    pass
