# Generated by Django 4.0.4 on 2022-08-26 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArcoIris', '0066_remove_detallepedidoproveedor_precio_compra_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidoproveedor',
            name='entregado',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedidoproveedor',
            name='solicitado',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedidoproveedoraseo',
            name='entregado',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedidoproveedoraseo',
            name='solicitado',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedidoproveedorpersonal',
            name='entregado',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedidoproveedorpersonal',
            name='solicitado',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]