# Generated by Django 4.0.4 on 2022-05-15 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0018_remove_pacientes_unidad_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Elementos',
            new_name='Elemento',
        ),
        migrations.DeleteModel(
            name='Pacientes',
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={'ordering': ['id'], 'verbose_name': 'Proveedor', 'verbose_name_plural': 'Proveedores'},
        ),
    ]
