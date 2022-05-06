from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
 return render(request,'paginas/inicio.html')

def  nosotros(request):
     return render(request,'paginas/nosotros.html')

def elementos(request):
     return render(request,'elementos/index.html')

def crear(request):
    return render(request, 'elementos/crear.html')

def editar(request):
    return render(request, 'elementos/editar.html')