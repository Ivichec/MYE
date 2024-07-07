from django.urls import path

from codigo import views

urlpatterns = [
    path('', views.index, name='index'),
  # path('a_que_es_mye', views.Ir_a_que_es_mye, name='iraqueesmye'),
    path('a_Login', views.Ir_a_login, name='iralogin'),
    path('menuIni', views.menuIni, name='menuIni'),
    path('BotonUser', views.CompruebaPass, name='BotonUser'),
    path('NuevoUser', views.CrearUsuario, name='NuevoUser'),
    path('darAlta', views.darAlta, name='darAlta'),
    path('verDiccionario', views.verDiccionario, name='verDiccionario'),
    path('Diccionarios', views.Diccionarios, name='Diccionarios'),
    path('formularioDic', views.formularioDiccionario, name='iraformularioDic'),
    path('formularioDicPost', views.formularioDiccionarioPost, name='iraformularioDicPost'),
    path('Tests', views.Tests, name='Tests'),
    path('crearTests', views.crearTests, name='crearTests'),
    path('enviarTest', views.enviarTest, name='enviarTest'),
    path('cerrarSesion', views.cerrarSesion, name='cerrarSesion'),

    path('prueba', views.prueba, name='prueba'),
]