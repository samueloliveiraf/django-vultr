# Generated by Django 4.0 on 2022-01-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_remove_company_image_alter_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='image',
            field=models.ImageField(default=1, upload_to='', verbose_name='Logo'),
            preserve_default=False,
        ),
    ]
