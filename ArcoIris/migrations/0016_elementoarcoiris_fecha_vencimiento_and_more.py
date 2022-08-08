# Generated by Django 4.0.4 on 2022-05-19 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArcoIris', '0015_alter_pacientearcoiris_tipodocumento'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementoarcoiris',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de vencimiento'),
        ),
        migrations.AddField(
            model_name='elementoarcoirisaseo',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de vencimiento'),
        ),
        migrations.AddField(
            model_name='elementoarcoirispersonal',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de vencimiento'),
        ),
    ]
