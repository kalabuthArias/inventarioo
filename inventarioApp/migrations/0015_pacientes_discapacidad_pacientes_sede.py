# Generated by Django 4.0.4 on 2022-05-07 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0014_alter_pacientes_fechaingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacientes',
            name='discapacidad',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Discapacidad'),
        ),
        migrations.AddField(
            model_name='pacientes',
            name='sede',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Sede'),
        ),
    ]