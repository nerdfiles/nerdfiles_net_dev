

import os
import sys

import site
from os import urandom

site.addsitedir('/home/nerdfiles/.virtualenvs/jangy177/lib/python2.7/site-packages')

#from django.core.handlers.wsgi import WSGIHandler
from django.core.wsgi import get_wsgi_application




path = '/home/nerdfiles/webapps/jangy177/nerdfiles_net_dev/'
if path not in sys.path:
  sys.path.append(path)
  os.chdir(path)





os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

activate_this = os.path.expanduser("/home/nerdfiles/.virtualenvs/jangy177/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

project = '/home/nerdfiles/webapps/jangy177/nerdfiles_net_dev/'
sys.path.insert(0, project)
workspace = os.path.dirname(project)
sys.path.append(workspace)

#application = WSGIHandler()
application = get_wsgi_application()

'''
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
'''
