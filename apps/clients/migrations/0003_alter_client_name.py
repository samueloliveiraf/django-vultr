# Generated by Django 4.0 on 2021-12-17 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
    ]