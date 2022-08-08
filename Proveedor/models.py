from django.db import models



# Create your models here.
class Proveedor(models.Model):

     class Meta:
        verbose_name='Proveedor'
        verbose_name_plural='Proveedores'

   
     nombreProveedor=models.CharField(max_length=40,verbose_name='Nombre',null=True)
     NumeroContacto=models.CharField(max_length=40,verbose_name='Número de contacto',null=True,blank=True,)
     Correo=models.CharField(max_length=40,verbose_name='Correo',null=True, blank=True,)
     Nit=models.IntegerField(null=True,verbose_name='Nit',)
     
     def __str__(self):
      return self.nombreProveedor

        

