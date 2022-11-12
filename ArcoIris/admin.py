from django.contrib import admin
from jmespath import search
from import_export import resources
from import_export.admin import ImportExportModelAdmin 
from inventarioApp import app_messages
from django import forms
from django.utils.html import format_html
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.urls import path
from ArcoIris.views import Index,exportUsersPDF


import datetime
# Register your models here.

from .models import DetalleDevolucionPedidoProveedorAseo, DetalleDevolucionPedidoProveedorPersonal, DevolucionPedidoProveedorAseo, DevolucionPedidoProveedorPersonal, ElementoArcoirisPersonal, PedidoProveedorAseo, PedidoProveedorPersonal, pacienteArcoiris
from .models import ElementoArcoiris
from .models import ElementoArcoirisAseo
from .models import ElementoArcoirisPersonal

from Proveedor.models import (
    Proveedor
)

from .models import (
    PedidoProveedor,PedidoProveedorAseo,PedidoProveedorPersonal, DetallePedidoProveedor, DetallePedidoProveedorAseo,DetallePedidoProveedorPersonal,
    DevolucionPedidoProveedor, DetalleDevolucionPedidoProveedor, DetalleSalidaDotaciónPersonal,SalidaDotacionPersonalFORM)

from inventarioApp import app_messages
from django import forms
from functools import partial

#___________________________________________________________________________________________
class  PacientesResource(resources.ModelResource):
      class Meta:
           model= pacienteArcoiris

class PacienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
   list_display= ('id', 'PrimerApellido','SegundoApellido', 'PrimerNombre', 'SegundoNombre', 'FechaNacimiento', 'TipoDocumento','NumeroDocumento','FechaIngreso', 'FechaEgreso',  )
   search_fields= ('id', 'PrimerApellido','SegundoApellido','FechaNacimiento','TipoDocumento','NumeroDocumento','tallaPrenda','tallaCalzado','tallaCalzado')
   list_filter=['modalidad', 'genero', 'TipoDocumento',]
   list_display_links=('PrimerApellido',)

#________________________________________________________________________________________________
 

class ElementoCreationForm(forms.ModelForm):
     model= ElementoArcoiris
     fields= ['id','nombreElemento','fechaElemento','stock','fecha_vencimiento']

     def clean_fecha_vencimiento(self):
        fecha_vencimiento = self.cleaned_data.get("fecha_vencimiento")
        if fecha_vencimiento <= datetime.date.today():
            raise forms.ValidationError(app_messages.DATE_MUST_BE_GREATER)
        return fecha_vencimiento


     def clean_stock(self):
        stock = self.cleaned_data.get("stock")
        if stock < 0:
            raise forms.ValidationError(app_messages.STOCK_MUST_BE_POSITIVE)
        return stock

     def save(self, commit=True):
        ElementoArcoiris = super(ElementoCreationForm, self).save(commit=False)
        if commit:
          ElementoArcoiris.save()
        return ElementoArcoiris
class ElementoCreationFormAseo(forms.ModelForm):
     model= ElementoArcoirisAseo
     fields= ['id','nombreElemento','fechaElemento','stock','fecha_vencimiento']

     def clean_fecha_vencimiento(self):
        fecha_vencimiento = self.cleaned_data.get("fecha_vencimiento")
        if fecha_vencimiento <= datetime.date.today():
            raise forms.ValidationError(app_messages.DATE_MUST_BE_GREATER)
        return fecha_vencimiento


     def clean_stock(self):
        stock = self.cleaned_data.get("stock")
        if stock < 0:
            raise forms.ValidationError(app_messages.STOCK_MUST_BE_POSITIVE)
        return stock

     def save(self, commit=True):
        ElementoArcoirisAseo = super(ElementoCreationFormAseo, self).save(commit=False)
        if commit:
          ElementoArcoiris.save()
        return ElementoArcoirisAseo
class ElementoCreationFormPersonal(forms.ModelForm):
     model= ElementoArcoirisPersonal
     fields= ['id','nombreElemento','fechaElemento','stock','fecha_vencimiento']

     def clean_fecha_vencimiento(self):
        fecha_vencimiento = self.cleaned_data.get("fecha_vencimiento")
        if fecha_vencimiento <= datetime.date.today():
            raise forms.ValidationError(app_messages.DATE_MUST_BE_GREATER)
        return fecha_vencimiento


     def clean_stock(self):
        stock = self.cleaned_data.get("stock")
        if stock < 0:
            raise forms.ValidationError(app_messages.STOCK_MUST_BE_POSITIVE)
        return stock

     def save(self, commit=True):
        ElementoArcoirisPersonal = super(ElementoCreationFormPersonal, self).save(commit=False)
        if commit:
          ElementoArcoirisPersonal.save()
        return ElementoArcoirisPersonal

class ElementoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
     form=ElementoCreationForm
     
     list_display= ('id','nombreElemento','fecha_vencimiento','stock',)
     search_fields=('id','nombreElemento')
     list_filter = ('nombreElemento','fecha_vencimiento' )
     list_display_links=['nombreElemento']

    

     

#____________________________________________________________________________________________


     class  ElementoResource(resources.ModelResource):
      class Meta:
           model= ElementoArcoirisAseo

class ElementoAdminAseo(ImportExportModelAdmin,admin.ModelAdmin):
     form=ElementoCreationFormAseo
     list_display= ('id','nombreElemento','fechaElemento','stock','fecha_vencimiento')
     search_fields=('id','nombreElemento')
     list_filter = ('nombreElemento','fecha_vencimiento' )
     list_display_links=['nombreElemento']


#____________________________________________________________________________________________
     class  ElementoResource(resources.ModelResource):
      class Meta:
           model= ElementoArcoirisPersonal


class ElementoAdminPersonal(ImportExportModelAdmin,admin.ModelAdmin):
    
     form=ElementoCreationFormPersonal
     list_display= ('id','nombreElemento','talla','fechaElemento','stock',)
     search_fields=('id','nombreElemento','talla')
     list_filter = ('talla','nombreElemento','fecha_vencimiento' )
     list_display_links=['nombreElemento']


#_____________________________________________________________________
# Pedido Proveedor
class DetallePedidoProveedorFormSet(forms.BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
        
            cantidad_entregada = form.instance.cantidad_entregada
            cantidad_solicitada = form.instance.cantidad_solicitada
            if cantidad_entregada < 0:
                raise forms.ValidationError(app_messages.CANTIDAD_ENTREGADA_MUST_BE_POSITIVE)
            elif cantidad_solicitada < 0:
                    raise forms.ValidationError(app_messages.CANTIDAD_SOLICITADA_MUST_BE_POSITIVE)
            elif cantidad_entregada > cantidad_solicitada:
                    raise forms.ValidationError(app_messages.CANTIDAD_ENTREGADA_MUST_BE_LESS)
            
        


class DetallePedidoProveedorInline(admin.TabularInline):
    formset = DetallePedidoProveedorFormSet
    model = DetallePedidoProveedor
    fields = ['producto', 'cantidad_solicitada','cantidad_entregada']


    extra = 1
    min_num = 1

class DetallePedidoProveedorInlineAseo(admin.TabularInline):
    formset = DetallePedidoProveedorFormSet
    model = DetallePedidoProveedorAseo
    fields = ['producto', 'cantidad_solicitada','cantidad_entregada']

    extra = 1
    min_num = 1

class DetallePedidoProveedorInlinePersonal(admin.TabularInline):
    formset = DetallePedidoProveedorFormSet
    model = DetallePedidoProveedorPersonal
    fields = ['producto', 'cantidad_solicitada','cantidad_entregada']
    extra = 1
    min_num = 1



class PedidoProveedorForm(forms.ModelForm):
    class Meta:
        model = PedidoProveedor
      
        fields = ['proveedor',]

class PedidoProveedorFormAseo(forms.ModelForm):
    class Meta:
        model = PedidoProveedorAseo
      
        fields = ['proveedor',]

class PedidoProveedorFormPersonal(forms.ModelForm):
    class Meta:
        model = PedidoProveedorPersonal
      
        fields = ['proveedor',]


      #  fields = ['proveedor', 'total_pagado']

   # def clean_total_pagado(self):
    #    total_pagado = self.cleaned_data.get("total_pagado")
     #   if total_pagado < 0:
      #      raise forms.ValidationError(app_messages.TOTAL_PAGADO_MUST_BE_POSITIVE)
       # elif total_pagado > float(self.instance.precio_total):
        #    raise forms.ValidationError(app_messages.TOTAL_PAGADO_MUST_BE_LESS)
        #return total_pagado


#_________________________________________________________________________

class PedidoProveedorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = PedidoProveedorForm
   
    
    fields = ['proveedor','solicitadoo','solicitado','recibido','entregado','fecha_solicitud']
   
    list_display = ('id','proveedor','solicitadoo','fecha_pedido','recibido','fecha_solicitud','solicitado','entregado')
    list_filter = ('fecha_pedido','fecha_solicitud' )
    search_fields = ['fecha_pedido','fecha_solicitud', 'proveedor__nombre']
    list_display_links=['proveedor']
    inlines = [DetallePedidoProveedorInline]
    
    def get_changelist_formset(self, request, **kwargs):
        defaults = {
            "formfield_callback": partial(super(PedidoProveedorAdmin, self).formfield_for_dbfield, request=request),
            "form": PedidoProveedorForm,
        }
        defaults.update(kwargs)
        return forms.models.modelformset_factory(PedidoProveedor,
                                                 extra=0,
                                                 fields=self.list_editable, **defaults)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)

        for obj in formset.deleted_objects:
            if obj.cantidad_entregada is None:
                obj.cantidad_entregada = 0
            producto = obj.producto
            producto.stock -= obj.cantidad_entregada
            producto.save()
            obj.delete()
        for instance in instances:
            if instance.cantidad_entregada is None:
                instance.cantidad_entregada = 0
            if instance.cantidad_entregada_anterior is None:
                instance.cantidad_entregada_anterior = 0
            producto = instance.producto

            if instance.cantidad_entregada > instance.cantidad_entregada_anterior:
                cantidad_entregada = instance.cantidad_entregada - instance.cantidad_entregada_anterior
                producto.stock += cantidad_entregada
            else:
                cantidad_entregada = instance.cantidad_entregada_anterior - instance.cantidad_entregada
                producto.stock -= cantidad_entregada

            instance.cantidad_entregada_anterior = instance.cantidad_entregada
            producto.save()
            instance.save()
        formset.save_m2m()

