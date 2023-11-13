from __future__ import annotations
import logging
from django.http import HttpRequest
from django.conf import settings
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import LoginView, LogoutView, redirect_to_login
from django.contrib.auth.models import AbstractUser
from django.views.generic.base import RedirectView

logger = logging.getLogger(__name__)

class CMDBaseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request: HttpRequest, view_func, view_args, view_kwargs):
        return         
