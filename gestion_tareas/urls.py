from . import views
from django.urls import path

app_name='gestion_tareas'

urlpatterns=[
  path('ingresar',views.ingresar, name='ingresar'),
  path('dashboard',views.dashboard, name='dashboard'),
  path('detallarTareas', views.detallarTareas, name='detallarTareas'),
  path('editarTareas',views.editarTareas,name='editarTareas'),
  path('crearTareas',views.crearTareas, name='crearTareas'),
]