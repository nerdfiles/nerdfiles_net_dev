# -*- coding: utf-8 -*-

# == IMPORTS ======================================== #

from django.conf import settings
from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse
from django import http
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.template import loader, Context
from django.template.context import RequestContext
from django.views.generic.simple import direct_to_template
from django.views.generic.simple import redirect_to
from django.views.generic import DetailView, ListView
from django.http import Http404
from sekizai.context import SekizaiContext
from django.template import RequestContext
import logging

from django.core.cache import cache
#from django.core import serializers
#from django.utils import simplejson
import json

if settings.LOCAL_DEVELOPMENT:
  import pdb

# lastfm API
from settings import API_KEY, API_SECRET, username, password_hash
import pylast

# == VIEWS ======================================== #



def render_response(request, *args, **kwargs):
  kwargs['context_instance'] = RequestContext(request)
  return render_to_response(*args, **kwargs)

def tumblr_redirect(request):
  return redirect('http://wittysense.tumblr.com/')

def lastfm_recent_tracks(request):
  #cache
  lfm_data = cache.get('lfm_data')
  TIMEOUT = 3600*48/60 # two days (48 hours)
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
  track_data = ["%s - %s" % (tr.get_artist(), tr.get_title()) for tr in lfm_data]
  #need to convert list to json
  #must list comp to grab only track and artist unicode data
  #if track_data:
  #  data = json.dumps(track_data)

  #set cache for next time
  cache.set(
    "lfm_data",
    track_data,
    TIMEOUT
  )
  #pdb.set_trace()

  #pprint(lfm_data)

  #load raw
  return HttpResponse(track_data, mimetype='application/json')

def error_404(request):
  return render_response(request, '404.tmpl')

def error_500(request):
  return render_response(request, '500.tmpl')
