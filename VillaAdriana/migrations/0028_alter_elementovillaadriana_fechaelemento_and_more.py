# Generated by Django 4.0.4 on 2022-08-31 18:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('VillaAdriana', '0027_alter_elementovillaadriana_fechaelemento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementovillaadriana',
            name='fechaElemento',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de ingreso'),
        ),
        migrations.AlterField(
            model_name='elementovillaadrianaaseo',
            name='fechaElemento',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de ingreso'),
        ),
        migrations.AlterField(
            model_name='elementovillaadrianapersonal',
            name='fechaElemento',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de ingreso'),
        ),
    ]