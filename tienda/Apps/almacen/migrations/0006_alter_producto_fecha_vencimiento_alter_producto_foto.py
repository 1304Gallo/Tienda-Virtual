# Generated by Django 5.0 on 2024-01-16 04:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0005_categoria_producto_foto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_vencimiento',
            field=models.DateField(default=datetime.datetime(2025, 1, 14, 23, 43, 6, 595422)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='foto',
            field=models.ImageField(upload_to='product_images/'),
        ),
    ]
