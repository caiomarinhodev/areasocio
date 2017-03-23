# Create your views here.
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.models import User as Account
from django.views.generic import CreateView

from app.forms import FormRegistro
from app.models import create_username


class RegistroView(CreateView):
    form_class = FormRegistro
    template_name = 'registro.html'
    success_url = '/login'

    def form_valid(self, form):
        data = form.cleaned_data
        try:
            account = Account.objects.create_user(
                create_username(data['email']), data['email'], data['senha'])
            account.save()
            form.instance.conta = account
        except Exception:
            messages.error(self.request, 'Email já esta sendo usado')
            return self.form_invalid(form)
        return super(RegistroView, self).form_valid(form)

    def form_invalid(self, form):
        print form.errors
        return super(RegistroView, self).form_invalid(form)
