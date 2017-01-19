from django.contrib import admin
from .models import Intro
from .models import WhatIDo
from .models import ImagesPortifolio
from .models import Clients
# Register your models here.

admin.site.register(Intro)
class whatAdmin(admin.ModelAdmin):
	list_display=("whyMe", "whatDo" , "mission")

admin.site.register(WhatIDo,whatAdmin)

class PortifolioAdmin(admin.ModelAdmin):
	list_display=("project","image","description")



admin.site.register(ImagesPortifolio,PortifolioAdmin)

class CLientsAdmin(admin.ModelAdmin):
	list_display=("No_Client","No_Projects","No_Exp","Ongoing")

admin.site.register(Clients,CLientsAdmin)