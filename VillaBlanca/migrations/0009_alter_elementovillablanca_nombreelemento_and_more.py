# Generated by Django 4.0.4 on 2022-05-17 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VillaBlanca', '0008_alter_elementovillablanca_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementovillablanca',
            name='nombreElemento',
            field=models.CharField(max_length=100, null=True, verbose_name='Elemento'),
        ),
        migrations.AlterField(
            model_name='elementovillablancaaseo',
            name='nombreElemento',
            field=models.CharField(max_length=100, null=True, verbose_name='Elemento'),
        ),
        migrations.AlterField(
            model_name='elementovillablancapersonal',
            name='nombreElemento',
            field=models.CharField(max_length=100, null=True, verbose_name='Elemento'),
        ),
        migrations.AlterField(
            model_name='pacientevillablanca',
            name='FechaNacimiento',
            field=models.DateField(null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='pacientevillablanca',
            name='PrimerApellido',
            field=models.CharField(max_length=40, null=True, verbose_name='Primer apellido'),
        ),
        migrations.AlterField(
            model_name='pacientevillablanca',
            name='TipoDocumento',
            field=models.CharField(choices=[('CC', 'C.C'), ('RC', 'R.C'), ('TI', ' T.I')], default='F', max_length=40, null=True, verbose_name='Tipo de cédula'),
        ),
        migrations.AlterField(
            model_name='pacientevillablanca',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='g', max_length=40, null=True, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='pacientevillablanca',
            name='modalidad',
            field=models.CharField(choices=[('PSICO', ' Psicosocial'), ('INTELE', 'Intelectual')], default='a', max_length=40, null=True, verbose_name='Modalidad'),
        ),
    ]
