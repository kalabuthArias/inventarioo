# Generated by Django 4.0.4 on 2022-08-31 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VillaAdriana', '0024_alter_pacientevillaadriana_fechaingreso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementovillaadriana',
            name='fecha_vencimiento',
            field=models.DateField(null=True, verbose_name='Fecha de vencimiento'),
        ),
        migrations.AlterField(
            model_name='elementovillaadrianaaseo',
            name='fecha_vencimiento',
            field=models.DateField(null=True, verbose_name='Fecha de vencimiento'),
        ),
        migrations.AlterField(
            model_name='elementovillaadrianapersonal',
            name='fecha_vencimiento',
            field=models.DateField(null=True, verbose_name='Fecha de vencimiento'),
        ),
    ]
