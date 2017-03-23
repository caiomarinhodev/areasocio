from __future__ import unicode_literals

import base64
import hashlib

from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User as Account
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def create_username(email):
    """
    Create a username to an email hash.
    """
    return base64.urlsafe_b64encode(hashlib.sha1(email).digest())


# Create your models here.
class User(TimeStamped):
    """
    Model of user.
    """

    ADMINISTRADOR = 'ADMINISTRADOR'
    ASPIRANTE = 'ASPIRANTE'
    REGULAR = 'REGULAR'
    EFETIVO = 'EFETIVO'
    CATEGORIAS = (
        (ASPIRANTE, ASPIRANTE),
        (REGULAR, REGULAR),
        (EFETIVO, EFETIVO),
        (ADMINISTRADOR, ADMINISTRADOR),
    )
    conta = models.OneToOneField(Account, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, verbose_name=_('name'))
    cpf = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    cod_area = models.CharField(max_length=2)
    telefone = models.CharField(max_length=30)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS,
                                 verbose_name=_('categoria'))
    foto = CloudinaryField('photo')
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s" % self.name

    def get_birth_date(self):
        return self.birth_date.strftime("%d/%m/%Y")

    def get_cpf_numbers(self):
        return self.cpf.replace('.', '').replace('-', '')

    def get_phone_numbers(self):
        return self.phone.replace(' ', '').replace('-', '')

    @staticmethod
    def create(nome, email, categoria, senha, is_active, cpf, data_nascimento, cod_area, fone, foto):
        """
        Create an user
        """
        user = User()
        user.nome = nome
        user.categoria = categoria
        user.is_active = is_active
        account = Account.objects.create_user(
            create_username(email), email, senha)
        account.save()
        user.conta = account
        user.cpf = cpf
        user.cod_area = cod_area
        user.data_nascimento = data_nascimento
        user.fone = fone
        user.foto = foto
        user.save()
