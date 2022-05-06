from django.urls import path
from .import views

urlpatterns = [

    path ('', views.inicio, name='inicio'),
   path ('nosotros', views.nosotros, name='nosotros' ),
   path('elementos', views.elementos, name='elementos'),
   path('elementos/crear', views.crear, name='crear'),
    path('elementos/editar', views.editar, name='editar'),
]