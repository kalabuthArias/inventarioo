# Generated by Django 4.0.4 on 2022-05-06 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0009_alter_elementos_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Discapacidad',
        ),
        migrations.DeleteModel(
            name='Sedes',
        ),
        migrations.RemoveField(
            model_name='pacientes',
            name='elementos',
        ),
    ]