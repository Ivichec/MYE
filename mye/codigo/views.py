from django.shortcuts import render
from codigo.models import Diccionario

def index(request):
    return render(request, "inicial/inicio.html")


def Ir_a_login(request):
    return render(request, "inicial/login.html")


def CrearUsuario(request):
    emple = Diccionario()
    condicional = emple.devolverRoles()
    print("asdlkjfhyglaksjfhgaljñsfhglñasjfhglñasfhglñjsakfhglñasfjg")

    datosRoles = {
        'datosRoles': condicional,
    }
    print(datosRoles)
    return render(request, "inicial/registrar.html", datosRoles)


def darAlta(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    email = request.POST['email']
    password = request.POST['password']
    rol = request.POST['rol']

    return render(request, "inicial/inicio.html")


def formularioDiccionario(request):
    return render(request, "inicial/formularioDic.html")


def formularioDiccionarioPost(request):
    datos = request.POST.getlist('campo[]')
    print(datos)
    #for i in range(len(datos)):
    #llamar al procedimiento para metar datos a un diccionario
    return render(request, "inicial/Diccionarios.html")
