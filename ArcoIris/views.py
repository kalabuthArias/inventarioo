#VIEWS.PY 
from django.shortcuts import render

from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.db.models import Sum
from django.db.models import F,FloatField

from report.utils import convert_to_64
from report.report import report
from .models import DetalleSalidaDotaciónPersonal,SalidaDotacionPersonalFORM

class Index(TemplateView):
    template_name = "index.html"

def exportUsersPDF(request,**kwargs):
    """Example of ExportPDF"""
    
    encrypted_id = kwargs['pedido_id']
    pedido_id = SalidaDotacionPersonalFORM.decryptId(encrypted_id)
    solicitud= SalidaDotacionPersonalFORM.objects.get(pk=pedido_id)
    users = DetalleSalidaDotaciónPersonal.objects.filter(salida_dotacion_personal=solicitud).order_by('usuario')
    kwargs['users'] = users
    kwargs['solicitud'] = solicitud

    
    users_list = []
    for  users in users:
        users_list.append({
            'insumo': users.producto.nombreElemento,
            'cantidad': users.cantidad,
            'especificacion': users.especificacion,
            'talla': users.producto.talla,
            'PrimerNombre': users.usuario.PrimerNombre,
            'SegundoNombre': users.usuario.SegundoNombre,
            'PrimerApellido': users.usuario.PrimerApellido, 
            
        })

    soli_list=[{
      'solicitado': solicitud.solicitado_por,
      'unidad': solicitud.unidad,
      'fecha': solicitud.fecha}]
   

    data = {
        'users': users_list,
        'solicitud': soli_list
    
    }

    return report(request, 'users', data)

def exportEntregaPDF(request,**kwargs):
    """Example of ExportPDF"""
    
    
    encrypted_id = kwargs['pedido_id']
    pedido_id = SalidaDotacionPersonalFORM.decryptId(encrypted_id)
    solicitud= SalidaDotacionPersonalFORM.objects.get(pk=pedido_id)
    entrega = DetalleSalidaDotaciónPersonal.objects.filter(salida_dotacion_personal=solicitud).raw('SELECT id,producto_id, SUM(cantidad) AS cantidad FROM railway.arcoiris_detallesalidadotaciónpersonal  WHERE salida_dotacion_personal_id LIKE %s GROUP BY producto_id ORDER BY cantidad'%(pedido_id))
    kwargs['solicitud'] = solicitud
    kwargs['entrega'] = entrega
   
#    raw('SELECT id,producto_id, SUM(cantidad) AS cantidad FROM arcoiris_detallesalidadotaciónpersonal  WHERE salida_dotacion_personal_id LIKE %s GROUP BY producto_id ORDER BY cantidad'%(pedido_id))
    users_list = []
    for user in entrega:
        users_list.append({
            'cantidad': user.cantidad,
            'producto': user.producto.nombreElemento,
            'talla': user.producto.talla
            
        })

    soli_list=[{
      'solicitado': solicitud.solicitado_por,
      'unidad': solicitud.unidad,
      'fecha': solicitud.fecha}]
   

    data= {
        'entrega': users_list,
        'solicitud': soli_list
    
    }

    return report(request, 'entrega', data)
    