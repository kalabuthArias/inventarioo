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



import datetime


# Register your models here.

from .models import DetalleDevolucionPedidoProveedorAseoAdriana, DetalleDevolucionPedidoProveedorPersonalAdriana, DevolucionPedidoProveedorAseoAdriana, DevolucionPedidoProveedorPersonalAdriana, ElementoVillaAdrianaPersonal, PedidoProveedorAseoAdriana, PedidoProveedorPersonalAdriana, pacienteVillaAdriana
from .models import ElementoVillaAdriana
from .models import ElementoVillaAdrianaAseo
from .models import ElementoVillaAdrianaPersonal

from Proveedor.models import (
    Proveedor
)

from .models import (
     PedidoProveedorAdriana,PedidoProveedorAseoAdriana,PedidoProveedorPersonalAdriana, DetallePedidoProveedorAdriana, DetallePedidoProveedorAseoAdriana,DetallePedidoProveedorPersonalAdriana,
    DevolucionPedidoProveedorAdriana, DetalleDevolucionPedidoProveedorAdriana, DetalleSalidaDotaciónPersonalAdriana,SalidaDotacionPersonalFORMAdriana)

from inventarioApp import app_messages
from django import forms
from functools import partial

#___________________________________________________________________________________________
class  PacientesResource(resources.ModelResource):
      class Meta:
           model= pacienteVillaAdriana

class PacienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
   list_display= ('id', 'PrimerApellido','SegundoApellido', 'PrimerNombre', 'SegundoNombre', 'FechaNacimiento', 'TipoDocumento','NumeroDocumento','FechaIngreso', 'FechaEgreso',  )
   search_fields= ('id', 'PrimerApellido','SegundoApellido','FechaNacimiento','TipoDocumento','NumeroDocumento','tallaPrenda','tallaCalzado','tallaCalzado')
   list_filter=['modalidad', 'genero', 'TipoDocumento',]
   list_display_links=('PrimerApellido',)

#________________________________________________________________________________________________
   class  ElementoResource(resources.ModelResource):
      class Meta:
           model= ElementoVillaAdriana

class ElementoCreationForm(forms.ModelForm):
     model= ElementoVillaAdriana
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
        ElementoVillaAdriana = super(ElementoCreationForm, self).save(commit=False)
        if commit:
          ElementoVillaAdriana.save()
        return ElementoVillaAdriana
class ElementoCreationFormAseo(forms.ModelForm):
     model= ElementoVillaAdrianaAseo
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
        ElementoVillaAdrianaAseo = super(ElementoCreationFormAseo, self).save(commit=False)
        if commit:
          ElementoAdminAseo.save()
        return ElementoVillaAdrianaAseo
class ElementoCreationFormPersonal(forms.ModelForm):
     model= ElementoVillaAdrianaPersonal
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
        ElementoVillaAdrianaPersonal = super(ElementoCreationFormPersonal, self).save(commit=False)
        if commit:
          ElementoVillaAdrianaPersonal.save()
        return ElementoVillaAdrianaPersonal

class ElementoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
     form=ElementoCreationForm
     
     list_display= ('id','nombreElemento','fecha_vencimiento','stock',)
     search_fields=('id','nombreElemento')
     list_display_links=('nombreElemento',)

    

     

#____________________________________________________________________________________________


     class  ElementoResource(resources.ModelResource):
      class Meta:
           model= ElementoVillaAdrianaAseo

class ElementoAdminAseo(ImportExportModelAdmin,admin.ModelAdmin):
     form=ElementoCreationFormAseo
     list_display= ('id','nombreElemento','fechaElemento','stock','fecha_vencimiento')
     search_fields=('id','nombreElemento')
     list_display_links=('nombreElemento',)


#____________________________________________________________________________________________
     class  ElementoResource(resources.ModelResource):
      class Meta:
           model= ElementoVillaAdrianaPersonal


