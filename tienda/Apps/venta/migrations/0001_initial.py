# Generated by Django 4.2.7 on 2023-12-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_productos', models.IntegerField()),
                ('nombre_producto', models.CharField(max_length=50)),
                ('numero_serie_producto', models.IntegerField()),
                ('id_venta', models.IntegerField()),
                ('dinero_recaudado', models.IntegerField()),
            ],
        ),
    ]