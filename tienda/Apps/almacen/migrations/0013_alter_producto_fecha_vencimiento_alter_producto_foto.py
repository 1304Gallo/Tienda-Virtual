# Generated by Django 5.0 on 2024-01-16 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0012_alter_producto_fecha_vencimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_vencimiento',
            field=models.DateField(default=datetime.datetime(2025, 1, 15, 10, 38, 48, 735134)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='foto',
            field=models.ImageField(upload_to='fotos_productos'),
        ),
    ]
