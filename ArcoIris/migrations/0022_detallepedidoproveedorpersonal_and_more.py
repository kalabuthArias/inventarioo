# Generated by Django 4.0.4 on 2022-06-06 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArcoIris', '0021_pedidoproveedor_devolucionpedidoproveedor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetallePedidoProveedorPersonal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_solicitada', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cantidad_entregada', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('cantidad_entregada_anterior', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('precio_compra', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArcoIris.pedidoproveedor')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArcoIris.elementoarcoirispersonal')),
            ],
            options={
                'verbose_name': 'DETALLE PEDIDO',
                'verbose_name_plural': 'DETALLE PEDIDO',
            },
        ),
        migrations.CreateModel(
            name='DetallePedidoProveedorAseo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_solicitada', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cantidad_entregada', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('cantidad_entregada_anterior', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('precio_compra', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArcoIris.pedidoproveedor')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArcoIris.elementoarcoirisaseo')),
            ],
            options={
                'verbose_name': 'DETALLE PEDIDO',
                'verbose_name_plural': 'DETALLE PEDIDO',
            },
        ),
        migrations.CreateModel(
            name='DetalleDevolucionPedidoProveedorPersonal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_devuelta', models.DecimalField(decimal_places=2, max_digits=6)),
                ('motivo', models.CharField(choices=[('PM', 'Producto en mal estado'), ('PV', 'Producto vencido')], max_length=2)),
                ('devolucion_pedido_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArcoIris.devolucionpedidoproveedor')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArcoIris.elementoarcoirispersonal')),
            ],
            options={
                'verbose_name': 'Detalle devolución',
                'verbose_name_plural': 'Detalle devolución',
            },
        ),
        migrations.CreateModel(
            name='DetalleDevolucionPedidoProveedorAseo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_devuelta', models.DecimalField(decimal_places=2, max_digits=6)),
                ('motivo', models.CharField(choices=[('PM', 'Producto en mal estado'), ('PV', 'Producto vencido')], max_length=2)),
                ('devolucion_pedido_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArcoIris.devolucionpedidoproveedor')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArcoIris.elementoarcoirisaseo')),
            ],
            options={
                'verbose_name': 'Detalle devolución',
                'verbose_name_plural': 'Detalle devolución',
            },
        ),
    ]
