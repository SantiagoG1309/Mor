from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('recuerdos/', views.recuerdos_lista, name='recuerdos_lista'),
    path('recuerdos/crear/', views.recuerdo_crear, name='recuerdo_crear'),
    path('recuerdos/eliminar/<int:pk>/', views.recuerdo_eliminar, name='recuerdo_eliminar'),
    path('mensajes/', views.mensajes_lista, name='mensajes_lista'),
    path('mensajes/crear/', views.mensaje_crear, name='mensaje_crear'),
    path('mensajes/eliminar/<int:pk>/', views.mensaje_eliminar, name='mensaje_eliminar'),
    path('fotos/', views.fotos_lista, name='fotos_lista'),
    path('fotos/crear/', views.foto_crear, name='foto_crear'),
    path('fotos/eliminar/<int:pk>/', views.foto_eliminar, name='foto_eliminar'),
    path('musica/', views.musica_lista, name='musica_lista'),
    path('musica/crear/', views.musica_crear, name='musica_crear'),
    path('musica/eliminar/<int:pk>/', views.musica_eliminar, name='musica_eliminar'),
    path('sorpresas/', views.sorpresas, name='sorpresas'),
    path('flores/', views.flores, name='flores'),
    path('toggle-dark-mode/', views.toggle_dark_mode, name='toggle_dark_mode'),
]