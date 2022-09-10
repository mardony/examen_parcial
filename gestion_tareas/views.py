
from django.urls import reverse
from django.shortcuts import render
from gestion_tareas.models import usuario,tarea
from django.http import HttpResponseRedirect

# Create your views here.
def ingresar(request):
  if request.method=='POST':
      nombreUsuario = request.POST.get('nombreUsuario')
      passwordUsuario=request.POST.get('passwordUsuario')

      #Validación de información
      usuario_registrado = 0
      usuarios_totales = usuario.objects.all()

      #recorrido por usuarios totales
      for usuariox in usuarios_totales:
        if usuariox.nombre == nombreUsuario and usuariox.psw_usuario == passwordUsuario:
          usuario_registrado = 1


      #vista de dashboard
      if usuario_registrado == 1:
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
      else:
        return render(request,'gestion_tareas/ingresar.html',{
                'mensaje':'Los datos ingresados son incorrectos',
        })

      #Fin de validación

  return render (request,'gestion_tareas/ingresar.html')

def dashboard(request):
  tareas_totales = tarea.objects.all()


  #Filtrar tareas de cada trabajador
  lista_tareas=[]
  mi_tarea=tarea.objects.filter(usuario_responsable="2")
  for tareas in mi_tarea:
      lista_tareas.append(tareas)

  #fin de filtro de trabajadores
  return render(request,'gestion_tareas/dashboard.html',{
      'objTareas':lista_tareas,
  })


def detallarTareas(request):
  pass


def editarTareas(request):
  pass


def crearTareas(request):
  pass

