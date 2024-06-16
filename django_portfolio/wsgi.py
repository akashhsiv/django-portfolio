"""
WSGI config for django_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_portfolio.settings')

if os.environ.get('ENV') == 'production':
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    
application = get_wsgi_application()

app = application
