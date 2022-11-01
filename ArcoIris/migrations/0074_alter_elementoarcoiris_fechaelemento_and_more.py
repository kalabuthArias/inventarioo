# Generated by Django 4.0.4 on 2022-08-31 18:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ArcoIris', '0073_alter_elementoarcoiris_fechaelemento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementoarcoiris',
            name='fechaElemento',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de ingreso'),
        ),
        migrations.AlterField(
            model_name='elementoarcoirisaseo',
            name='fechaElemento',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de ingreso'),
        ),
        migrations.AlterField(
            model_name='elementoarcoirispersonal',
            name='fechaElemento',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de ingreso'),
        ),
    ]
