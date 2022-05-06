from django.db import models
from .choices import Docs


# Create your models here.
class Elementos(models.Model):
    
    nombreElemento=models.CharField(max_length=100,verbose_name='Elemento')
    fechaElemento=models.DateField(verbose_name='Fecha de creación')
    descripcionElemento=models.TextField(null=True, verbose_name='Descripción')
    def elementos_c(self):
        return ("nombreElemento%s")%(self.nombreElemento)

class Pacientes(models.Model):
    id=models.AutoField(primary_key=True, verbose_name="ID")
    PrimerApellido=models.CharField(max_length=40, verbose_name='Primer apellido')
    SegundoApellido=models.CharField(max_length=40, verbose_name='Segundo apellido')
    PrimerNombre=models.CharField(max_length=40, verbose_name='Primer nombre')
    SegundoNombre=models.CharField(max_length=40, verbose_name='Segundo nombre')
    FechaNacimiento=models.DateField(verbose_name='Fecha de nacimiento',)
    TipoDocumento=models.CharField(max_length=40, null=False, blank=False, choices= Docs, verbose_name='Tipo de cédula', default='F')
    NumeroDocumento=models.CharField(max_length=20, verbose_name='Número de documento')
    FechaIngreso=models.DateField(verbose_name='Fecha de ingreso')
    FechaEgreso=models.DateField(verbose_name='Fecha de salida')
    elementos=models.ManyToManyField(Elementos)
    




class Sedes(models.Model):
 id=models.AutoField(primary_key=True,verbose_name="ID")
 nombreSede=models.CharField(max_length=60, verbose_name="Nombre de la sede")
 direccionSede=models.CharField(max_length=80, verbose_name="Dirección")

class Discapacidad(models.Model):
     id=models.AutoField(primary_key=True, verbose_name="ID")
     nombreDiscapacidad=models.CharField(max_length=40, verbose_name="Discapacidad")






 