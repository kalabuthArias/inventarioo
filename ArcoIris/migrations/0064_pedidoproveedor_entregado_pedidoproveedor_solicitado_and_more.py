# Generated by Django 4.0.4 on 2022-07-16 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArcoIris', '0063_pedidoproveedor_solicitadoo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidoproveedor',
            name='entregado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidoproveedor',
            name='solicitado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidoproveedoraseo',
            name='entregado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidoproveedoraseo',
            name='solicitado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidoproveedorpersonal',
            name='entregado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedidoproveedorpersonal',
            name='solicitado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pedidoproveedor',
            name='fecha_solicitud',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de entrega'),
        ),
        migrations.AlterField(
            model_name='pedidoproveedoraseo',
            name='fecha_solicitud',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de entrega'),
        ),
        migrations.AlterField(
            model_name='pedidoproveedorpersonal',
            name='fecha_solicitud',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de entrega'),
        ),
    ]