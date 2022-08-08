# Generated by Django 4.0.4 on 2022-05-17 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VillaAdriana', '0002_elementovillaadriana'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elementovillaadriana',
            options={'ordering': ['nombreElemento'], 'verbose_name': 'Elemento', 'verbose_name_plural': 'Elementos'},
        ),
        migrations.AlterModelOptions(
            name='pacientevillaadriana',
            options={'ordering': ['PrimerApellido'], 'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
        migrations.AlterField(
            model_name='elementovillaadriana',
            name='TipoProducto',
            field=models.CharField(blank=True, choices=[('Dormitorio', 'Dormitorio'), ('UsoPersonal', 'Uso personal'), ('UsoComún', 'Uso común')], default='F', max_length=40, null=True, verbose_name='Tipo de elemento'),
        ),
        migrations.AlterField(
            model_name='elementovillaadriana',
            name='fechaElemento',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
    ]