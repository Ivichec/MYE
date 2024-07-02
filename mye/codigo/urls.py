from django.urls import path

from codigo import (views)

urlpatterns = [
    path('inicio', views.index, name='index'),
    path('a_Login', views.Ir_a_login, name='iralogin'),
    path('a_que_es_mye', views.Ir_a_que_es_mye, name='iraqueesmye'),
    path('BotonUser', views.CompruebaPass, name='comprueba'),
    path('NuevoUser', views.CrearUsuario, name='NuevoUser'),
]