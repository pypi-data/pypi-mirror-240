import json
from datetime import date
from django.conf import settings
from django.http import HttpRequest
from django.urls import reverse
from django.shortcuts import resolve_url
from django.utils.safestring import mark_safe
from .commons import should_authenticate

LOGIN_URL = resolve_url(getattr(settings, 'LOGIN_URL'))
LOGOUT_URL = resolve_url(getattr(settings, 'LOGOUT_URL', 'admin:logout'))

COPYRIGHT_HOLDER = getattr(settings, 'COPYRIGHT_HOLDER', 'Ipamo')
COPYRIGHT_YEARS = getattr(settings, 'COPYRIGHT_YEARS', None)
if not COPYRIGHT_YEARS:
    today = date.today()
    COPYRIGHT_YEARS = '2023' + (f'-{today.year}' if today.year > 2023 else '')

CMDBASE_AUTOCOMPLETE_PAUSE = float(getattr(settings, 'CMDBASE_AUTOCOMPLETE_PAUSE', '0.2'))

base_url = reverse('cmdbase:index')
if base_url.endswith('/'):
    base_url = base_url[:-1]

def cmdbase(request: HttpRequest):
    return {
        'LOGIN_URL': LOGIN_URL,
        'LOGOUT_URL': LOGOUT_URL,
        'COPYRIGHT_HOLDER': COPYRIGHT_HOLDER,
        'COPYRIGHT_YEARS': COPYRIGHT_YEARS,
        'should_authenticate': should_authenticate(),
        'configure_cmdbase_script': mark_safe(f"<script>cmdbase = new CMDBase({json.dumps({'base_url': base_url, 'autocomplete_pause': CMDBASE_AUTOCOMPLETE_PAUSE, 'debug': settings.DEBUG}, ensure_ascii=False)})</script>")
    }
