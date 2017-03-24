# -*- coding: utf-8 -*-
from django import forms

from app.models import Usuario


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class FormLogin(BaseForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'required': 'true',
        'maxlength': 150,
        'placeholder': 'Email'

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'autocomplete': 'off',
        'class': 'form-control input-lg',
        'placeholder': 'Senha',
        'required': 'true',
        'data-parsley-trigger': 'change'
    }))


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


class FormAlterarDados(forms.ModelForm, BaseForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'sobrenome', 'data_nascimento', 'titulo', 'descricao',
                  'categoria', 'area', 'departamento', 'universidade', 'cep', 'rua', 'numero',
                  'bairro', 'cidade', 'estado', 'foto')

    def __init__(self, *args, **kwargs):
        super(FormAlterarDados, self).__init__(*args, **kwargs)
        self.fields['data_nascimento'].widget.attrs['class'] += ' datepicker'
