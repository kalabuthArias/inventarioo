# Generated by Django 4.0.4 on 2022-05-17 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VillaAdriana', '0007_alter_elementovillaadrianapersonal_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='elementovillaadriana',
            options={'ordering': ['nombreElemento'], 'verbose_name': 'Dotación Dormitorio', 'verbose_name_plural': 'Dotación dormitorio'},
        ),
    ]