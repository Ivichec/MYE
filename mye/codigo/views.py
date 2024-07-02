from django.shortcuts import render
from codigo.models import MiraPass

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

