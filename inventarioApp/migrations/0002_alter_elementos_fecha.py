# Generated by Django 4.0.4 on 2022-05-02 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementos',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de entrada'),
        ),
    ]
