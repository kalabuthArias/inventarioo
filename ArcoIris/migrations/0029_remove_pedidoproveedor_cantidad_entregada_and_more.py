# Generated by Django 4.0.4 on 2022-06-08 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ArcoIris', '0028_pedidoproveedor_cantidad_entregada_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidoproveedor',
            name='cantidad_entregada',
        ),
        migrations.RemoveField(
            model_name='pedidoproveedor',
            name='cantidad_entregada_anterior',
        ),
        migrations.RemoveField(
            model_name='pedidoproveedor',
            name='cantidad_solicitada',
        ),
        migrations.RemoveField(
            model_name='pedidoproveedor',
            name='producto',
        ),
    ]
