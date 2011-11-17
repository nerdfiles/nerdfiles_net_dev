# -*- coding: utf-8 -*-

# == IMPORTS ======================================== #

from view_utils import *
from django.conf import settings
from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse
from django import http
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import loader, Context
from django.template.context import RequestContext
from django.views.generic.simple import direct_to_template
from django.views.generic.simple import redirect_to
from django.views.generic import DetailView, ListView
from django.http import Http404
from sekizai.context import SekizaiContext
from django.template import RequestContext
import logging


# == VIEWS ======================================== #



def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)

def error_404(request):
  return render_response('404.tmpl')

def error_500(request):
  return render_response('500.tmpl')
