from django.shortcuts import render
from codigo.models import Datos
def index(request):
    return render(request, "hospitales/Inicio.html")