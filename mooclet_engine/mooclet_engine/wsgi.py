"""
WSGI config for adaptive_mooclet_lti project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
print(sys.path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mooclet_engine.settings.local")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
