from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
	list_display=("Name" , "Email" , "Phone" , "Message")
	list_display_links=("Name" , "Email" , "Phone")
	#list_filter=("Name" , "Email" , "Phone")
	search_fields=("Name" , "Email" , "Phone")


admin.site.register(Contact,ContactAdmin)