from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail

from .models import Usuarios 
from .forms import UsuariosForm, InfoForm
from django.views.generic import ListView, TemplateView

from django.template import Template, Context


# Create your views here.
def inicio(request): 
	if request.user.is_authenticated:
		titulo = "Bienvenid@! %s" %(request.user) 

	form = UsuariosForm(request.POST or None)

	context = {"el_form": form,}   
	if form.is_valid():
		instance = form.save(commit=False)
		if not instance.nombre:
			instance.nombre = "Usuario sin nombre"
		instance.save()
		print (instance)
		
	return render(request,"inicio.html", context)

def category(request):
    queryset = Usuarios.objects.all()
    context = {'queryset': queryset,}
    return render(request,'info.html', context)
