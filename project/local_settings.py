import os
import pylast

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

TIME_ZONE = 'America/Chicago'

SECRET_KEY = 'yf0jkw+brbcv)t50m37agmggdq7@vv03(f5l145duhxk@e3hub'

DEBUG_APPS = ()

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    'localhost/',
)

KIPPT_TIMEOUT = 3600*4
KIPPT_API_USER = 'nerdfiles'
KIPPT_API_TOKEN = 'cb08721433031016984ebc269e4f07e0a1d8ce4b'

TWITTER_USER = "filesofnerds"
TWITTER_TIMEOUT = 3600*4

LASTFM_USER = "wittysense"
LASTFM_PASS = pylast.md5("f0xf0x0!6")
LASTFM_API_KEY = "4c84847605bf2fd159d3aa5277ef2f32"  # this is a sample key
LASTFM_API_SECRET = "15097744590f54e0f9df2c8c5bee4cd0"
