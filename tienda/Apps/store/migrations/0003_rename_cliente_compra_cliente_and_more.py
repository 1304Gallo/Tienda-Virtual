# Generated by Django 5.0.3 on 2024-04-17 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_cliente_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='Cliente',
            new_name='cliente',
        ),
        migrations.AlterField(
            model_name='direccioncompra',
            name='compra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articulos', to='store.compra'),
        ),
    ]