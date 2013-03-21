# -*- coding: utf-8 -*-

# == IMPORTS ======================================== #

from django.conf import settings
from django.conf.urls.defaults import *
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

if settings.LOCAL_DEVELOPMENT:
  import pdb

# lastfm API
from settings import API_KEY, API_SECRET, username, password_hash


# == VIEWS ======================================== #



def render_response(request, *args, **kwargs):
  kwargs['context_instance'] = RequestContext(request)
  return render_to_response(*args, **kwargs)

def tumblr_redirect(request):
  return redirect('http://wittysense.tumblr.com/')

def twitter_recent_tweets(request):
  import requests
  from django.core.cache import cache
  from pprint import pprint
  import json
  tw_data = cache.get('tw_data')
  TIMEOUT = 2880*2
  if tw_data:
    return HttpResponse(tw_data, mimetype='application/json')

  # tw_data
  r = requests.get('http://twitter.com/users/show.json?screen_name=filesofnerds', 
        auth=('filesofnerds', 'thec4tisonthem4t'))

  #pprint(r)
  #print r.status_code
  #print r.text

  tw_data = []

  data = json.dumps(tw_data)

  cache.set(
    'tw_data',
    data,
    TIMEOUT
  )

  return HttpResponse(data, mimetype='application/json')

def lastfm_recent_tracks(request):
  import pylast
  import json
  from django.core.cache import cache
  #cache
  lfm_data = cache.get('lfm_data')
  TIMEOUT = 2880*2 # two days (48 hours)
  if lfm_data:
    return HttpResponse(lfm_data, mimetype='application/json')

  network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = 
      API_SECRET, username = username, password_hash = password_hash)

  network.enable_caching()

  user_data = network.get_user('wittysense')
  r_tracks = user_data.get_recent_tracks(limit=5)
  recent_tracks = [r.track for r in r_tracks]

  #raw
  lfm_data = recent_tracks
  #for tr in lfm_data:
    #print dir(tr)
  track_data = ["%s - %s on '%s'" % (tr.get_artist(), tr.get_title(), tr.get_album()) for tr in lfm_data]
  #need to convert list to json
  #must list comp to grab only track and artist unicode data
  if track_data:
    data = json.dumps(track_data)

  #set cache for next time
  cache.set(
    "lfm_data",
    data,
    TIMEOUT
  )
  #pdb.set_trace()

  #load raw
  return HttpResponse(data, mimetype='application/json')

def error_404(request):
  return render_response(request, '404.tmpl')

def error_500(request):
  return render_response(request, '500.tmpl')
