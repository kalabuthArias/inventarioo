# Generated by Django 4.0.4 on 2022-05-17 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0020_delete_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='elemento',
            name='TipoProducto',
            field=models.CharField(blank=True, choices=[('Dormitorio', 'Dormitorio'), ('UsoPersonal', 'Uso personal'), ('UsoComún', 'Uso común')], default='F', max_length=40, null=True, verbose_name='Tipo de cédula'),
        ),
    ]
