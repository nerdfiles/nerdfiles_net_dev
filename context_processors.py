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
from datetime import datetime
from django.core.cache import cache
import twitter
from kippt import kippt_wrapper


# == CONTEXT PROCESSORS ======================================== #

def kippt_saves(request):
  k = kippt_wrapper.user('%s' % settings.KIPPT_API_USER,'%s' % settings.KIPPT_API_TOKEN)

  kippt_saves = cache.get('kippt_saves')
  if kippt_saves:
    return {
      "kippt_saves": kippt_saves[1]
    }
    
  kippt_saves = k.search('#!', limit=2)
  cache.set(
    'kippt_saves', 
    kippt_saves, 
    settings.KIPPT_TIMEOUT
  )
  return {
    "kippt_saves": kippt_saves[1],
    "kippt_authed": k.checkAuth()
  }

def latest_tweet(request):
  tweet = cache.get( 'tweet' )

  if tweet:
    return {
      "tweet": tweet
    }

  tweet = twitter.Api().GetUserTimeline( settings.TWITTER_USER )[0]
  tweet.date = datetime.strptime( tweet.created_at, "%a %b %d %H:%M:%S +0000 %Y" )
  cache.set( 'tweet', tweet, settings.TWITTER_TIMEOUT )

  return {
    "tweet": tweet
  }

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

