from urllib.parse import urlparse
from django.urls import path
from report.report import*
from django.urls import include, re_path as url
from ArcoIris.views import exportUsersPDF, exportEntregaPDF
from VillaAdriana.views import exportUsersPDFF, exportEntregaPDFF
from VillaBlanca.views import exportEntregaPDFFF,exportUsersPDFFF
from VillaJimena.views import exportEntregaPDFFFF,exportUsersPDFFFF

#URL
urlpatterns=[
    path('edit/<str:report_type>/', edit, name='report_edit'),
    path('run/',run, name='report_run'),
    path('save/<str:report_type>/',save,name='report_save'),
    path('exportArcoIris/<str:pedido_id>/)',exportUsersPDF,name='exportArcoIris'),
    path('exportEntregaArcoIris/<str:pedido_id>/)',exportEntregaPDF,name='exportEntregaArcoIris'),
    path('exportVillaAdriana/<str:pedido_id>/)',exportUsersPDFF,name='exportVillaAdriana'),
    path('exportEntregaAdriana/<str:pedido_id>/)',exportEntregaPDFF,name='exportEntregaVillaAdriana'),
    path('exportVillaBlanca/<str:pedido_id>/)',exportUsersPDFFF,name='exportVillaBlanca'),
    path('exportEntregaBlanca/<str:pedido_id>/)',exportEntregaPDFFF,name='exportEntregaVillaBlanca'),
    path('exportVillaJimena/<str:pedido_id>/)',exportUsersPDFFFF,name='exportVillaJimena'),
    path('exportEntregaJimena/<str:pedido_id>/)',exportEntregaPDFFFF,name='exportEntregaVillaJimena')
    ]
    