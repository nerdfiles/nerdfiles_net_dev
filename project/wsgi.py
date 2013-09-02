import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nerdfiles_net.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
