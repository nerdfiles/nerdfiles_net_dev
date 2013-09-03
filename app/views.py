from app.models import *
from app.serializers import *
from rest_framework import generics
from rest_framework import permissions
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext


def render_response(request, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(request)
    return render_to_response(*args, **kwargs)


class UserList(generics.ListCreateAPIView):
    """List all users or create a new User"""
    permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """Retrieve, update or delete a User instance."""
    permission_classes = (permissions.IsAuthenticated,)
    model = User
    serializer_class = UserSerializer


class AddressList(generics.ListCreateAPIView):
    """List all addresses or create a new Address"""
    permission_classes = (permissions.IsAuthenticated,)
    model = Address
    serializer_class = AddressSerializer


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete an Address."""
    permission_classes = (permissions.IsAuthenticated,)
    model = Address
    serializer_class = AddressSerializer


def kippt_clips(request):
    """call to kippt"""

    from django.core.cache import cache
    from kippt import kippt_wrapper
    from pprint import pprint

    k = kippt_wrapper.user('%s' %
                           settings.KIPPT_API_USER, '%s' % settings.KIPPT_API_TOKEN,)

    TIMEOUT = 2880 * 5  # ten days

    pprint(k)

def HomeView(request):
    '''
        Landing page view.
    '''


    context = {
        'CONTEXT': True
    }

    return render_response(request, 'base.tmpl.haml', context)

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
