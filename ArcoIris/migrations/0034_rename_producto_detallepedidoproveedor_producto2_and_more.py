# Generated by Django 4.0.4 on 2022-06-08 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArcoIris', '0033_rename_producto2_detallepedidoproveedor_producto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallepedidoproveedor',
            old_name='Producto',
            new_name='producto2',
        ),
        migrations.RenameField(
            model_name='pedidoproveedor',
            old_name='Producto',
            new_name='producto2',
        ),
        migrations.AddField(
            model_name='detallepedidoproveedor',
            name='producto1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ArcoIris.elementoarcoiris'),
        ),
        migrations.AddField(
            model_name='pedidoproveedor',
            name='producto1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ArcoIris.elementoarcoiris'),
        ),
    ]
