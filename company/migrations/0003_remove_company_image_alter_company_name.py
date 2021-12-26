# Generated by Django 4.0 on 2021-12-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_company_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='image',
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
    ]
