from django.shortcuts import render
from codigo.models import Diccionario,MiraPass

def index(request):
    return render(request, "inicial/inicio.html")


def Ir_a_login(request):
    contexto = {
        'errorlogeo': True
    }
    return render(request, "inicial/login.html",contexto)


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

def CompruebaPass(request):
    mail = request.POST['txtemail']
    passw = request.POST['txtcontrasena']
    mira = MiraPass()
    cursor = mira.devolverpass(mail)
    if cursor.getvalue() == passw:
        print(cursor)
        print(passw)
        return render(request, "inicial/menuini.html")

    else:
        print(cursor)
        print(passw)
        contexto = {
            'errorlogeo': False
        }
        return render(request, "inicial/login.html",contexto)
