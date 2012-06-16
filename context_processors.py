#!/usr/bin/env python

# == IMPORTS ======================================== #

from django.conf import settings
from django.contrib.sites.models import Site


# == CONTEXT PROCESSORS ======================================== #

def site_info(request):
  domain = Site.objects.get_current().domain

  if domain == 'example.com':
    domain = 'localhost:8000'

  http_host = request.META.get('HTTP_HOST', '')

  return { 
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

