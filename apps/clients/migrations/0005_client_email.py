# Generated by Django 4.0 on 2021-12-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_client_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='E-mail'),
            preserve_default=False,
        ),
    ]