# Generated by Django 4.0.4 on 2022-05-03 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0003_alter_elementos_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementos',
            name='fecha',
            field=models.DateField(verbose_name='Fecha de entrada'),
        ),
    ]
