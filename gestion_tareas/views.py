
from django.urls import reverse
from django.shortcuts import render
from gestion_tareas.models import usuario
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
  return render(request,'gestion_tareas/dashboard.html')


def detallarTareas(request):
  pass


def editarTareas(request):
  pass


def crearTareas(request):
  pass

