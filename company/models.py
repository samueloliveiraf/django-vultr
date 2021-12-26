from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome')
    user = models.OneToOneField(User, on_delete=models.PROTECT)


    def __str__(self):
        return self.name

        