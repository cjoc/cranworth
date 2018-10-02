"""
MIDDLEWARE
Defines middleware (namely for authentication purposes)
to be used in this application.
Cameron O'Connor, 2018
"""

from .models import Student
from django.conf import settings
from django.http import HttpResponseRedirect, Http404
from re import compile


class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
        if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
            EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]
        response = self.get_response(request)
        # Check whether user is authenticated.
        if not request.user.is_authenticated:
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                return HttpResponseRedirect('/landing')
            else:
                return response
        # Check that user is registered as a student, excluding admin pages.
        ADMIN_URLS = [compile('admin'), compile('error')]
        try:
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in ADMIN_URLS):
                Student.objects.get(user_id=request.user.username)
        except Student.DoesNotExist:
            return HttpResponseRedirect('/error')
        return response