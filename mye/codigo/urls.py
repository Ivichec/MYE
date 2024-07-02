from django.urls import path

from codigo import (views)

urlpatterns = [
    path('inicio', views.index, name='index'),
    path('a_Login', views.Ir_a_login, name='iralogin'),
   # path('a_que_es_mye', views.Ir_a_que_es_mye, name='iraqueesmye'),
    path('formularioDic', views.formularioDiccionario, name='iraformularioDic'),
    path('formularioDicPost', views.formularioDiccionarioPost, name='iraformularioDicPost'),
    path('NuevoUser', views.CrearUsuario, name='NuevoUser'),
    path('darAlta', views.darAlta, name='darAlta'),
    path('BotonUser', views.CompruebaPass, name='BotonUser'),
]