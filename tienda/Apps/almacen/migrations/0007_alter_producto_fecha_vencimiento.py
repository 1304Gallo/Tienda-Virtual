# Generated by Django 5.0 on 2024-01-16 04:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0006_alter_producto_fecha_vencimiento_alter_producto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_vencimiento',
            field=models.DateField(default=datetime.datetime(2025, 1, 14, 23, 44, 18, 740071)),
        ),
    ]
