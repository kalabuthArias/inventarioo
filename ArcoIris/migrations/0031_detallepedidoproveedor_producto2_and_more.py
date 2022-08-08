# Generated by Django 4.0.4 on 2022-06-08 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArcoIris', '0030_pedidoproveedor_cantidad_entregada_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallepedidoproveedor',
            name='producto2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ArcoIris.elementoarcoirispersonal'),
        ),
        migrations.AddField(
            model_name='pedidoproveedor',
            name='producto2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ArcoIris.elementoarcoirispersonal'),
        ),
    ]
