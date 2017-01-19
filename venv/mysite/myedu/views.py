from django.http import HttpResponse
from django.template import loader
from .models import Education



def index(request):
	template=loader.get_template('myprofile/home.html')
	context={
		'All_Education' : Education.objects.all(),
	}
	return HttpResponse(template.render(context, request))