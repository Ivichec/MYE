from django.shortcuts import render
#from codigo.models import AltaEmp

def index(request):
    return render(request, "inicial/inicio.html")

def Ir_a_login(request):
    return render(request, "inicial/login.html")

def CrearUsuario(request):
    return render(request, "inicial/registrar.html")

def Ir_a_que_es_mye(request):
    # pendiente desarrollar función que llame al video de presentación
    pass

def CompruebaPass(request):
    mail = request.POST['txtemail']
    emple = Empleado()
    cursor = emple.devolverdato(mail)
    contexto = {
        'listado_empleados': cursor
    }
    return render(request, "deportes/Empleados.html", contexto)