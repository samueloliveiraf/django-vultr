# Generated by Django 4.0 on 2022-01-11 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_company_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Logo da empresa'),
        ),
    ]
