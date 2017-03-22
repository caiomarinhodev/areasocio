from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _


class UnauthorizedException(Exception):
    """
    Handles unauthorized exceptions.
    """


class ForbiddenException(Exception):
    """
    Handles forbidden exceptions.
    """


class CustomMiddleware(object):
    """
    Handles request/response processing.
    """

    @classmethod
    def process_exception(cls, request, exception):
        """
        Handle exceptions raised by views.
        :param request: HttpRequest object.
        :param exception: Exception object raised by the view function.
        :return: The HttpResponse handling the exception or None if no action is taken.
        """
        response = None
        if isinstance(exception, UnauthorizedException):
            if request.session.get('user'):
                messages.error(request, _('Your session has expired'))
            response = redirect('login')
        elif isinstance(exception, ForbiddenException):
            if request.session.get('user'):
                messages.error(request, _('Permission denied'))
            response = redirect('index')
        return response
