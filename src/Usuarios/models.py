
from django.db import models

# Create your models here.

class Usuarios(models.Model):
	nombre = models.CharField(max_length=25, blank=False, null=False) 
	contraseña = models.CharField(max_length=12, blank=False, null=False)
	primer_apellido = models.CharField(max_length=30, blank=True, null=True, verbose_name='primer apellido')
	email = models.EmailField(max_length=40, blank=False, null=False, unique=True)
	timestamp = models.DateField(auto_now_add=True, auto_now=False)

	#Funcíon para recuperar el nombre completo de un usuario
	def get_full_name(self):
		return self.nombre + '' + self.primer_apellido

	def short_name(self):
		return self.nombre

	#Método que devuelve los campos expresados para representar dicha clase del modelo
	def __str__(self):
		return '%s %s' % (self.nombre, self.email)

#Relación de los datos del perfil adicionales con el usuario registrado.
class Perfil(models.Model):
	segundo_apellido = models.CharField(max_length=30, blank=True, null=True, verbose_name='segundo apellido')
	direccion = models.CharField(max_length=60, blank=True, null=True)
	telefono = models.CharField(max_length=9, blank=True, null=True)
	proyecto = models.CharField(max_length=60, blank=True, null=True)
	usuarios = models.ForeignKey(Usuarios, on_delete = models.CASCADE)

	def __str__(self):
		return self.telefono