# -*- coding: utf-8 -*-

from urls_sugar.utils import patterns, url_sugar
from urls_sugar.classes import Constant, Variable

# == CORE/DEBUGGING ============================================== #

DEBUG = True # True doesn't work; 500 errors, again

TEMPLATE_DEBUG = DEBUG

# ================================================================ #

LOCAL_DEVELOPMENT = True # False means work on the shared DB

'''
if LOCAL_DEVELOPMENT:
  try:
    from settings_pipeline import *
  except ImportError:
    pass
'''

'''
urlpatterns = patterns('',

  #url(r'^_assets(?P<path>.*)$', 'django.views.static.serve',
  url_sugar([Constant('web-cv'),
              #Variable('pk', '\d+'),
              Variable('slug', '[a-z0-9-]+', suffix=''),
            ], page_view, name='web-cv'), #docs (?P<pk>\d+) #thescienceoftheparticular

  #{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
  #url(r'^_static(?P<path>.*)$', 'django.views.static.serve',

  #{'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
  #url(r'', include('django.contrib.staticfiles.urls')),

) + urlpatterns
'''
