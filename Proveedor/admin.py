from django.contrib import admin
from jmespath import search
from import_export import resources
from import_export.admin import ImportExportModelAdmin 
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from inventarioApp import app_messages
from django import forms
from functools import partial


from Proveedor.models import (
    Proveedor
)

# Register your models here.


# Proveedor
class ProveedorAdmin(admin.ModelAdmin):
    fields = ('nombreProveedor', 'Nit', 'NumeroContacto', 'Correo',)
    list_display = ('id','nombreProveedor', 'Nit', 'NumeroContacto', 'Correo',)
    search_fields = ('nombreProveedor', 'Nit', 'id')




admin.site.register(Proveedor, ProveedorAdmin)
