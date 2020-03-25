from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail

from .models import Usuarios 
from .forms import UsuariosForm, InfoForm
from django.views.generic import ListView, TemplateView

# Create your views here.
def inicio(request): 
	if request.user.is_authenticated:
		titulo = "Bienvenid@! %s" %(request.user) #"Bienvenido %s" %(request.user)

	form = UsuariosForm(request.POST or None)

	context = {
		#"titulo" : titulo,
		"el_form": form,
	}   
	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.nombre:
			instance.nombre = "Usuario sin nombre"
		instance.save()
		context = {
			"titulo" : "Gracias %(nombre)!" 
		}
		context = {
			"titulo" : "Gracias por registrate en nuestra aplicación."	 
		}

		print (instance)
		
	return render(request,"inicio.html", context)

def category(request):
    form = InfoForm(request.GET or None)

    context = {'object_list': usuarios_lista}
    return render(request,'info.html', context)


def info(ListView):
	template_name = "info.html"
	nombres = ["Pepe","Pablo","Santiago","David"]
	context_object_name = "nombres"

	return HttpResponse(nombres)

def prueba(ListView):
	template_name = "info.html"
	model = Usuarios()
	queryset = Usuarios.objects.all()
	context_object_name = "usuarios_lista"

	return HttpResponse(Usuarios)