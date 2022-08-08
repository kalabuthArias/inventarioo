# Generated by Django 4.0.4 on 2022-05-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0017_proveedor_elementos_cantidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pacientes',
            name='Unidad',
        ),
        migrations.RemoveField(
            model_name='pacientes',
            name='discapacidad',
        ),
        migrations.AddField(
            model_name='pacientes',
            name='genero',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino')], default='g', max_length=40, null=True, verbose_name='Género'),
        ),
        migrations.AddField(
            model_name='pacientes',
            name='modalidad',
            field=models.CharField(blank=True, default='a', max_length=40, null=True, verbose_name='Modalidad'),
        ),
        migrations.AddField(
            model_name='pacientes',
            name='sede',
            field=models.CharField(blank=True, choices=[('VA', 'Villa Adriana'), ('VJ', 'Villa Johana'), ('VB', 'Villa Blanca'), ('AI', 'Arco Iris')], default='f', max_length=40, null=True, verbose_name='Sede'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='PrimerNombre',
            field=models.CharField(max_length=40, verbose_name='Primer  nombre'),
        ),
    ]
