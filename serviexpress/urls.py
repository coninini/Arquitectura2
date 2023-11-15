from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('servicios', views.servicios, name='servicios'),
    path('reserva', views.reserva, name='reserva'),
    path('cuenta', views.cuenta, name='cuenta'),
    path('contacto', views.contacto, name='contacto'),
    path('tipoUsuario', views.tipoUsuario, name='tipoUsuario'),
    path('registro_cli', views.registro_cli, name='registro_cli'),
    path('servicio1',views.servicio1, name='servicio1'),
    path('servicio2',views.servicio2, name='servicio2'),
    path('servicio3',views.servicio3, name='servicio3'),
    path('servicio4',views.servicio4, name='servicio4'),
    path('servicio5',views.servicio5, name='servicio5'),
    path('servicio6',views.servicio6, name='servicio6'),
    path('registro_pro',views.registro_pro, name='registro_pro'),
    path('registro_emp',views.registro_emp, name='registro_emp'),
    path('confirmacion_res',views.confirmacion_res, name='confirmacion_res'),
]
