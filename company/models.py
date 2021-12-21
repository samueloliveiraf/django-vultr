from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='company', verbose_name='Imagem')
    user = models.OneToOneField(User, on_delete=models.PROTECT)


    def __str__(self):
        return self.name

        