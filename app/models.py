# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import base64
import hashlib

from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User as Account
from django.db import models
from django.utils.translation import ugettext_lazy as _
from djmoney.models.fields import MoneyField
from moneyed import BRL


class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Activable(models.Model):
    class Meta:
        abstract = True

    is_active = models.BooleanField(default=True)


TITULOS = (
    ('Doutor', 'Doutor'),
    ('Doutorando', 'Doutorando'),
    ('Mestre', 'Mestre'),
    ('Mestrando', 'Mestrando'),
    ('Bacharel', 'Bacharel'),
    ('Graduando', 'Graduando')
)

CATEGORIAS = (
    ('ASPIRANTES', 'ASPIRANTES'),
    ('REGULARES', 'REGULARES'),
    ('EFETIVOS', 'EFETIVOS'),
    ('ADMINISTRADOR', 'ADMINISTRADOR'),
)


class Categoria(TimeStamped, Activable):
    """
    Categoria Model.
    """
    nome = models.CharField(max_length=100, choices=CATEGORIAS)
    valor_categoria = MoneyField(max_digits=10, decimal_places=2, default_currency=BRL)

    def __unicode__(self):
        return "%s" % self.nome


class Sociable(models.Model):
    class Meta:
        abstract = True

    titulo = models.CharField(max_length=100, choices=TITULOS)
    descricao = models.TextField(verbose_name='Outras Informações')
    categoria = models.OneToOneField(Categoria)
    area = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    universidade = models.CharField(max_length=100, blank=True, null=True)


class Fotoable(models.Model):
    class Meta:
        abstract = True

    foto = CloudinaryField('foto')


class BaseAddress(models.Model):
    class Meta:
        abstract = True

    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=100)


def create_username(email):
    """
    Create a username to an email hash.
    """
    return base64.urlsafe_b64encode(hashlib.sha1(email).digest())


# Create your models here.
class Usuario(TimeStamped, Activable, Sociable, Fotoable, BaseAddress):
    """
    Model of usuario.
    """

    conta = models.OneToOneField(Account, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, verbose_name=_('Nome'))
    data_nascimento = models.DateField()
    status_pagamento = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s" % self.name

    def get_birth_date(self):
        return self.data_nascimento.strftime("%d/%m/%Y")

    @staticmethod
    def create(nome, email, categoria, senha, is_active, data_nascimento, titulo, descricao,
               area, depto, universidade, rua, num, bairro, cep, cidade, estado, foto):
        """
        Create an user
        """
        user = Usuario()
        user.nome = nome
        user.categoria = categoria  # Instance or pk categoria.
        user.is_active = is_active
        account = Account.objects.create_user(
            create_username(email), email, senha)
        account.save()
        user.conta = account
        user.data_nascimento = data_nascimento
        if foto:
            user.foto = foto
        user.titulo = titulo
        user.descricao = descricao
        user.area = area
        user.departamento = depto
        user.universidade = universidade
        user.rua = rua
        user.numero = num
        user.bairro = bairro
        user.cep = cep
        user.cidade = cidade
        user.estado = estado
        user.save()
