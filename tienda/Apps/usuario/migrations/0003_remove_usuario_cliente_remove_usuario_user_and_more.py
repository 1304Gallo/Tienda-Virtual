# Generated by Django 5.0.3 on 2024-04-17 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_rename_userprofile_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]