class PedidoProveedorAdminAseo(ImportExportModelAdmin,admin.ModelAdmin):
    form = PedidoProveedorFormAseo
   
    fields = ['proveedor','solicitadoo','solicitado','recibido','entregado','fecha_solicitud']
   
    list_display = ('id','proveedor','solicitadoo','fecha_pedido','recibido','fecha_solicitud','solicitado','entregado')
    list_filter = ('fecha_pedido','fecha_solicitud' )
    search_fields = ['fecha_pedido','fecha_solicitud', 'proveedor__nombre']
    list_display_links=['proveedor']

    inlines = [DetallePedidoProveedorInlineAseo]
    
    def get_changelist_formset(self, request, **kwargs):
        defaults = {
            "formfield_callback": partial(super(PedidoProveedorAdminAseo, self).formfield_for_dbfield, request=request),
            "form": PedidoProveedorFormAseo,
        }
        defaults.update(kwargs)
        return forms.models.modelformset_factory(PedidoProveedorAseo,
                                                 extra=0,
                                                 fields=self.list_editable, **defaults)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)

        for obj in formset.deleted_objects:
            if obj.cantidad_entregada is None:
                obj.cantidad_entregada = 0
            producto = obj.producto
            producto.stock -= obj.cantidad_entregada
            producto.save()
            obj.delete()
        for instance in instances:
            if instance.cantidad_entregada is None:
                instance.cantidad_entregada = 0
            if instance.cantidad_entregada_anterior is None:
                instance.cantidad_entregada_anterior = 0
            producto = instance.producto

            if instance.cantidad_entregada > instance.cantidad_entregada_anterior:
                cantidad_entregada = instance.cantidad_entregada - instance.cantidad_entregada_anterior
                producto.stock += cantidad_entregada
            else:
                cantidad_entregada = instance.cantidad_entregada_anterior - instance.cantidad_entregada
                producto.stock -= cantidad_entregada

            instance.cantidad_entregada_anterior = instance.cantidad_entregada
            producto.save()
            instance.save()
        formset.save_m2m()

