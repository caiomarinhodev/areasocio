# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout, authenticate, login
from django.contrib.auth.models import User as Account
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import RedirectView

from app.forms import FormLogin
from app.mixins import CustomFormView


class LoginView(CustomFormView):
    """
    Provides the ability to login as a user with a username and password
    """
    success_url = '/'
    form_class = FormLogin
    template_name = 'login.html'

    def form_valid(self, form):
        try:
            auth_user = Account.objects.get(email=form.cleaned_data['email'])
            user = authenticate(username=auth_user.username, password=form.cleaned_data['password'])
            login(self.request, user)
        except Account.DoesNotExist:
            messages.error(self.request, 'Usuário não cadastrado.')
            return self.form_invalid(form)
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/login'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
