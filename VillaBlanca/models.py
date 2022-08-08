from xml.parsers.expat import model
from django.db import models
from inventarioApp.models import PacienteGeneral
from inventarioApp.models import Elemento
from django.core.signing import Signer, BadSignature
from Proveedor.models import Proveedor



# PACIENTE
class pacienteVillaBlanca(PacienteGeneral):
    id=models.AutoField(primary_key=True, verbose_name="ID",)

    def __str__(self):
      texto="{0} {1} {2} {3}"
      return texto.format(self.PrimerApellido,self.SegundoApellido,self.PrimerNombre, self.SegundoNombre)

    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
        ordering= ['PrimerApellido']

# ELEMENTOS


class ElementoVillaBlancaAseo(Elemento):
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    def __str__(self):
      return self.nombreElemento

    class Meta:
        verbose_name='Dotación Aseo Personal'
        verbose_name_plural='Dotación aseo personal'
        ordering= ['nombreElemento']

class ElementoVillaBlancaPersonal(Elemento):
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    talla=models.CharField(max_length=40, verbose_name='Talla',null=True, blank=True)
    descripcionElemento=models.TextField(verbose_name='Descripción',null=True, blank=True)

    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.nombreElemento,self.talla)

    class Meta:
        verbose_name='Dotación personal'
        verbose_name_plural='Dotación personal'
        ordering= ['nombreElemento']


class ElementoVillaBlanca(Elemento):
   
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    def __str__(self):
      return self.nombreElemento

    class Meta:
        verbose_name='Dotación Dormitorio'
        verbose_name_plural='Dotación dormitorio'
        ordering= ['nombreElemento']

#____________________________________________________________________________________



