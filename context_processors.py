#!/usr/bin/env python

# == IMPORTS ======================================== #

from django.conf import settings
from django.contrib.sites.models import Site
from lastfm import views
from lastfm.views import *
from pprint import pprint
from StringIO import StringIO
from django.utils.safestring import SafeString
import json


# == CONTEXT PROCESSORS ======================================== #

def lastfm(request):
  lfm_data = views.lastfm_data(request)
  lfm_data = lfm_data.content
  return {
    'rt': json.loads(lfm_data)
  }

def site_info(request):
  domain = Site.objects.get_current().domain
  http_host = request.META.get('HTTP_HOST')

  if domain == 'example.com':
    domain = http_host

  if settings.LOCAL_DEVELOPMENT: 
    #domain = 'localhost:8001'
    settings.ASSETS_URL = '/_assets/'

  return { 
    'LOCAL': settings.LOCAL_DEVELOPMENT,
    'SITE_URL': 'http://' + domain + '/',
    'ASSETS_URL': 'http://' + domain + settings.ASSETS_URL,
  }

def google_analytics(request):

    if not settings.GA_PATH:
        return {}

    f = None
    try:
        f = file(settings.GA_PATH)
        GA_CODE = f.read()
    finally:
        if f is not None:
            f.close()

    return dict(GA_CODE=GA_CODE)

