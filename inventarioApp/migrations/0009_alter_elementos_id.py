# Generated by Django 4.0.4 on 2022-05-05 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0008_pacientes_tipodocumento_pacientes_elementos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementos',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
