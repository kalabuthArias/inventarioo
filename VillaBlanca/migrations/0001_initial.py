# Generated by Django 4.0.4 on 2022-11-12 15:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Proveedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementoVillaBlanca',
            fields=[
                ('nombreElemento', models.CharField(max_length=100, null=True, verbose_name='Elemento')),
                ('fechaElemento', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de ingreso')),
                ('stock', models.IntegerField(default=10, null=True, verbose_name='Cantidad')),
                ('unidadmedida', models.CharField(choices=[('unidades', 'Unidades'), ('kit', 'KIT'), ('litros', 'Litros'), ('otro', 'Otro')], default='ninguna', max_length=40, null=True, verbose_name='Unidad de medidad')),
                ('fecha_vencimiento', models.DateField(null=True, verbose_name='Fecha de vencimiento')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Dotación Dormitorio',
                'verbose_name_plural': 'Dotación dormitorio',
                'ordering': ['nombreElemento'],
            },
        ),
        migrations.CreateModel(
            name='ElementoVillaBlancaAseo',
            fields=[
                ('nombreElemento', models.CharField(max_length=100, null=True, verbose_name='Elemento')),
                ('fechaElemento', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de ingreso')),
                ('stock', models.IntegerField(default=10, null=True, verbose_name='Cantidad')),
                ('unidadmedida', models.CharField(choices=[('unidades', 'Unidades'), ('kit', 'KIT'), ('litros', 'Litros'), ('otro', 'Otro')], default='ninguna', max_length=40, null=True, verbose_name='Unidad de medidad')),
                ('fecha_vencimiento', models.DateField(null=True, verbose_name='Fecha de vencimiento')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Dotación Aseo Personal',
                'verbose_name_plural': 'Dotación aseo personal',
                'ordering': ['nombreElemento'],
            },
        ),
        migrations.CreateModel(
            name='ElementoVillaBlancaPersonal',
            fields=[
                ('nombreElemento', models.CharField(max_length=100, null=True, verbose_name='Elemento')),
                ('fechaElemento', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de ingreso')),
                ('stock', models.IntegerField(default=10, null=True, verbose_name='Cantidad')),
                ('unidadmedida', models.CharField(choices=[('unidades', 'Unidades'), ('kit', 'KIT'), ('litros', 'Litros'), ('otro', 'Otro')], default='ninguna', max_length=40, null=True, verbose_name='Unidad de medidad')),
                ('fecha_vencimiento', models.DateField(null=True, verbose_name='Fecha de vencimiento')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('talla', models.CharField(blank=True, max_length=40, null=True, verbose_name='Talla')),
                ('descripcionElemento', models.TextField(blank=True, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Dotación personal',
                'verbose_name_plural': 'Dotación personal',
                'ordering': ['nombreElemento'],
            },
        ),
        migrations.CreateModel(
            name='pacienteVillaBlanca',
            fields=[
                ('modalidad', models.CharField(choices=[('PSICOSIAL', ' Psicosocial'), ('INTELECTUAL', 'Intelectual')], default='a', max_length=40, null=True, verbose_name='Modalidad')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='g', max_length=40, null=True, verbose_name='Género')),
                ('PrimerApellido', models.CharField(max_length=40, null=True, verbose_name='Primer apellido')),
                ('SegundoApellido', models.CharField(blank=True, default=' ', max_length=40, verbose_name='Segundo apellido')),
                ('PrimerNombre', models.CharField(max_length=40, verbose_name='Primer  nombre')),
                ('SegundoNombre', models.CharField(blank=True, default=' ', max_length=40, verbose_name='Segundo nombre')),
                ('FechaNacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('TipoDocumento', models.CharField(choices=[('CC', 'C.C'), ('RC', 'R.C'), ('TI', ' T.I')], default='F', max_length=40, null=True, verbose_name='Tipo de documento')),
                ('NumeroDocumento', models.CharField(max_length=20, verbose_name='Número de documento')),
                ('tallaPrenda', models.CharField(blank=True, max_length=20, verbose_name='Talla de prenda')),
                ('tallaCalzado', models.CharField(blank=True, max_length=20, verbose_name='Talla de calzado')),
                ('FechaIngreso', models.DateField(null=True, verbose_name='Fecha de ingreso')),
                ('FechaEgreso', models.DateField(blank=True, null=True, verbose_name='Fecha de salida')),
                ('tiposalida', models.CharField(blank=True, choices=[('traslado', 'Traslado al ICBF'), ('fallecimiento', 'Fallecimieno'), ('desertor', 'Desertor'), ('otro', 'Otro')], default='ninguna', max_length=40, null=True, verbose_name='Motivo de salida')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['PrimerApellido'],
            },
        ),
        migrations.CreateModel(
            name='SalidaDotacionPersonalFORMBlanca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solicitado_por', models.CharField(blank=True, max_length=40, null=True, verbose_name='Solicitado por:')),
                ('unidad', models.CharField(blank=True, default='Arco Iris', max_length=24, null=True, verbose_name='Unidad')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.pacientevillablanca')),
            ],
            options={
                'verbose_name': 'Salida Dotación Personal',
                'verbose_name_plural': 'Salidas Dotación Personal',
            },
        ),
        migrations.CreateModel(
            name='PedidoProveedorPersonalBlanca',
            fields=[
                ('cantidad_solicitada', models.IntegerField(default=0)),
                ('cantidad_entregada', models.IntegerField(blank=True, default=0)),
                ('cantidad_entregada_anterior', models.IntegerField(blank=True, default=0)),
                ('fecha_pedido', models.DateField(auto_now=True, verbose_name='Fecha de solicitud')),
                ('fecha_solicitud', models.DateField(blank=True, null=True, verbose_name='Fecha de entrega')),
                ('solicitadoo', models.CharField(blank=True, max_length=40, null=True, verbose_name='Solicitado por:')),
                ('recibido', models.CharField(blank=True, max_length=40, null=True, verbose_name='Recibido por:')),
                ('entregado', models.BooleanField()),
                ('solicitado', models.BooleanField()),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.elementovillablancapersonal')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Proveedor.proveedor')),
            ],
            options={
                'verbose_name': 'Pedido de dotación personal',
                'verbose_name_plural': 'Pedidos de dotación personal',
            },
        ),
        migrations.CreateModel(
            name='PedidoProveedorBlanca',
            fields=[
                ('cantidad_solicitada', models.IntegerField(default=0)),
                ('cantidad_entregada', models.IntegerField(blank=True, default=0)),
                ('cantidad_entregada_anterior', models.IntegerField(blank=True, default=0)),
                ('fecha_pedido', models.DateField(auto_now=True, verbose_name='Fecha de solicitud')),
                ('fecha_solicitud', models.DateField(blank=True, null=True, verbose_name='Fecha de entrega')),
                ('solicitadoo', models.CharField(blank=True, max_length=40, null=True, verbose_name='Solicitado por:')),
                ('recibido', models.CharField(blank=True, max_length=40, null=True, verbose_name='Recibido por:')),
                ('entregado', models.BooleanField()),
                ('solicitado', models.BooleanField()),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.elementovillablanca')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Proveedor.proveedor')),
            ],
            options={
                'verbose_name': 'Pedido de dotación dormitorio',
                'verbose_name_plural': 'Pedidos de dotación dormitorio',
            },
        ),
        migrations.CreateModel(
            name='PedidoProveedorAseoBlanca',
            fields=[
                ('cantidad_solicitada', models.IntegerField(default=0)),
                ('cantidad_entregada', models.IntegerField(blank=True, default=0)),
                ('cantidad_entregada_anterior', models.IntegerField(blank=True, default=0)),
                ('fecha_pedido', models.DateField(auto_now=True, verbose_name='Fecha de solicitud')),
                ('fecha_solicitud', models.DateField(blank=True, null=True, verbose_name='Fecha de entrega')),
                ('solicitadoo', models.CharField(blank=True, max_length=40, null=True, verbose_name='Solicitado por:')),
                ('recibido', models.CharField(blank=True, max_length=40, null=True, verbose_name='Recibido por:')),
                ('entregado', models.BooleanField()),
                ('solicitado', models.BooleanField()),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.elementovillablancaaseo')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Proveedor.proveedor')),
            ],
            options={
                'verbose_name': 'Pedido dotación de aseo personal ',
                'verbose_name_plural': 'Pedidos de aseo personal',
            },
        ),
        migrations.CreateModel(
            name='DevolucionPedidoProveedorPersonalBlanca',
            fields=[
                ('fecha_devolucion', models.DateField(auto_now=True)),
                ('detalle', models.TextField()),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Proveedor.proveedor')),
            ],
            options={
                'verbose_name': 'Devolución pedido',
                'verbose_name_plural': 'Devoluciones pedido de dotación personal',
            },
        ),
        migrations.CreateModel(
            name='DevolucionPedidoProveedorBlanca',
            fields=[
                ('fecha_devolucion', models.DateField(auto_now=True)),
                ('detalle', models.TextField()),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Proveedor.proveedor')),
            ],
            options={
                'verbose_name': 'Devolución pedido',
                'verbose_name_plural': 'Devoluciones pedido de dotación dormitorio',
            },
        ),
        migrations.CreateModel(
            name='DevolucionPedidoProveedorAseoBlanca',
            fields=[
                ('fecha_devolucion', models.DateField(auto_now=True)),
                ('detalle', models.TextField()),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Proveedor.proveedor')),
            ],
            options={
                'verbose_name': 'Devolución pedido',
                'verbose_name_plural': 'Devoluciones pedido de aseo personal ',
            },
        ),
        migrations.CreateModel(
            name='DetalleSalidaDotaciónPersonalBlanca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('especificacion', models.CharField(choices=[('REPOSICIÓN POR ROTO', 'REPOSICIÓN POR ROTO'), ('REPOSICIÓN POR DETERIORO', 'REPOSICIÓN POR DETERIORO')], max_length=24, verbose_name='Especificación')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.elementovillablancapersonal')),
                ('salida_dotacion_personal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.salidadotacionpersonalformblanca')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.pacientevillablanca')),
            ],
            options={
                'verbose_name': 'DETALLE SALIDA',
                'verbose_name_plural': 'DETALLE SALIDA',
            },
        ),
        migrations.CreateModel(
            name='DetallePedidoProveedorPersonalBlanca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_solicitada', models.IntegerField(default=0)),
                ('cantidad_entregada', models.IntegerField(blank=True, default=0)),
                ('cantidad_entregada_anterior', models.IntegerField(blank=True, default=0)),
                ('pedido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.pedidoproveedorpersonalblanca')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.elementovillablancapersonal')),
            ],
            options={
                'verbose_name': 'DETALLE DE PEDIDO PARA DOTACIÓN PERSONAL',
                'verbose_name_plural': 'DETALLE DE PEDIDO PARA DOTACIÓN PERSONAL',
            },
        ),
        migrations.CreateModel(
            name='DetallePedidoProveedorBlanca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_solicitada', models.IntegerField(default=0)),
                ('cantidad_entregada', models.IntegerField(blank=True, default=0)),
                ('cantidad_entregada_anterior', models.IntegerField(blank=True, default=0)),
                ('pedido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.pedidoproveedorblanca')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.elementovillablanca')),
            ],
            options={
                'verbose_name': 'DETALLE DE PEDIDO PARA DOTACIÓN DE DORMITORIO',
                'verbose_name_plural': 'DETALLE DE PEDIDO PARA DOTACIÓN DE DORMITORIO',
            },
        ),
        migrations.CreateModel(
            name='DetallePedidoProveedorAseoBlanca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_solicitada', models.IntegerField(default=0)),
                ('cantidad_entregada', models.IntegerField(blank=True, default=0)),
                ('cantidad_entregada_anterior', models.IntegerField(blank=True, default=0)),
                ('pedido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.pedidoproveedoraseoblanca')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.elementovillablancaaseo')),
            ],
            options={
                'verbose_name': 'DETALLE DE PEDIDO PARA DOTACIÓN DE ASEO PERSONAL',
                'verbose_name_plural': 'DETALLE DE PEDIDO PARA DOTACIÓN DE ASEO PERSONAL',
            },
        ),
        migrations.CreateModel(
            name='DetalleDevolucionPedidoProveedorPersonalBlanca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_devuelta', models.IntegerField()),
                ('motivo', models.CharField(choices=[('PM', 'Producto en mal estado'), ('PV', 'Producto vencido')], max_length=2)),
                ('devolucion_pedido_proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.devolucionpedidoproveedorpersonalblanca')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.elementovillablancapersonal')),
            ],
            options={
                'verbose_name': 'Detalle devolución',
                'verbose_name_plural': 'Detalle devolución',
            },
        ),
        migrations.CreateModel(
            name='DetalleDevolucionPedidoProveedorBlanca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_devuelta', models.IntegerField()),
                ('motivo', models.CharField(choices=[('PM', 'Producto en mal estado'), ('PV', 'Producto vencido')], max_length=2)),
                ('devolucion_pedido_proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.devolucionpedidoproveedorblanca')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.elementovillablanca')),
            ],
            options={
                'verbose_name': 'Detalle devolución',
                'verbose_name_plural': 'Detalle devolución',
            },
        ),
        migrations.CreateModel(
            name='DetalleDevolucionPedidoProveedorAseoBlanca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_devuelta', models.IntegerField()),
                ('motivo', models.CharField(choices=[('PM', 'Producto en mal estado'), ('PV', 'Producto vencido')], max_length=2)),
                ('devolucion_pedido_proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.devolucionpedidoproveedoraseoblanca')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='VillaBlanca.elementovillablancaaseo')),
            ],
            options={
                'verbose_name': 'Detalle devolución',
                'verbose_name_plural': 'Detalle devolución',
            },
        ),
    ]
