# Generated by Django 4.0.4 on 2022-05-07 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0012_alter_pacientes_tipodocumento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='FechaEgreso',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de salida'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='FechaNacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='SegundoApellido',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Segundo apellido'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='SegundoNombre',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Segundo nombre'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='TipoDocumento',
            field=models.CharField(blank=True, choices=[('CC', 'C.C'), ('RC', 'R.C'), ('TI', ' T.I')], default='F', max_length=40, null=True, verbose_name='Tipo de cédula'),
        ),
    ]
