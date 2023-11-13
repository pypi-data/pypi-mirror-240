"""
ASGI configuration for CMDBase default website.
"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmdbase.site.settings")

application = get_asgi_application()
