
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('myprofile.urls')),
    url(r'^myedu/', include('myedu.urls')),
    url(r'^myskills/', include('myedu.urls')),
    url(r'^myexperience/', include('myedu.urls')),
    url(r'^contactme/', include('myprofile.urls')),
   

]

admin.site.site_header = 'Site Administrator: Django'
#https://www.fiverr.com/s2/371e98b8c9
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)