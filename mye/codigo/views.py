from django.shortcuts import render


from codigo.models import Usuario

def index(request):
    return render(request, "inicial/inicio.html")
def menuIni(request):
    return render(request, "inicial/menuini.html")
def Diccionarios(request):
    return render(request, "inicial/Diccionarios.html")
def Tests(request):
    return render(request, "inicial/Tests.html")

def crearTests(request):
    return render(request, "inicial/crearTests.html")

def enviarTest(request):
    #cojer todos los post del formulario de crearTests.html y comprobarlo con la api para ver si lo ha hecho bien o no y devolverle
    #un diccionario a resultadosTests.html con la nota que ha sacado
    #despues enviar el resultado a la base de datos
    return render(request, "inicial/resultadosTest.html")

def Ir_a_login(request):
    #hay que cambiar el if este que esta mal para verificar la cookie de sesion
    if get_session_view(request) != 'Guest':
        print("holasdafadfad")
        print(get_session_view(request))
        print(str(get_session_view(request)) == 'Guest')
        contexto = {
            'errorlogeo': True
        }
        return render(request, "inicial/login.html", contexto)
    else:
        return render(request, "inicial/menuini.html")


def CrearUsuario(request):
    emple = Usuario()
    condicional = emple.devolverRoles()
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
    #Llamar al procedimiento para dar de alta
    usr = Usuario()
    usr.insertarUsuario(nombre, apellido, email, password, rol)
    return render(request, "inicial/inicio.html")


def formularioDiccionario(request):
    return render(request, "inicial/formularioDic.html")


def formularioDiccionarioPost(request):
    #Compruebo que al llamar a este metodo estoy logeado con el if
    if get_session_view(request) != 'Guest':
        datos = request.POST.getlist('campo[]')
        print(datos)
        #for i in range(len(datos)):
        #llamar al procedimiento para metar datos a un diccionario
        return render(request, "inicial/Diccionarios.html")
    else:
        return render(request, "inicial/inicio.html")


def CompruebaPass(request):
    mail = request.POST['txtemail']
    passw = request.POST['txtcontrasena']
    mira = Usuario()
    cursor = mira.devolverpass(mail)
    if cursor.getvalue() == passw:
        cursor2 = mira.devolverId(mail)
        id = cursor2.getvalue()
        #creo una cookie para saber si el usuario esta logeado
        set_session_view(request,id)
        return render(request, "inicial/menuini.html")
    else:
        print(cursor)
        print(passw)
        contexto = {
            'errorlogeo': False
        }
        return render(request, "inicial/login.html", contexto)


def cerrarSesion(request):
    delete_session_view(request)
    return render(request, "inicial/inicio.html")


def prueba(request):
    set_session_view(request)
    return render(request, "inicial/menuini.html")

def muestraDic(request):
    #aqui hay que traer la id con la función que ha hecho Iván


    muestra = Usuario()
    cursor=muestra.TraeDiccionarios(id)
    contexto = {
        'listado_diccionarios': cursor
    }
    return render(request, "inicial/Diccionarios.html", contexto)
#con esto hacemos el for dentro del html Diccionarios

#Funciones de sesiones

#Funcion para crear una cookie con el id de la base de datos de el usuaio logeado
def set_session_view(request):

    request.session['id'] = 'Iván'  #Llamar a la base de datos con un metodo para que te devuelva el id de usuario, cambiar el 'Iván' por eso
    get_session_view(request)
    return render(request, 'inicial/menuini.html')


#Funcion para ver el id de usuario del usuario logeado
def get_session_view(request):
    username = request.session.get('id', 'Guest')
    #Si haces print te devuelve el id de usuario
    print(username)
    return render(request, 'inicial/inicio.html', {'username': username})


#Funcion para borrar la cookie(cuando hace el log out)
#Con esta funcion el id que le hemos dado cuando se logeado se borra y la cookie se queda el Guest
def delete_session_view(request):
    try:
        del request.session['id']
        get_session_view(request)
    except KeyError:
        pass
    return render(request, 'inicial/inicio.html')
