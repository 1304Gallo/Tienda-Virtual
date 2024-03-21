# Generated by Django 5.0 on 2024-01-12 17:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='id',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='numero_serie_producto',
        ),
        migrations.AddField(
            model_name='venta',
            name='cliente',
            field=models.CharField(default='Cliente Anónimo', max_length=100),
        ),
        migrations.AddField(
            model_name='venta',
            name='fecha_hora_venta',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='venta',
            name='numero_serie_productos',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='precio_producto',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='venta',
            name='id_venta',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
