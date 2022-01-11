from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome')
    image = models.ImageField(verbose_name='Logo da empresa')
    user = models.OneToOneField(User, on_delete=models.PROTECT)


    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        
        return url

        