from django.db import models
from .choices import Docs
from .choices import modalidadd
from .choices import generoo
from .choices import tiposalida
from .choices import dotacion
from .choices import unidadmedida




# Create your models here.
class Elemento(models.Model):
    nombreElemento=models.CharField(max_length=100,verbose_name='Elemento',null=True)
    fechaElemento=models.DateField(auto_now_add=True,verbose_name='Fecha de creación')
    stock=models.IntegerField(null=True,verbose_name='Cantidad', default=10)
    unidadmedida=models.CharField(max_length=40,choices=unidadmedida,verbose_name='Unidad de medidad',default='ninguna',null=True)
    fecha_vencimiento= models.DateField(verbose_name="Fecha de vencimiento",null=True, blank=True)
    
    
    class Meta:
       abstract = True


class PacienteGeneral(models.Model):
    
    modalidad=models.CharField(max_length=40, choices=modalidadd, verbose_name='Modalidad',default='a',null=True)
    genero=models.CharField(max_length=40,choices=generoo,verbose_name='Género',default='g',null=True)
    PrimerApellido=models.CharField(max_length=40, verbose_name='Primer apellido',null=True)
    SegundoApellido=models.CharField(max_length=40, verbose_name='Segundo apellido', null=True, blank=True, )
    PrimerNombre=models.CharField(max_length=40, verbose_name='Primer  nombre')
    SegundoNombre=models.CharField(max_length=40, verbose_name='Segundo nombre', null=True, blank=True, )
    FechaNacimiento=models.DateField(verbose_name='Fecha de nacimiento',null=True,)
    TipoDocumento=models.CharField( max_length=40, null=True, choices= Docs, verbose_name='Tipo de documento', default='F')
    NumeroDocumento=models.CharField(max_length=20, verbose_name='Número de documento')
    tallaPrenda=models.CharField(max_length=20, verbose_name='Talla de prenda')
    tallaCalzado=models.CharField(max_length=20, verbose_name='Talla de calzado')
    FechaIngreso=models.DateField(auto_now_add=True, verbose_name='Fecha de ingreso',null=True,)
    FechaEgreso=models.DateField(verbose_name='Fecha de salida', null=True, blank=True, )
    tiposalida=models.CharField(max_length=40,choices=tiposalida,verbose_name='Motivo de salida',default='ninguna',null=True, blank=True)
    

    class Meta: 
         abstract = True
    
   







 







 