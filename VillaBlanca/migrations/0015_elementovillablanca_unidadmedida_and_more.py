# Generated by Django 4.0.4 on 2022-05-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VillaBlanca', '0014_pacientevillablanca_tiposalida_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementovillablanca',
            name='unidadmedida',
            field=models.CharField(choices=[('unidades', 'Unidades'), ('kit', 'KIT'), ('litros', 'Litros'), ('otro', 'Otro')], default='ninguna', max_length=40, null=True, verbose_name='Unidad de medidad'),
        ),
        migrations.AddField(
            model_name='elementovillablancaaseo',
            name='unidadmedida',
            field=models.CharField(choices=[('unidades', 'Unidades'), ('kit', 'KIT'), ('litros', 'Litros'), ('otro', 'Otro')], default='ninguna', max_length=40, null=True, verbose_name='Unidad de medidad'),
        ),
        migrations.AddField(
            model_name='elementovillablancapersonal',
            name='unidadmedida',
            field=models.CharField(choices=[('unidades', 'Unidades'), ('kit', 'KIT'), ('litros', 'Litros'), ('otro', 'Otro')], default='ninguna', max_length=40, null=True, verbose_name='Unidad de medidad'),
        ),
    ]
