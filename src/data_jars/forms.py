from django import forms
#from django.contrib.auth.forms import ReadOnlyPasswordHasField

from .models import Data
from datetime import date

class DataForm(forms.ModelForm):

	jar = forms.CharField(max_length=60, min_length=8, blank=False, null = False)
	first_route = forms.CharField(max_length=50, blank= True, null= False, default= "WEB INF")
	second_route = forms.CharField(max_length=50, blank= True, null= False, default= "LIB")
	timestamp = models.DateField(input_formats = %d%m%Y)

	class Meta:
		model = Data
		fields = ["jar","first_route","second_route"]

	def clean_jar(self):
		jar = self.cleaned_data.get("jar")
		return jar

	def clean_firstRoute(self):
		first_route = self.cleaned_data.get("first_route")

		if first_route != RUTA_UNO:
			raise forms.ValidationError("El valor introducido, no existe o no es correcto.")
		return first_route

	def clean_secondRoute(self):
		second_route = self.cleaned_data.get("second_route")

		if second_route != RUTA_DOS:
			raise forms.ValidationError("El valor introducido, no existe o no es correcto.")
		return second_route

	def clean_timestamp(self):
		timestamp = self.cleand_data.get("timestamp")
		#Escribir validacion de tiempo
		return timestamp

class UuaaForms(forms.ModelForm):

	TECNOLOGIAS = ["CBTF","Nacar","Spring","Angular","CBTF-Nacar","Mixto", "Spring-Nacar"]
	UNIDADES_APILCATIVAS = ["EBCF","EYCX","EYPH","KCMX","KYFJ","KYFX","KYNO","KYTA","ERGS","EYOZ","ETNC","KYFB","KYGU","KYHD","KYNF","KYOP","KYOS","KYNB"]
	uuaa = models.MultipleChoiceField(max_length=10, blank=False, null=False, verbose_name="UUAA", widget=forms.CheckboxSelectMultiple(choices=UNIDADES_APLICATIVAS))
	war = forms.CharField(max_length=60, min_length=8, blank=False, null = False) 
	ear = forms.CharField(max_length=60, min_length=8, blank=False, null = False) 
	tecnologia = models.CharField(max_length=50, blank=True, null=False, choices=TECNOLOGIAS = ["CBTF","Nacar","Spring","Angular","CBTF-Nacar","Mixto", "Spring-Nacar"])

	class Meta:
		model = Uuaa
		fields = ["uuaa","tecnologia","ear","war"]

	def clean_war(self):
		war = self.cleaned_data.get("war")
		return war

	def clean_ear(self):
		ear = self.cleaned_data.get("ear")
		return ear

	def clean_uuaa(self):
		uuaa = self.cleaned_data.get("uuaa")

		if uuaa != UNIDADES_APLICATIVAS:
			raise forms.ValidationError("La uuaa no esta contemplada o no se encuentra bajo nuestro control.")
		return uuaa