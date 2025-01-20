# Generated by Django 5.1.5 on 2025-01-19 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquiler', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='usaurio',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='anfrition',
            name='fecha_registro',
        ),
        migrations.AlterField(
            model_name='usuariologin',
            name='rol',
            field=models.PositiveSmallIntegerField(choices=[(1, 'administrador'), (2, 'anfrition'), (3, 'usuario')], default=3),
        ),
    ]
