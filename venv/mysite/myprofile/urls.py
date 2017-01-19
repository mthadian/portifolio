from django.conf.urls import url, patterns, include
from . import views

#app_name='contactme'

urlpatterns = [
	
	
	url(r'^$', views.index, name='index'),
	url(r'^$', views.sendMessage, name='contactme'),

	#url(r'^$', views.indexEd, name='indexEd'),
]
