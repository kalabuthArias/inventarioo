# Generated by Django 4.0.4 on 2022-05-17 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VillaBlanca', '0009_alter_elementovillablanca_nombreelemento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientevillablanca',
            name='TipoDocumento',
            field=models.CharField(choices=[('CC', 'C.C'), ('RC', 'R.C'), ('TI', ' T.I')], default='F', max_length=40, null=True, verbose_name='Tipo de documento'),
        ),
    ]
