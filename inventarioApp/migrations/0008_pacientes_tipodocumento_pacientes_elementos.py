# Generated by Django 4.0.4 on 2022-05-05 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0007_discapacidad_pacientes_sedes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacientes',
            name='TipoDocumento',
            field=models.CharField(choices=[('CC', 'Cedula de ciudadania'), ('RC', 'Registro civil'), ('TI', ' Tarjeta de identidad')], default='F', max_length=40, verbose_name='Tipo de cédula'),
        ),
        migrations.AddField(
            model_name='pacientes',
            name='elementos',
            field=models.ManyToManyField(to='inventarioApp.elementos'),
        ),
    ]