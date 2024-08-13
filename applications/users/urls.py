from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'user_app'


urlpatterns = [
    path('registro/', views.RegistrarUsuario.as_view(), name='registro'),
    path('lista-usuarios-generales/',views.ListaUsuariosGeneral.as_view(),name='lista_usuarios_general'),
    path('eliminar-usuarios/<int:pk>/',views.EliminarUsuarios.as_view(),name='eliminar_usuarios'),
    path('editar-usuarios/<int:pk>/',views.EditarUsuario.as_view(),name='editar_usuarios'),
    path('solicitud/<int:user_id>/', views.SolicitudCheck.as_view(), name='solicitud'),
    path('clientes/', views.ClientesAll.as_view(), name='clientes'),
    path('change_password/', views.change_password, name='change_password'),
   

    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
