# Generated by Django 5.0 on 2024-01-16 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0010_alter_producto_fecha_vencimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_vencimiento',
            field=models.DateField(default=datetime.datetime(2025, 1, 14, 23, 49, 39, 312772)),
        ),
    ]
