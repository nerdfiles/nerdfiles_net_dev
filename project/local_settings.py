
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('nerdfiles', 'nerdfiles@gmail..com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nerdfiles_net',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

TIME_ZONE = 'America/Denver'

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

SECRET_KEY = 'yf0jkw+brbcv)t50m37agmggdq7@vv03(f5l145duhxk@e3hub'

DEBUG_APPS = ()

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    'localhost/',
)
