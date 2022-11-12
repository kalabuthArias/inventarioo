# Generated by Django 4.0.4 on 2022-08-31 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VillaBlanca', '0022_alter_pacientevillablanca_segundoapellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientevillablanca',
            name='FechaIngreso',
            field=models.DateField(null=True, verbose_name='Fecha de ingreso'),
        ),
        migrations.AlterField(
            model_name='pacientevillablanca',
            name='FechaNacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='pedidoproveedorblanca',
            name='entregado',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='pedidoproveedorblanca',
            name='solicitado',
            field=models.BooleanField(),
        ),
    ]