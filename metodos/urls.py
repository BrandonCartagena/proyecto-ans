from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('integrantes/', views.integrantes, name='integrantes'),
	path('info/', views.info, name='info'),
	path('unidad2/biseccion/', views.biseccion, name='biseccion'),
	path('unidad2/falsa_posicion/', views.falsa_posicion, name='falsa_posicion'),
	path('unidad2/secante/', views.secante, name='secante'),
	path('unidad2/newton_raphson', views.newton_raphson, name='newton_raphson'),
	path('unidad2/newton_raphson_modificado', views.newton_raphson_modificado, name='newton_raphson_modificado')
]