# Generated by Django 4.0.4 on 2022-05-23 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VillaAdriana', '0011_elementovillaadriana_fecha_vencimiento_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elementovillaadrianapersonal',
            options={'ordering': ['nombreElemento'], 'verbose_name': 'Dotación personal', 'verbose_name_plural': 'Dotación personal'},
        ),
        migrations.AlterModelOptions(
            name='pacientevillaadriana',
            options={'ordering': ['PrimerApellido'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]
