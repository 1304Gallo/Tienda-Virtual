# Generated by Django 5.0.3 on 2024-04-10 02:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0028_alter_producto_fecha_vencimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_vencimiento',
            field=models.DateField(default=datetime.datetime(2025, 4, 9, 22, 44, 59, 365542)),
        ),
    ]
