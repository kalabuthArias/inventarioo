from django.db import models

# Create your models here.
from xml.parsers.expat import model
from django.db import models
from inventarioApp.models import PacienteGeneral
from inventarioApp.models import Elemento
from django.core.signing import Signer, BadSignature
from Proveedor.models import Proveedor



# PACIENTE
class pacienteVillaJimena(PacienteGeneral):
    id=models.AutoField(primary_key=True, verbose_name="ID",)

    def __str__(self):
      texto="{0} {1} {2} {3}"
      return texto.format(self.PrimerApellido,self.SegundoApellido,self.PrimerNombre, self.SegundoNombre)

    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
        ordering= ['PrimerApellido']

# ELEMENTOS


class ElementoVillaJimenaAseo(Elemento):
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    def __str__(self):
      return self.nombreElemento

    class Meta:
        verbose_name='Dotación Aseo Personal'
        verbose_name_plural='Dotación aseo personal'
        ordering= ['nombreElemento']

class ElementoVillaJimenaPersonal(Elemento):
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


class ElementoVillaJimena(Elemento):
   
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    def __str__(self):
      return self.nombreElemento

    class Meta:
        verbose_name='Dotación Dormitorio'
        verbose_name_plural='Dotación dormitorio'
        ordering= ['nombreElemento']

#____________________________________________________________________________________



class DetallePedidoJimena(models.Model):
    cantidad_solicitada = models.IntegerField(default=0)
    cantidad_entregada = models.IntegerField(blank=True,default=0)
    cantidad_entregada_anterior = models.IntegerField(blank=True,default=0)
    producto=models.ForeignKey(ElementoVillaJimena,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        abstract = True

class DetallePedidoPersonalJimena(models.Model):
   
    cantidad_solicitada = models.IntegerField( default=0)
    cantidad_entregada = models.IntegerField(blank=True, default=0,)
    cantidad_entregada_anterior = models.IntegerField(blank=True, default=0)
    producto=models.ForeignKey(ElementoVillaJimenaPersonal,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        abstract = True

class DetallePedidoAseoJimena(models.Model):
    cantidad_solicitada = models.IntegerField( default=0)
    cantidad_entregada = models.IntegerField(blank=True, default=0)
    cantidad_entregada_anterior = models.IntegerField(blank=True, default=0)
    producto = models.ForeignKey(ElementoVillaJimenaAseo,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        abstract = True


class DevolucionPedidoJimena(models.Model):
    fecha_devolucion = models.DateField(auto_now=True)
    detalle = models.TextField()

    class Meta:
        abstract = True

#_____________________________________________________________
class DetalleDevolucionPedidoJimena(models.Model):
    MOTIVOS = (
        ('PM', 'Producto en mal estado'),
        ('PV', 'Producto vencido')
    )
    producto = models.ForeignKey(ElementoVillaJimena,on_delete=models.CASCADE,null=True, blank=True)
    cantidad_devuelta = models.IntegerField()
    motivo = models.CharField(max_length=2, choices=MOTIVOS)
    
    class Meta:
        abstract = True

class DetalleDevolucionPedidoAseoJimena(models.Model):
    MOTIVOS = (
        ('PM', 'Producto en mal estado'),
        ('PV', 'Producto vencido')
    )
    producto = models.ForeignKey(ElementoVillaJimenaAseo,on_delete=models.CASCADE,null=True, blank=True)
    cantidad_devuelta = models.IntegerField()
    motivo = models.CharField(max_length=2, choices=MOTIVOS)

    class Meta:
        abstract = True
        
class DetalleDevolucionPedidoPersonalJimena(models.Model):
    MOTIVOS = (
        ('PM', 'Producto en mal estado'),
        ('PV', 'Producto vencido')
    )
    producto = models.ForeignKey(ElementoVillaJimenaPersonal,on_delete=models.CASCADE,null=True, blank=True)
    cantidad_devuelta = models.IntegerField()
    motivo = models.CharField(max_length=2, choices=MOTIVOS)

    class Meta:
        abstract = True
#____________________________________________________________________________________
#PEDIDO
class PedidoJimena(DetallePedidoJimena):
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

    
class PedidoAseoJimena(DetallePedidoAseoJimena):
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

    
class PedidoPersonalJimena(DetallePedidoPersonalJimena):
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
class PedidoProveedorJimena(PedidoJimena):
    class Meta:
        verbose_name = "Pedido de dotación dormitorio"
        verbose_name_plural = "Pedidos de dotación dormitorio"
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True, blank=True)
    

    def __str__(self):
        return self.fecha_pedido.strftime("Solicitud hecho el %d de %m del %Y")
    

   


class PedidoProveedorAseoJimena(PedidoAseoJimena):
    class Meta:
        verbose_name = "Pedido dotación de aseo personal "
        verbose_name_plural = "Pedidos de aseo personal"
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True, blank=True)


    def __str__(self):
        return self.fecha_pedido.strftime("Pedido hecho el %d de %m del %Y")
    
    

class PedidoProveedorPersonalJimena(PedidoPersonalJimena):
    class Meta:
        verbose_name = "Pedido de dotación personal"
        verbose_name_plural = "Pedidos de dotación personal"
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True, blank=True)
    

    def __str__(self):
        return self.fecha_pedido.strftime("Pedido hecho el %d de %m del %Y")
