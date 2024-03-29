from django.shortcuts import render

from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.db.models import Sum
from django.db.models import F,FloatField

from report.utils import convert_to_64
from report.report import report
from .models import DetalleSalidaDotaciónPersonalAdriana,SalidaDotacionPersonalFORMAdriana

class Index(TemplateView):
    template_name = "index.html"

def exportUsersPDFF(request,**kwargs):
    """Example of ExportPDF"""
    
    encrypted_id = kwargs['pedido_id']
    pedido_id = SalidaDotacionPersonalFORMAdriana.decryptId(encrypted_id)
    solicitud= SalidaDotacionPersonalFORMAdriana.objects.get(pk=pedido_id)
    users = DetalleSalidaDotaciónPersonalAdriana.objects.filter(salida_dotacion_personal=solicitud).order_by('usuario')
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

def exportEntregaPDFF(request,**kwargs):
    """Example of ExportPDF"""
    
    
    encrypted_id = kwargs['pedido_id']
    pedido_id = SalidaDotacionPersonalFORMAdriana.decryptId(encrypted_id)
    solicitud= SalidaDotacionPersonalFORMAdriana.objects.get(pk=pedido_id)
    entrega = DetalleSalidaDotaciónPersonalAdriana.objects.filter(salida_dotacion_personal=solicitud).values(productoo=F('producto__nombreElemento'),tallaa=F('producto__talla')).order_by('cantidad').annotate(cantidad=Sum('cantidad'))
    kwargs['solicitud'] = solicitud
    kwargs['entrega'] = entrega
   
    users_list = []
    for user in entrega:
        users_list.append({
            'cantidad': user['cantidad'],
            'producto': user['productoo'],
            'talla': user['tallaa']
            
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
    