class DetallePedidoBlanca(models.Model):
    cantidad_solicitada = models.IntegerField(default=0)
    cantidad_entregada = models.IntegerField(blank=True,default=0)
    cantidad_entregada_anterior = models.IntegerField(blank=True,default=0)
    producto=models.ForeignKey(ElementoVillaBlanca,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        abstract = True

class DetallePedidoPersonalBlanca(models.Model):
   
    cantidad_solicitada = models.IntegerField( default=0)
    cantidad_entregada = models.IntegerField(blank=True, default=0,)
    cantidad_entregada_anterior = models.IntegerField(blank=True, default=0)
    producto=models.ForeignKey(ElementoVillaBlancaPersonal,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        abstract = True

class DetallePedidoAseoBlanca(models.Model):
    cantidad_solicitada = models.IntegerField( default=0)
    cantidad_entregada = models.IntegerField(blank=True, default=0)
    cantidad_entregada_anterior = models.IntegerField(blank=True, default=0)
    producto = models.ForeignKey(ElementoVillaBlancaAseo,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        abstract = True


class DevolucionPedidoBlanca(models.Model):
    fecha_devolucion = models.DateField(auto_now=True)
    detalle = models.TextField()

    class Meta:
        abstract = True

#_____________________________________________________________
class DetalleDevolucionPedidoBlanca(models.Model):
    MOTIVOS = (
        ('PM', 'Producto en mal estado'),
        ('PV', 'Producto vencido')
    )
    producto = models.ForeignKey(ElementoVillaBlanca,on_delete=models.CASCADE,null=True, blank=True)
    cantidad_devuelta = models.IntegerField()
    motivo = models.CharField(max_length=2, choices=MOTIVOS)
    
    class Meta:
        abstract = True

class DetalleDevolucionPedidoAseoBlanca(models.Model):
    MOTIVOS = (
        ('PM', 'Producto en mal estado'),
        ('PV', 'Producto vencido')
    )
    producto = models.ForeignKey(ElementoVillaBlancaAseo,on_delete=models.CASCADE,null=True, blank=True)
    cantidad_devuelta = models.IntegerField()
    motivo = models.CharField(max_length=2, choices=MOTIVOS)

    class Meta:
        abstract = True
        
class DetalleDevolucionPedidoPersonalBlanca(models.Model):
    MOTIVOS = (
        ('PM', 'Producto en mal estado'),
        ('PV', 'Producto vencido')
    )
    producto = models.ForeignKey(ElementoVillaBlancaPersonal,on_delete=models.CASCADE,null=True, blank=True)
    cantidad_devuelta = models.IntegerField()
    motivo = models.CharField(max_length=2, choices=MOTIVOS)

    class Meta:
        abstract = True
#____________________________________________________________________________________
#PEDIDO
class PedidoBlanca(DetallePedidoBlanca):
    fecha_pedido = models.DateField(auto_now=True,verbose_name='Fecha de solicitud')
    fecha_solicitud=models.DateField(verbose_name='Fecha de entrega', null=True, blank=True, )
    solicitadoo=models.CharField(max_length=40,verbose_name='Solicitado por:', null=True, blank=True,)
    recibido=models.CharField(max_length=40,verbose_name='Recibido por:', null=True, blank=True,)
    entregado= models.BooleanField()
    solicitado= models.BooleanField()

    class Meta:
        abstract = True

    def getFechaPedido(self):
        return self.fecha_pedido.strftime("%d de %m del %Y")

    
class PedidoAseoBlanca(DetallePedidoAseoBlanca):
    fecha_pedido = models.DateField(auto_now=True,verbose_name='Fecha de solicitud')
    fecha_solicitud=models.DateField(verbose_name='Fecha de entrega', null=True, blank=True, )
    solicitadoo=models.CharField(max_length=40,verbose_name='Solicitado por:', null=True, blank=True,)
    recibido=models.CharField(max_length=40,verbose_name='Recibido por:', null=True, blank=True,)
    entregado= models.BooleanField()
    solicitado= models.BooleanField()
    class Meta:
        abstract = True

    def getFechaPedido(self):
        return self.fecha_pedido.strftime("%d de %m del %Y")

    
class PedidoPersonalBlanca(DetallePedidoPersonalBlanca):
    fecha_pedido = models.DateField(auto_now=True,verbose_name='Fecha de solicitud')
    fecha_solicitud=models.DateField(verbose_name='Fecha de entrega', null=True, blank=True, )
    solicitadoo=models.CharField(max_length=40,verbose_name='Solicitado por:', null=True, blank=True,)
    recibido=models.CharField(max_length=40,verbose_name='Recibido por:', null=True, blank=True,)
    entregado= models.BooleanField()
    solicitado= models.BooleanField()
    class Meta:
        abstract = True

    def getFechaPedido(self):
        return self.fecha_pedido.strftime("%d de %m del %Y")

   
#___________________________________________________________________________________________________
class PedidoProveedorBlanca(PedidoBlanca):
    class Meta:
        verbose_name = "Pedido de dotación dormitorio"
        verbose_name_plural = "Pedidos de dotación dormitorio"
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True, blank=True)
    

    def __str__(self):
        return self.fecha_pedido.strftime("Solicitud hecho el %d de %m del %Y")
    

class PedidoProveedorAseoBlanca(PedidoAseoBlanca):
    class Meta:
        verbose_name = "Pedido dotación de aseo personal "
        verbose_name_plural = "Pedidos de aseo personal"
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True, blank=True)


    def __str__(self):
        return self.fecha_pedido.strftime("Pedido hecho el %d de %m del %Y")
    
class PedidoProveedorPersonalBlanca(PedidoPersonalBlanca):
    class Meta:
        verbose_name = "Pedido de dotación personal"
        verbose_name_plural = "Pedidos de dotación personal"
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.fecha_pedido.strftime("Pedido hecho el %d de %m del %Y")
   
#_____________________________________________________________________________________________


class DetallePedidoProveedorBlanca(DetallePedidoBlanca):
    class Meta:
        verbose_name = "DETALLE DE PEDIDO PARA DOTACIÓN DE DORMITORIO"
        verbose_name_plural = "DETALLE DE PEDIDO PARA DOTACIÓN DE DORMITORIO"

    
    pedido = models.ForeignKey(PedidoProveedorBlanca,on_delete=models.CASCADE,null=True, blank=True)
    

    def __str__(self):
        return str(self.producto )

class DetallePedidoProveedorAseoBlanca(DetallePedidoAseoBlanca):
    class Meta:
        verbose_name = "DETALLE DE PEDIDO PARA DOTACIÓN DE ASEO PERSONAL"
        verbose_name_plural = "DETALLE DE PEDIDO PARA DOTACIÓN DE ASEO PERSONAL"

   
    pedido = models.ForeignKey(PedidoProveedorAseoBlanca,on_delete=models.CASCADE,null=True, blank=True)
   

    def __str__(self):
        return str(self.producto )

class DetallePedidoProveedorPersonalBlanca(DetallePedidoPersonalBlanca):
    class Meta:
        verbose_name = "DETALLE DE PEDIDO PARA DOTACIÓN PERSONAL"
        verbose_name_plural = "DETALLE DE PEDIDO PARA DOTACIÓN PERSONAL"

   
    pedido = models.ForeignKey(PedidoProveedorPersonalBlanca,on_delete=models.CASCADE,null=True, blank=True)
   

    def __str__(self):
        return str(self.producto )

# Devolución______________________________________________________________________________________________
class DevolucionPedidoProveedorBlanca(DevolucionPedidoBlanca):
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = "Devolución pedido"
        verbose_name_plural = "Devoluciones pedido de dotación dormitorio"

    def __str__(self):
        return str(self.proveedor)

class DevolucionPedidoProveedorAseoBlanca(DevolucionPedidoBlanca):
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = "Devolución pedido"
        verbose_name_plural = "Devoluciones pedido de aseo personal "

    def __str__(self):
        return str(self.proveedor)
    
class DevolucionPedidoProveedorPersonalBlanca(DevolucionPedidoBlanca):
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = "Devolución pedido"
        verbose_name_plural = "Devoluciones pedido de dotación personal"

    def __str__(self):
        return str(self.proveedor)


class DetalleDevolucionPedidoProveedorBlanca(DetalleDevolucionPedidoBlanca):
    devolucion_pedido_proveedor = models.ForeignKey(DevolucionPedidoProveedorBlanca,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = "Detalle devolución"
        verbose_name_plural = "Detalle devolución"

    def __str__(self):
        return "DDPP" + str(self.devolucion_pedido_proveedor)

class DetalleDevolucionPedidoProveedorAseoBlanca(DetalleDevolucionPedidoAseoBlanca):
    devolucion_pedido_proveedor = models.ForeignKey(DevolucionPedidoProveedorAseoBlanca,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = "Detalle devolución"
        verbose_name_plural = "Detalle devolución"

    def __str__(self):
        return "DDPP" + str(self.devolucion_pedido_proveedor)

class DetalleDevolucionPedidoProveedorPersonalBlanca(DetalleDevolucionPedidoPersonalBlanca):
    devolucion_pedido_proveedor = models.ForeignKey(DevolucionPedidoProveedorPersonalBlanca,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = "Detalle devolución"
        verbose_name_plural = "Detalle devolución"

    def __str__(self):
        return "DDPP" + str(self.devolucion_pedido_proveedor)


# SALIDAS DOTACIÓN PERSONAL_____________________________________________________________________________________
#MODELOS
class SalidaDotaciónPersonalBlanca(models.Model):

   
    solicitado_por=models.CharField(max_length=40,verbose_name="Solicitado por:",null=True, blank=True)
    unidad=models.CharField(max_length=24,verbose_name="Unidad", default="Arco Iris",null=True, blank=True)
    fecha = models.DateField(verbose_name="Fecha",null=True, blank=True)
     
    @staticmethod
    def encryptId(pedido_id):
     signer = Signer()
     return signer.sign(pedido_id)

    @staticmethod
    def decryptId(encrypted_id):

        try:
            signer = Signer()
            return int(signer.unsign(encrypted_id))
        except BadSignature:
            return None

    class Meta:
        abstract = True

class DetalleSalidaBlanca(models.Model):
    ESPECIFICACION = (
        ('REPOSICIÓN POR ROTO', 'REPOSICIÓN POR ROTO'),
        ('REPOSICIÓN POR DETERIORO', 'REPOSICIÓN POR DETERIORO')
    )
    usuario= models.ForeignKey(pacienteVillaBlanca,on_delete=models.CASCADE,null=True, blank=True)
    producto = models.ForeignKey(ElementoVillaBlancaPersonal,on_delete=models.CASCADE,null=True, blank=True)
    cantidad= models.IntegerField()
    especificacion= models.CharField(max_length=24, choices= ESPECIFICACION, verbose_name="Especificación")
    
    class Meta:
        abstract = True

class SalidaDotacionPersonalFORMBlanca(SalidaDotaciónPersonalBlanca):
    usuario = models.ForeignKey(pacienteVillaBlanca,on_delete=models.CASCADE,null=True, blank=True)
    
  
    class Meta:
        verbose_name = "Salida Dotación Personal"
        verbose_name_plural = "Salidas Dotación Personal"

    def __str__(self):
        return str(self.usuario)

class DetalleSalidaDotaciónPersonalBlanca(DetalleSalidaBlanca):
     salida_dotacion_personal = models.ForeignKey(SalidaDotacionPersonalFORMBlanca,on_delete=models.CASCADE,null=True, blank=True)

     class Meta:
        verbose_name = "DETALLE SALIDA"
        verbose_name_plural = "DETALLE SALIDA"

     def __str__(self):
        return "DSDP" + str(self. salida_dotacion_personal)