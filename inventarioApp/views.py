from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
 return render(request,'paginas/index.html')

def inicioo(request):
 return render(request,'paginas/inicioo.html')

