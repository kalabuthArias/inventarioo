# Generated by Django 4.0.4 on 2022-05-17 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ArcoIris', '0012_alter_elementoarcoiris_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elementoarcoirispersonal',
            options={'ordering': ['nombreElemento'], 'verbose_name': 'Inventario dotación personal', 'verbose_name_plural': 'Inventario dotación personal'},
        ),
    ]