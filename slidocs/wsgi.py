"""
WSGI config for slidocs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from slidocs.settings.base import DEBUG

if DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'slidocs.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'slidocs.settings.production')

application = get_wsgi_application()
