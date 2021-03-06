from django.urls import path
from . import views

urlpatterns = [
    path("bienvenido", views.bienvenido, name="bienvenido"),
    path("bienvenido_premium", views.bienvenido_premium, name="bienvenido_premium"),
    path("nuevo", views.nuevo_usuario, name="nuevo_usuario"),
    path("login", views.iniciar_sesion, name="iniciar_sesion"),
    path("logout", views.cerrar_sesion, name="cerrar_sesion"),
]
