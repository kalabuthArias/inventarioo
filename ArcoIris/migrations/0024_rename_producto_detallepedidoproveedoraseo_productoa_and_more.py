# Generated by Django 4.0.4 on 2022-06-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArcoIris', '0023_alter_detallepedidoproveedor_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallepedidoproveedoraseo',
            old_name='producto',
            new_name='productoA',
        ),
        migrations.RenameField(
            model_name='detallepedidoproveedorpersonal',
            old_name='producto',
            new_name='productoP',
        ),
        migrations.AlterField(
            model_name='detallepedidoproveedorpersonal',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]