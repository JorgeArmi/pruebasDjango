from django.shortcuts import render

from .models import Data, Uuaa
from .forms import DataForm, UuaaForm
from django.views.generic import ListView, TemplateView
from django.template import Template, Context
# Create your views here.

#Views para visualización de los datos en el html
def datos(request):
	queryset = Data.objects.all().order_by("jar")
	context = {'queryset':queryset,}
	return render(request,"data.html", context)

def datos_asociados(request):
	qset = Uuaa.objects.all().order_by("uuaa")
	context = {'qset':qset,}
	return render(request, 'data.html', context)

#Views para los forms 
def data(request):
	form = DataForm(request.POST or None)
	context = {"el_form": form,}   
	if form.is_valid():
		instance = form.save(commit=False)
	return render(request,'info_jars.html', context)

def data_asociated(request):
	form = UuaaForm(request.POST or None)
	context = {"uuaa_form": form,}   
	if form.is_valid():
		instance = form.save(commit=False)
	return render(request,'info_jars.html', context)