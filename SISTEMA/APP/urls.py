from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('cumple',views.agregarCumple,name='agregarCumple'),
    path('tarea',views.agregarTarea,name='agregarTarea'),
    path('verTareas',views.verTareas,name='verTareas'),
    path('verCumples',views.verCumples,name='verCumples'),
    path('login',views.LogIn,name='login'),
    path('cumpleMes/<int:mes>/', views.cumpleMes, name="cumpleMes"),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
