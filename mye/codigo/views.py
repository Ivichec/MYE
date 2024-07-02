from django.shortcuts import render
#from codigo.models import AltaEmp

def index(request):
    return render(request, "inicial/inicio.html")

def Ir_a_login(request):
    return render(request, "inicial/login.html")

def Ir_a_que_es_mye(request):
    # pendiente desarrollar función que llame al video de presentación