class ElementoAdminPersonal(ImportExportModelAdmin,admin.ModelAdmin):
    
     form=ElementoCreationFormPersonal
     list_display= ('id','nombreElemento','talla','fechaElemento','stock',)
     search_fields=('id','nombreElemento','talla')
     list_display_links=('nombreElemento',)


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
    model = DetallePedidoProveedorAdriana
    fields = ['producto', 'cantidad_solicitada','cantidad_entregada']


    extra = 1
    min_num = 1

class DetallePedidoProveedorInlineAseo(admin.TabularInline):
    formset = DetallePedidoProveedorFormSet
    model = DetallePedidoProveedorAseoAdriana
    fields = ['producto', 'cantidad_solicitada','cantidad_entregada']

    extra = 1
    min_num = 1

class DetallePedidoProveedorInlinePersonal(admin.TabularInline):
    formset = DetallePedidoProveedorFormSet
    model = DetallePedidoProveedorPersonalAdriana
    fields = ['producto', 'cantidad_solicitada','cantidad_entregada']
    extra = 1
    min_num = 1



class PedidoProveedorForm(forms.ModelForm):
    class Meta:
        model = PedidoProveedorAdriana
      
        fields = ['proveedor',]

class PedidoProveedorFormAseo(forms.ModelForm):
    class Meta:
        model = PedidoProveedorAseoAdriana
      
        fields = ['proveedor',]

class PedidoProveedorFormPersonal(forms.ModelForm):
    class Meta:
        model = PedidoProveedorPersonalAdriana
      
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

