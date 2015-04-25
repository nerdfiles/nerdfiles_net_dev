import os
import sys
import site
from os import urandom

site.addsitedir('/Users/nerdfiles/.pyenv/versions/django_nerdfiles_net/lib/python2.7/site-packages')

from django.core.wsgi import get_wsgi_application

path = '/Users/nerdfiles/Projects/nerdfiles_net/'
if path not in sys.path:
  sys.path.append(path)
  os.chdir(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

activate_this = os.path.expanduser("/Users/nerdfiles/.pyenv/versions/django_nerdfiles_net/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

project = '/Users/nerdfiles/Projects/nerdfiles_net/'
sys.path.insert(0, project)
workspace = os.path.dirname(project)
sys.path.append(workspace)

application = get_wsgi_application()
