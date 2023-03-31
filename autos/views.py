from django.shortcuts import render
#importo los modelos para poder llamar los valores que tenga en la base de datos, le pongo .models pq el archivo esta en la misma carpeta
from .models import *

def clientes(request):
    context={
        "titulo":"Clientes",
        #en la clave clientes voy a llamar mi modelo y aplicar el all() para traerme todos los valores
        "clientes":Clientes.objects.all(),
        }
    return render(request,"clientes.html",context)

def autos(request):
    context={
        "titulo":"Autos",
        'autos':Autos.objects.all(),
        }
    return render(request,"autos.html",context)

def principal(request):
    context={
        "titulo":"vista principal"
        }
    return render(request,"principal.html",context)