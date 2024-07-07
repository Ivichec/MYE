from django.shortcuts import render, redirect
from deep_translator import GoogleTranslator
from datetime import datetime
from codigo.models import Usuario

def Ir_a_que_es_mye(request):
    return render(request, "inicial/queesmye.html")
def index(request):
    cerrarSesion(request)
    return render(request, "inicial/inicio.html")

def Ir_a_login(request):
    print("Voy a login:", get_session_view(request))
    if get_session_view(request) != 'Guest':
        print("Soy alguien:", get_session_view(request))
        return render(request, "inicial/menuini.html")
    else:
        contexto = {
            'errorlogeo': False
        }
        print("no soy nadie:", get_session_view(request), contexto)
        return render(request, "inicial/login.html", contexto)

def menuIni(request):
    return render(request, "inicial/menuini.html")

def CompruebaPass(request):
    mail = request.POST['txtemail']
    passw = request.POST['txtcontrasena']
    mira = Usuario()
    cursor = mira.devolverpass(mail)
    if cursor.getvalue() == passw:
        cursor2 = mira.devolverId(mail)
        print("Es el usuario:", cursor2)
        set_session_view(request, cursor2)
        return redirect('menuIni')
    else:
        contexto = {
            'errorlogeo': True
        }
        return render(request, "inicial/login.html", contexto)

def Diccionarios(request):
    id = get_session_view(request)
    muestra = Usuario()
    cursor = muestra.TraeDiccionarios(id)
    contexto = {
        'listado_diccionarios': cursor
    }
    return render(request, "inicial/Diccionarios.html", contexto)

def Tests(request):
    user_id = get_session_view(request)
    if user_id == 'Guest':
        return render(request, "inicial/inicio.html")
    usuario = Usuario()
    tests_y_resultados = usuario.obtenerTestsYResultados(user_id)
    contexto = {
        'tests_y_resultados': tests_y_resultados
    }
    return render(request, "inicial/Tests.html",contexto)

def crearTests(request):
    id = get_session_view(request)
    muestra = Usuario()
    palabras = muestra.obtenerPalabrasAleatorias(10)  # Obtener 10 palabras aleatorias
    contexto = {
        'palabras': palabras
    }
    return render(request, "inicial/crearTests.html",contexto)

def enviarTest(request):
    if request.method == 'POST':
        palabras_correctas = 0
        total_palabras = 10
        id = get_session_view(request)
        emple = Usuario()
        print(datetime.now())
        idTests = emple.altaTests(id, datetime.now())
        print(idTests)
        for i in range(1, total_palabras + 1):
            respuesta_usuario = request.POST.get(f'traduccion_{i}')
            respuesta_correcta = request.POST.get(f'palabra_id_{i}')
            id_trad = request.POST.get(f'trad_id_{i}')
            print(id_trad)

            if respuesta_usuario and respuesta_correcta:
                resultado = 1 if respuesta_usuario.strip().lower() == respuesta_correcta.strip().lower() else 0
                emple.insertarResultado(idTests, id_trad, resultado)
                if resultado == 1:
                    palabras_correctas += 1

        nota = (palabras_correctas / total_palabras) * 100
        print(nota)
        contexto = {
            'nota': nota,
            'palabras_correctas': palabras_correctas,
            'total_palabras': total_palabras
        }

        return render(request, "inicial/resultadosTest.html", contexto)


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
        print("flñkjsadfgljashbflñgjasñlf")
        print(datos)
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
    idDic = request.GET.get('idDic')
    print(idDic)
    mira = Usuario()
    cursor = mira.listaDiccionario(idDic)
    print(cursor)
    contexto = {
        'listado_palabras': cursor
    }
    return render(request, "inicial/verDiccionario.html", contexto)


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