class PedidoProveedorAdminPersonal(ImportExportModelAdmin,admin.ModelAdmin):
    form = PedidoProveedorFormPersonal
   
    
    fields = ['proveedor','solicitadoo','solicitado','recibido','entregado','fecha_solicitud']
   
    list_display = ('id','proveedor','solicitadoo','fecha_pedido','recibido','fecha_solicitud','solicitado','entregado')
    list_filter = ('fecha_pedido','fecha_solicitud' )
    search_fields = ['fecha_pedido','fecha_solicitud', 'proveedor__nombre']
    list_display_links=['proveedor']

    inlines = [DetallePedidoProveedorInlinePersonal]

    def solicitado_(self, obj):
     return obj.fecha_pedido == True
    solicitado_.boolean = True
    
    def get_changelist_formset(self, request, **kwargs):
        defaults = {
            "formfield_callback": partial(super(PedidoProveedorAdminPersonal, self).formfield_for_dbfield, request=request),
            "form": PedidoProveedorFormPersonal,
        }
        defaults.update(kwargs)
        return forms.models.modelformset_factory(PedidoProveedorPersonal,
                                                 extra=0,
                                                 fields=self.list_editable, **defaults)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)

        for obj in formset.deleted_objects:
            if obj.cantidad_entregada is None:
                obj.cantidad_entregada = 0
            producto = obj.producto
            producto.stock -= obj.cantidad_entregada
            producto.save()
            obj.delete()
        for instance in instances:
            if instance.cantidad_entregada is None:
                instance.cantidad_entregada = 0
            if instance.cantidad_entregada_anterior is None:
                instance.cantidad_entregada_anterior = 0
            producto = instance.producto

            if instance.cantidad_entregada > instance.cantidad_entregada_anterior:
                cantidad_entregada = instance.cantidad_entregada - instance.cantidad_entregada_anterior
                producto.stock += cantidad_entregada
            else:
                cantidad_entregada = instance.cantidad_entregada_anterior - instance.cantidad_entregada
                producto.stock -= cantidad_entregada

            instance.cantidad_entregada_anterior = instance.cantidad_entregada
            producto.save()
            instance.save()
        formset.save_m2m()


    

#___________________________________________________________________________________
class DetalleDevolucionPedidoProveedorInline(admin.TabularInline):
    model = DetalleDevolucionPedidoProveedor
    extra = 1
    min_num = 1
    show_change_link = False

class DetalleDevolucionPedidoProveedorInlineAseo(admin.TabularInline):
    model = DetalleDevolucionPedidoProveedorAseo
    extra = 1
    min_num = 1
    show_change_link = False

class DetalleDevolucionPedidoProveedorInlinePersonal(admin.TabularInline):
    model = DetalleDevolucionPedidoProveedorPersonal
    extra = 1
    min_num = 1
    show_change_link = False


class DevolucionPedidoProveedorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    fields = ['proveedor', 'detalle']
    list_filter = ['fecha_devolucion']
    search_fields = ['proveedor__nombre']
    list_display = ['id','proveedor', 'fecha_devolucion', 'detalle']
    inlines = [DetalleDevolucionPedidoProveedorInline]

    
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        stocks = {}
        for obj in formset.deleted_objects:
            if obj.cantidad_devuelta  is None:
                obj.cantidad_devuelta  = 0
            producto = obj.producto
            producto.stock += obj.cantidad_devuelta 
            producto.save()
            obj.delete()
        for instance in instances:
            if instance.cantidad_devuelta is None:
                instance.cantidad_devuelta = 0
            producto = instance.producto
            stock_actual = stocks.get(producto)
            if stock_actual:
                stocks[producto] -= instance.cantidad_devuelta
                producto.stock = stocks[producto]
            else:
                stocks[producto] = producto.stock
                stocks[producto] -= instance.cantidad_devuelta
                producto.stock = stocks[producto]
            producto.save()
            instance.save()
        formset.save_m2m()

class DevolucionPedidoProveedorAdminAseo(ImportExportModelAdmin,admin.ModelAdmin):
    fields = ['proveedor', 'detalle']
    list_filter = ['fecha_devolucion']
    search_fields = ['proveedor__nombre']
    list_display = ['id','proveedor', 'fecha_devolucion', 'detalle']
    inlines = [DetalleDevolucionPedidoProveedorInlineAseo]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        stocks = {}
        for obj in formset.deleted_objects:
            if obj.cantidad_devuelta  is None:
                obj.cantidad_devuelta  = 0
            producto = obj.producto
            producto.stock += obj.cantidad_devuelta 
            producto.save()
            obj.delete()
        for instance in instances:
            if instance.cantidad_devuelta is None:
                instance.cantidad_devuelta = 0
            producto = instance.producto
            stock_actual = stocks.get(producto)
            if stock_actual:
                stocks[producto] -= instance.cantidad_devuelta
                producto.stock = stocks[producto]
            else:
                stocks[producto] = producto.stock
                stocks[producto] -= instance.cantidad_devuelta
                producto.stock = stocks[producto]
            producto.save()
            instance.save()
        formset.save_m2m()

