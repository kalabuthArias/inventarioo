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
    path('exportArcoIris/(?P<pedido_id>[-_:\w\d]+)',exportUsersPDF,name='exportArcoIris'),
    path('exportEntregaArcoIris/(?P<pedido_id>[-_:\w\d]+)',exportEntregaPDF,name='exportEntregaArcoIris'),
    path('exportVillaAdriana/(?P<pedido_id>[-_:\w\d]+)',exportUsersPDFF,name='exportVillaAdriana'),
    path('exportEntregaAdriana/(?P<pedido_id>[-_:\w\d]+)',exportEntregaPDFF,name='exportEntregaVillaAdriana'),
    path('exportVillaBlanca/(?P<pedido_id>[-_:\w\d]+)',exportUsersPDFFF,name='exportVillaBlanca'),
    path('exportEntregaBlanca/(?P<pedido_id>[-_:\w\d]+)',exportEntregaPDFFF,name='exportEntregaVillaBlanca'),
    path('exportVillaJimena/(?P<pedido_id>[-_:\w\d]+)',exportUsersPDFFFF,name='exportVillaJimena'),
    path('exportEntregaJimena/(?P<pedido_id>[-_:\w\d]+)',exportEntregaPDFFFF,name='exportEntregaVillaJimena')
    ]
        
    