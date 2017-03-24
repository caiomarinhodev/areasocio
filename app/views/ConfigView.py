# Create your views here.
# -*- coding: utf-8 -*-
import cloudinary
from django.contrib import messages
from django.views.generic import UpdateView

from app.forms import FormAlterarDados
from app.models import Usuario


class ConfigView(UpdateView):
    form_class = FormAlterarDados
    template_name = 'alterar_dados.html'
    success_url = '/configuracoes'
    model = Usuario

    def get_object(self, queryset=None):
        return self.request.user.usuario

    def post(self, request, *args, **kwargs):
        return super(ConfigView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Alterado com sucesso')
        return super(ConfigView, self).form_valid(form)

    def form_invalid(self, form):
        print form.errors
        messages.error(self.request, 'Houve algum erro')
        return super(ConfigView, self).form_invalid(form)
