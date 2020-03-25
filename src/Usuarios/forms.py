from django import forms
#from django.contrib.auth.forms import ReadOnlyPasswordHasField

from .models import Usuarios

class UsuariosForm(forms.ModelForm):

	contraseña = forms.CharField(max_length=12, min_length=8, widget=forms.PasswordInput, help_text="La contraseña de be contener entre 8 y 12 caracteres.")
	contraseña1 = forms.CharField(max_length=12, min_length=8, widget=forms.PasswordInput, label='Confirmación Contraseña',
	 help_text="Introduce la misma contraseña, por favor.")

	class Meta:
		model = Usuarios
		fields = ["nombre","email","contraseña"]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		#qs = Usuarios.objects.filter(email = email)  
		email_base, proveedor = email.split("@")
		dominio, extension = proveedor.split(".")

		#if qs.exists()
			#raise forms.ValidationError("Esta cuenta de email ya existe, por favor introduce otra.")
		#return email

		if extension != "com" and proveedor != "gmail": #and qs.exists(): 
			raise forms.ValidationError("Introduce un email con la extensión gmail")
		return email

	def clean_contraseña(self):
		contraseña = self.cleaned_data.get("contraseña")
		contraseña1 = self.cleaned_data.get("contraseña1")

		if contraseña != contraseña1:
			raise forms.ValidationError("Las contraseñas no coinciden, por favor comprueba que ambas son iguales.")
		return contraseña

class InfoForm(forms.ModelForm):

	nombre = forms.CharField()
	contraseña = forms.CharField()
	primer_apellido = forms.CharField()
	email = forms.EmailField()
	timestamp = forms.DateField()
