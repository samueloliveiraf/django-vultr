# Generated by Django 4.0 on 2021-12-26 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product'),
        ),
    ]
