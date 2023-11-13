"""
URL configuration for CMDBase default website.
"""
import re
from django.contrib import admin, auth
from django.views.static import serve
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django_js_choices.views import choices_js

# Text to put at the end of each page's <title>.
admin.site.site_title = _("CMDBase admin")

# Text to put in each page's <h1> and in loggin form.
admin.site.site_header = _("CMDBase admin")

# Text to put at the top of the admin index page.
admin.site.index_title = _("Administration")


urlpatterns = [
    path('', include('cmdbase.urls', namespace='cmdbase')),
    path('favicon.ico', RedirectView.as_view(url=static('cmdbase/favicon.ico'))),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # NOTE: if not DEBUG, use static file (see: https://github.com/lorinkoz/django-js-choices#usage-as-static-file)
    urlpatterns.append(path("jschoices/", choices_js, name="js_choices"))

if getattr(settings, 'WITH_DEBUG_TOOLBAR', False):
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
