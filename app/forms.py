# -*- coding: utf-8 -*-
from django import forms

from app.models import Usuario


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = 'true'


class FormRegistro(forms.ModelForm, BaseForm):
    email = forms.EmailField(widget=forms.EmailInput)
    senha = forms.CharField(widget=forms.PasswordInput)
    retype_senha = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('nome', 'sobrenome', 'data_nascimento', 'titulo', 'descricao',
                  'categoria', 'area', 'departamento', 'universidade', 'cep', 'rua', 'numero',
                  'bairro', 'cidade', 'estado')

    def __init__(self, *args, **kwargs):
        super(FormRegistro, self).__init__(*args, **kwargs)
        self.fields['data_nascimento'].widget.attrs['class'] += ' datepicker'
