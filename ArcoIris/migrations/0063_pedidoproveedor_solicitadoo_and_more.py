# Generated by Django 4.0.4 on 2022-07-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArcoIris', '0062_remove_pedidoproveedor_solicitado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidoproveedor',
            name='solicitadoo',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Sopytholicitado por:'),
        ),
        migrations.AddField(
            model_name='pedidoproveedoraseo',
            name='solicitadoo',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Solicitado por:'),
        ),
        migrations.AddField(
            model_name='pedidoproveedorpersonal',
            name='solicitadoo',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Solicitado por:'),
        ),
    ]