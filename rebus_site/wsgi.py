import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rebus_site.settings")

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

#path = '/home/mariana/REBUS/rebus_site'
#if path not in sys.path:
#    sys.path.append(path)