class PedidoProveedorAdmin(admin.ModelAdmin):
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
        return forms.models.modelformset_factory(PedidoProveedorAdriana,
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

class PedidoProveedorAdminAseo(admin.ModelAdmin):
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
        return forms.models.modelformset_factory(PedidoProveedorAseoAdriana,
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

class PedidoProveedorAdminPersonal(admin.ModelAdmin):
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
        return forms.models.modelformset_factory(PedidoProveedorPersonalAdriana,
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
    model = DetalleDevolucionPedidoProveedorAdriana
    extra = 1
    min_num = 1
    show_change_link = False

class DetalleDevolucionPedidoProveedorInlineAseo(admin.TabularInline):
    model = DetalleDevolucionPedidoProveedorAseoAdriana
    extra = 1
    min_num = 1
    show_change_link = False

class DetalleDevolucionPedidoProveedorInlinePersonal(admin.TabularInline):
    model = DetalleDevolucionPedidoProveedorPersonalAdriana
    extra = 1
    min_num = 1
    show_change_link = False


class DevolucionPedidoProveedorAdmin(admin.ModelAdmin):
    fields = ['proveedor', 'detalle']
    list_filter = ['fecha_devolucion']
    search_fields = ['proveedor__nombre']
    list_display = ['id','proveedor', 'fecha_devolucion', 'detalle']
    inlines = [DetalleDevolucionPedidoProveedorInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            if obj.cantidad_devuelta is None:
                obj.cantidad_devuelta = 0
            producto = obj.producto
            producto.stock += obj.cantidad_devuelta
            producto.save()
            obj.delete()
        for instance in instances:
            if instance.cantidad_devuelta is None:
                instance.cantidad_devuelta = 0
            producto = instance.producto
            producto.stock -= instance.cantidad_devuelta
            producto.save()
            instance.save()
        formset.save_m2m()

class DevolucionPedidoProveedorAdminAseo(admin.ModelAdmin):
    fields = ['proveedor', 'detalle']
    list_filter = ['fecha_devolucion']
    search_fields = ['proveedor__nombre']
    list_display = ['id','proveedor', 'fecha_devolucion', 'detalle']
    inlines = [DetalleDevolucionPedidoProveedorInlineAseo]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            if obj.cantidad_devuelta is None:
                obj.cantidad_devuelta = 0
            producto = obj.producto
            producto.stock += obj.cantidad_devuelta
            producto.save()
            obj.delete()
        for instance in instances:
            if instance.cantidad_devuelta is None:
                instance.cantidad_devuelta = 0
            producto = instance.producto
            producto.stock -= instance.cantidad_devuelta
            producto.save()
            instance.save()
        formset.save_m2m()

class DevolucionPedidoProveedorAdminPersonal(admin.ModelAdmin):
    fields = ['proveedor', 'detalle']
    list_filter = ['fecha_devolucion']
    search_fields = ['proveedor__nombre']
    list_display = ['id','proveedor', 'fecha_devolucion', 'detalle']
    inlines = [DetalleDevolucionPedidoProveedorInlinePersonal]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            if obj.cantidad_devuelta  is None:
                obj.cantidad_devuelta  = 0
            producto = obj.producto
            producto.stock += obj.cantidad_devuelta 
            producto.save()
            obj.delete()
        for instance in instances:
            if instance.cantidad_devuelta  is None:
                instance.cantidad_devuelta  = 0
            producto = instance.producto
            producto.stock -= instance.cantidad_devuelta
            producto.save()
            instance.save()
        formset.save_m2m()


#SALIDAS_____________________________________________________________________
class DetalleSalidaDotaciónPersonalInline(admin.TabularInline):
    model =  DetalleSalidaDotaciónPersonalAdriana
    extra = 1
    min_num = 1
    show_change_link = False
##ADMIN
class SalidaDotaciónPersonalAdmin(admin.ModelAdmin):
    fields = ['solicitado_por','unidad','fecha']
    list_filter = ['fecha','unidad']
    search_fields = ['solicitado_por','unidad']
    list_display = ['id','solicitado_por', 'unidad','fecha']
    inlines = [DetalleSalidaDotaciónPersonalInline]
    actions = ['generar_pdf','generar_pdf_2']

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
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
            producto.stock -= instance.cantidad
            producto.save()
            instance.save()
        formset.save_m2m()

            
    def generar_pdf(self, request, queryset):
     id = queryset[0].id
     pedido_id = SalidaDotacionPersonalFORMAdriana.encryptId(id)
     url = reverse('report:exportVillaAdriana', kwargs={'pedido_id': pedido_id})
     return HttpResponseRedirect(url)

    generar_pdf.short_description = "Generar documento 'Registro de salidas para solicitud y entrega de dotación personal'"


    def generar_pdf_2(self, request, queryset):
     id = queryset[0].id
     pedido_id = SalidaDotacionPersonalFORMAdriana.encryptId(id)
     url = reverse('report:exportEntregaVillaAdriana', kwargs={'pedido_id': pedido_id})
     return HttpResponseRedirect(url)

    generar_pdf_2.short_description = "Generar documento 'solicitud y entrega de insumos'"

    #@admin.action(description='Generate PDF file')
    #def generatePDF(modeladmin, request, queryset):
     #   url ='templates/admin/person/?pks=' + ','.join(str([q.pk for q in queryset]))
       
    #actions = [generatePDF]
    
 
     

admin.site.register(pacienteVillaAdriana, PacienteAdmin)
admin.site.register(ElementoVillaAdriana,ElementoAdmin)
admin.site.register(ElementoVillaAdrianaAseo,ElementoAdminAseo)
admin.site.register(ElementoVillaAdrianaPersonal,ElementoAdminPersonal)
admin.site.register(PedidoProveedorAdriana, PedidoProveedorAdmin)
admin.site.register(PedidoProveedorAseoAdriana, PedidoProveedorAdminAseo)
admin.site.register(PedidoProveedorPersonalAdriana, PedidoProveedorAdminPersonal)
admin.site.register(DevolucionPedidoProveedorAdriana, DevolucionPedidoProveedorAdmin)
admin.site.register(DevolucionPedidoProveedorAseoAdriana, DevolucionPedidoProveedorAdminAseo)
admin.site.register(DevolucionPedidoProveedorPersonalAdriana, DevolucionPedidoProveedorAdminPersonal)
admin.site.register(SalidaDotacionPersonalFORMAdriana,SalidaDotaciónPersonalAdmin)