class DevolucionPedidoProveedorAdminPersonal(ImportExportModelAdmin,admin.ModelAdmin):
    fields = ['proveedor', 'detalle']
    list_filter = ['fecha_devolucion']
    search_fields = ['proveedor__nombre']
    list_display = ['id','proveedor', 'fecha_devolucion', 'detalle']
    inlines = [DetalleDevolucionPedidoProveedorInlinePersonal]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        stocks = {}
        for obj in formset.deleted_objects:
            if obj.cantidad_devuelta  is None:
                obj.cantidad_devuelta  = 0
            producto = obj.producto
            producto.stock += obj.cantidad_devuelta 
            producto.save()
            obj.delete()
        for instance in instances:
            if instance.cantidad_devuelta is None:
                instance.cantidad_devuelta = 0
            producto = instance.producto
            stock_actual = stocks.get(producto)
            if stock_actual:
                stocks[producto] -= instance.cantidad_devuelta
                producto.stock = stocks[producto]
            else:
                stocks[producto] = producto.stock
                stocks[producto] -= instance.cantidad_devuelta
                producto.stock = stocks[producto]
            producto.save()
            instance.save()
        formset.save_m2m()


#SALIDAS_____________________________________________________________________
class DetalleSalidaDotaciónPersonalInline(admin.TabularInline):
    model =  DetalleSalidaDotaciónPersonal
    extra = 1
    min_num = 1
    show_change_link = False
##ADMIN

    class  SalidaResource(resources.ModelResource):
        class Meta:
            model= SalidaDotacionPersonalFORM

class SalidaDotaciónPersonalAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    fields = ['solicitado_por','unidad','fecha']
    list_filter = ['fecha','unidad']
    search_fields = ['solicitado_por','unidad']
    list_display = ['id','solicitado_por', 'unidad','fecha']
    inlines = [DetalleSalidaDotaciónPersonalInline]
    actions = ['generar_pdf','generar_pdf_2']

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        stocks = {}
        for obj in formset.deleted_objects:
            if obj.cantidad is None:
                obj.cantidad= 0
            producto = obj.producto
            producto.stock += obj.cantidad
            producto.save()
            obj.delete()
        for instance in instances:
            if instance.cantidad is None:
                instance.cantidad = 0
            producto = instance.producto
            stock_actual = stocks.get(producto)
            if stock_actual:
                stocks[producto] -= instance.cantidad
                producto.stock = stocks[producto]
            else:
                stocks[producto] = producto.stock
                stocks[producto] -= instance.cantidad
                producto.stock = stocks[producto]
            producto.save()
            instance.save()
        formset.save_m2m()

            
    def generar_pdf(self, request, queryset):
     id = queryset[0].id
     pedido_id = SalidaDotacionPersonalFORM.encryptId(id)
     url = reverse('report:exportArcoIris', kwargs={'pedido_id': pedido_id})
     return HttpResponseRedirect(url)

    generar_pdf.short_description = "Generar documento 'Registro de salidas para solicitud y entrega de dotación personal'"


    def generar_pdf_2(self, request, queryset):
     id = queryset[0].id
     pedido_id = SalidaDotacionPersonalFORM.encryptId(id)
     url = reverse('report:exportEntregaArcoIris', kwargs={'pedido_id': pedido_id})
     return HttpResponseRedirect(url)

    generar_pdf_2.short_description = "Generar documento 'solicitud y entrega de insumos'"

    #@admin.action(description='Generate PDF file')
    #def generatePDF(modeladmin, request, queryset):
     #   url ='templates/admin/person/?pks=' + ','.join(str([q.pk for q in queryset]))
       
    #actions = [generatePDF]
    
 
     

admin.site.register(pacienteArcoiris, PacienteAdmin)
admin.site.register(ElementoArcoiris,ElementoAdmin)
admin.site.register(ElementoArcoirisAseo,ElementoAdminAseo)
admin.site.register(ElementoArcoirisPersonal,ElementoAdminPersonal)
admin.site.register(PedidoProveedor, PedidoProveedorAdmin)
admin.site.register(PedidoProveedorAseo, PedidoProveedorAdminAseo)
admin.site.register(PedidoProveedorPersonal, PedidoProveedorAdminPersonal)
admin.site.register(DevolucionPedidoProveedor, DevolucionPedidoProveedorAdmin)
admin.site.register(DevolucionPedidoProveedorAseo, DevolucionPedidoProveedorAdminAseo)
admin.site.register(DevolucionPedidoProveedorPersonal, DevolucionPedidoProveedorAdminPersonal)
admin.site.register(SalidaDotacionPersonalFORM,SalidaDotaciónPersonalAdmin)
