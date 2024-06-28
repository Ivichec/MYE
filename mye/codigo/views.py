from django.shortcuts import render
from codigo.models import Datos
def index(request):
    return render(request, "hospitales/Inicio.html")
def index1(request):
    return render(request, "hospitales/Inicio.html")
def index2(request):
    return render(request, "hospitales/Inicio.html")