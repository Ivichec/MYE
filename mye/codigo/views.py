from django.shortcuts import render, redirect
from deep_translator import GoogleTranslator
from codigo.models import Usuario

def index(request):
    return render(request, "inicial/inicio.html")

def menuIni(request):
    return render(request, "inicial/menuini.html")

def Diccionarios(request):
    id = get_session_view(request)
    muestra = Usuario()
    cursor = muestra.TraeDiccionarios(id)
    contexto = {
        'listado_diccionarios': cursor
    }
    return render(request, "inicial/Diccionarios.html", contexto)

def Tests(request):
    return render(request, "inicial/Tests.html")

def crearTests(request):
    return render(request, "inicial/crearTests.html")

def enviarTest(request):
    return render(request, "inicial/resultadosTest.html")

def Ir_a_login(request):
    if get_session_view(request) != 'Guest':
        return render(request, "inicial/menuini.html")
    else:
        contexto = {
            'errorlogeo': False
        }
        return render(request, "inicial/login.html", contexto)

def CrearUsuario(request):
    emple = Usuario()
    condicional = emple.devolverRoles()
    datosRoles = {
        'datosRoles': condicional,
    }
    return render(request, "inicial/registrar.html", datosRoles)

def darAlta(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    email = request.POST['email']
    password = request.POST['password']
    rol = request.POST['rol']
    usr = Usuario()
    usr.insertarUsuario(nombre, apellido, email, password, rol)
    return redirect('index')

def formularioDiccionario(request):
    return render(request, "inicial/formularioDic.html")

def formularioDiccionarioPost(request):
    if get_session_view(request) != 'Guest':
        nombre = request.POST['nombre1']
        datos = request.POST.getlist('campo[]')
        mira = Usuario()
        cursor = mira.crearDic(int(get_session_view(request)), nombre)
        for i in datos:
            translated = GoogleTranslator(source='auto', target='en').translate(i)
            mira.insertarPalabra(cursor, i, 'es', translated, 'en')
        id = get_session_view(request)
        muestra = Usuario()
        cursor = muestra.TraeDiccionarios(id)
        contexto = {
            'listado_diccionarios': cursor,
        }
        return render(request, "inicial/Diccionarios.html", contexto)
    else:
        return redirect('index')

def verDiccionario(request):
    idDic = request.GET['idDic']
    mira = Usuario()
    cursor = mira.listaDiccionario(idDic)
    print(cursor)
    # Render the dictionary view with the cursor data (you might need to adjust this)
    contexto = {
        'listado_palabras': cursor
    }
    return render(request, "inicial/verDiccionario.html", contexto)

def CompruebaPass(request):
    mail = request.POST['txtemail']
    passw = request.POST['txtcontrasena']
    mira = Usuario()
    cursor = mira.devolverpass(mail)
    if cursor.getvalue() == passw:
        cursor2 = mira.devolverId(mail)
        set_session_view(request, cursor2)
        return redirect('menuIni')
    else:
        contexto = {
            'errorlogeo': True
        }
        return render(request, "inicial/login.html", contexto)

def cerrarSesion(request):
    delete_session_view(request)
    return redirect('index')

def prueba(request):
    set_session_view(request)
    return redirect('menuIni')

def muestraDic(request):
    id = get_session_view(request)
    muestra = Usuario()
    cursor = muestra.TraeDiccionarios(id)
    contexto = {
        'listado_diccionarios': cursor
    }
    return render(request, "inicial/Diccionarios.html", contexto)

def set_session_view(request, id):
    request.session['id'] = id
    return

def get_session_view(request):
    return request.session.get('id', 'Guest')

def delete_session_view(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return
