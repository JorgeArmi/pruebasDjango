from django.db import models

# Create your models here.

class Data(models.Model):

	RUTA_UNO = ["WEB INF"]
	RUTA_DOS = ["LIB"]
	jar = models.CharField(max_length=100, blank=False, null= False, verbose_name="Jar")
	first_route = models.CharField(max_length=100, blank=False, null= False, verbose_name="RUTA 1",choices=RUTA_UNO)
	second_route = models.CharField(max_length=100, blank=True, null= True, verbose_name="RUTA 2", choices=RUTA_DOS)
	timestamp = models.DateField()

	def get_default_routes(self):
		return self.first_route + "" + self.second_route

	def __str__(self):
		return self.jar

class Uuaa(models.Model):

	UNIDADES_APILCATIVAS = ["EBCF","EYCX","EYPH","KCMX","KYFJ","KYFX","KYNO","KYTA","ERGS","EYOZ","ETNC","KYFB","KYGU","KYHD","KYNF","KYOP","KYOS","KYNB"]
	uuaa = models.MultipleChoiceField(max_length=10, blank=False, null=False, verbose_name="UUAA", choices=UNIDADES_APLICATIVAS)
	tecnologia = models.CharField(max_length=50, blank=True, null=False)
	data = models.ManyToManyFields(Data)
	data = models.ForeignKey(Data, on_delete = models.CASCADE)

	ear = models.CharField(max_length=100, blank=False, null= False)
	war = models.CharField(max_length=100, blank=False, null= False)

	def get_full_route(self):
		return self.ear + "" + self.war

	def __str__(self):
		return self.uuaa