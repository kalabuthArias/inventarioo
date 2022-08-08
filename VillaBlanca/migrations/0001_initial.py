# Generated by Django 4.0.4 on 2022-05-16 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pacienteVillaBlanca',
            fields=[
                ('modalidad', models.CharField(blank=True, choices=[('PSICO', ' Psicosocial'), ('INTELE', 'Intelectual')], default='a', max_length=40, null=True, verbose_name='Modalidad')),
                ('genero', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino')], default='g', max_length=40, null=True, verbose_name='Género')),
                ('PrimerApellido', models.CharField(max_length=40, verbose_name='Primer apellido')),
                ('SegundoApellido', models.CharField(blank=True, max_length=40, null=True, verbose_name='Segundo apellido')),
                ('PrimerNombre', models.CharField(max_length=40, verbose_name='Primer  nombre')),
                ('SegundoNombre', models.CharField(blank=True, max_length=40, null=True, verbose_name='Segundo nombre')),
                ('FechaNacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('TipoDocumento', models.CharField(blank=True, choices=[('CC', 'C.C'), ('RC', 'R.C'), ('TI', ' T.I')], default='F', max_length=40, null=True, verbose_name='Tipo de cédula')),
                ('NumeroDocumento', models.CharField(max_length=20, verbose_name='Número de documento')),
                ('tallaPrenda', models.CharField(max_length=20, verbose_name='Talla de prenda')),
                ('tallaCalzado', models.CharField(max_length=20, verbose_name='Talla de calzado')),
                ('FechaIngreso', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha de ingreso')),
                ('FechaEgreso', models.DateField(blank=True, null=True, verbose_name='Fecha de salida')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'ordering': ['id'],
            },
        ),
    ]
