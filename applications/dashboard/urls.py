from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'dashboard_app'

urlpatterns = [
    path("",views.DashboardView.as_view(), name="index"),
    
    
    ##videos,audios,pdf##
    path('upload/', views.upload_video, name='upload_video'),
    path('catalog/', views.video_catalog, name='video_catalog'),
    path('audio/', views.audio_list, name='audio_list'),
    path('audio/add/', views.add_audio, name='add_audio'),
    path('pdfs/', views.pdf_list, name='pdf_list'),
    path('upload-pdf/', views.upload_pdf, name='upload_pdf'),
    ##videos,audios,pdf##
    
    #path('dashboard/get_nombre_producto/<int:prestamo_id>/', views.GetNombreProductoView.as_view(), name='get_nombre_producto'),
    #path('index/info-prestamo/', views.obtener_informacion_prestamo, name='info_prestamo'),
    #path('dashboard/obtener_detalles_prestamo/', views.ObtenerDetallesPrestamoView.as_view(), name='obtener_detalles_prestamo'),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
