from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome')
    phone = models.DecimalField(max_digits=14,decimal_places=0, verbose_name='Telefone')
    email = models.EmailField(verbose_name='E-mail')
    user = models.ForeignKey(User, on_delete=PROTECT)

    def __str__(self):
        return self.name