#_____________________________________________________________________________________________


class DetallePedidoProveedorJimena(DetallePedidoJimena):
    class Meta:
        verbose_name = "DETALLE DE PEDIDO PARA DOTACIÓN DE DORMITORIO"
        verbose_name_plural = "DETALLE DE PEDIDO PARA DOTACIÓN DE DORMITORIO"

    pedido = models.ForeignKey(PedidoProveedorJimena,on_delete=models.CASCADE,null=True, blank=True)
    
    def __str__(self):
        return str(self.producto )

class DetallePedidoProveedorAseoJimena(DetallePedidoAseoJimena):
    class Meta:
        verbose_name = "DETALLE DE PEDIDO PARA DOTACIÓN DE ASEO PERSONAL"
        verbose_name_plural = "DETALLE DE PEDIDO PARA DOTACIÓN DE ASEO PERSONAL"

  
    pedido = models.ForeignKey(PedidoProveedorAseoJimena,on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return str(self.producto )

class DetallePedidoProveedorPersonalJimena(DetallePedidoPersonalJimena):
    class Meta:
        verbose_name = "DETALLE DE PEDIDO PARA DOTACIÓN PERSONAL"
        verbose_name_plural = "DETALLE DE PEDIDO PARA DOTACIÓN PERSONAL"

    
    pedido = models.ForeignKey(PedidoProveedorPersonalJimena,on_delete=models.CASCADE,null=True, blank=True)
   

    def __str__(self):
        return str(self.producto )

# Devolución______________________________________________________________________________________________
class DevolucionPedidoProveedorJimena(DevolucionPedidoJimena):
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = "Devolución pedido"
        verbose_name_plural = "Devoluciones pedido de dotación dormitorio"

    def __str__(self):
        return str(self.proveedor)

class DevolucionPedidoProveedorAseoJimena(DevolucionPedidoJimena):
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = "Devolución pedido"
        verbose_name_plural = "Devoluciones pedido de aseo personal "

    def __str__(self):
        return str(self.proveedor)
    
class DevolucionPedidoProveedorPersonalJimena(DevolucionPedidoJimena):
    id=models.AutoField(primary_key=True, verbose_name="ID",)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = "Devolución pedido"
        verbose_name_plural = "Devoluciones pedido de dotación personal"

    def __str__(self):
        return str(self.proveedor)


class DetalleDevolucionPedidoProveedorJimena(DetalleDevolucionPedidoJimena):
    devolucion_pedido_proveedor = models.ForeignKey(DevolucionPedidoProveedorJimena,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = "Detalle devolución"
        verbose_name_plural = "Detalle devolución"

    def __str__(self):
        return "DDPP" + str(self.devolucion_pedido_proveedor)

class DetalleDevolucionPedidoProveedorAseoJimena(DetalleDevolucionPedidoAseoJimena):
    devolucion_pedido_proveedor = models.ForeignKey(DevolucionPedidoProveedorAseoJimena,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = "Detalle devolución"
        verbose_name_plural = "Detalle devolución"

    def __str__(self):
        return "DDPP" + str(self.devolucion_pedido_proveedor)

class DetalleDevolucionPedidoProveedorPersonalJimena(DetalleDevolucionPedidoPersonalJimena):
    devolucion_pedido_proveedor = models.ForeignKey(DevolucionPedidoProveedorPersonalJimena,on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = "Detalle devolución"
        verbose_name_plural = "Detalle devolución"

    def __str__(self):
        return "DDPP" + str(self.devolucion_pedido_proveedor)


# SALIDAS DOTACIÓN PERSONAL_____________________________________________________________________________________
#MODELOS
class SalidaDotaciónPersonalJimena(models.Model):

   
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

class DetalleSalidaJimena(models.Model):
    ESPECIFICACION = (
        ('REPOSICIÓN POR ROTO', 'REPOSICIÓN POR ROTO'),
        ('REPOSICIÓN POR DETERIORO', 'REPOSICIÓN POR DETERIORO')
    )
    usuario= models.ForeignKey(pacienteVillaJimena,on_delete=models.CASCADE,null=True, blank=True)
    producto = models.ForeignKey(ElementoVillaJimenaPersonal,on_delete=models.CASCADE,null=True, blank=True)
    cantidad= models.IntegerField()
    especificacion= models.CharField(max_length=24, choices= ESPECIFICACION, verbose_name="Especificación")
    
    class Meta:
        abstract = True

class SalidaDotacionPersonalFORMJimena(SalidaDotaciónPersonalJimena):
    usuario = models.ForeignKey(pacienteVillaJimena,on_delete=models.CASCADE,null=True, blank=True)
    
  
    class Meta:
        verbose_name = "Salida Dotación Personal"
        verbose_name_plural = "Salidas Dotación Personal"

    def __str__(self):
        return str(self.usuario)

class DetalleSalidaDotaciónPersonalJimena(DetalleSalidaJimena):
     salida_dotacion_personal = models.ForeignKey(SalidaDotacionPersonalFORMJimena,on_delete=models.CASCADE,null=True, blank=True)

     class Meta:
        verbose_name = "DETALLE SALIDA"
        verbose_name_plural = "DETALLE SALIDA"

     def __str__(self):
        return "DSDP" + str(self. salida_dotacion_personal)