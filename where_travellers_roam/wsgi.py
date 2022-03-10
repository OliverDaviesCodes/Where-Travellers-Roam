import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'where_travellers_roam.settings')

application = get_wsgi_application()
