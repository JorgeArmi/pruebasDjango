from django.contrib import admin

from .models import Uuaa, Data
# Register your models here.

class AdminData(admin.ModelAdmin):

	list_display = ["id","jar","first_route","second_route", "timestamp"]
	list_editable = ["first_route","second_route"]
	list_filter = ["id","jar","first_route","second_route"]
	search_fields = ["id","jar"]
	ordering = ["id","jar"]

#class AdminUuaa(admin.ModelAdmin):

	#list_display = ["id","uuaa","tecnologia","ear", "war"]
	#list_editable = ["tecnologia"]
	#list_filter = ["id","uuaa","ear","war"]
	#search_fields = ["id","uuaa"]
	#ordering = ["id","uuaa"]

admin.site.register(Data, AdminData)
admin.site.register(Uuaa) #,AdminUuaa)