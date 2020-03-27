from django.contrib import admin

from .models import Usuarios , Perfil
#from .forms import UsuariosModelForm

# Register your models here.

class AdminUsuarios(admin.ModelAdmin):

	#Listado de campos que queremos que se vean en el administrador por defecto de django.
	list_display = ["id","nombre","primer_apellido","email","timestamp"]

	#Lista de campos que serán editables en el admin.
	list_editable = ["nombre","primer_apellido","email"]

	#Campos por los cuales se quiere poder filtrar
	list_filter = ["id","nombre", "email"]

	#Campos a traves de los que poder hacer una busqueda en el admin por defecto de django
	search_fields = ["id","nombre","email","timestamp"]

	#Orden en función del campo especificado en el administrador de nuestra BBDD.
	ordering = ["id"]

class AdminPerfil(admin.ModelAdmin):
	list_display = ["id","segundo_apellido","telefono", "usuario","proyecto", "direccion"]
	list_editable = ["segundo_apellido","telefono","proyecto", "direccion"]
	search_fields = ["id","segundo_apellido","telefono","proyecto"]
	list_filter = ["id","telefono", "proyecto"]

admin.site.register(Usuarios, AdminUsuarios) 
admin.site.register(Perfil, AdminPerfil)