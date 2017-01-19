from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from myedu.models import Education #imports the Education model from myedu app
from .models import Intro
from myexperience.models import Experience
from contactme.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from contactme.models import Contact
from .models import WhatIDo
from .models import ImagesPortifolio
from .models import Clients


def index(request):

	template=loader.get_template('myprofile/home.html')
	#return render(request, 'myprofile/home.html')

	context = {
		'Introduction': Intro.objects.all(),
		'All_Education' : Education.objects.all(),
		'Experiences' : Experience.objects.all(),
		'WhatIDo':WhatIDo.objects.all(),
		'Portifolio':ImagesPortifolio.objects.all(),
		'All_Clients': Clients.objects.all(),

	}
	sendMessage(request)

	return HttpResponse(template.render(context, request))
	

	



def sendMessage(request):

	if request.method=='POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			Name=request.POST.get('Name','')
			Email=request.POST.get('Email','')
			Phone=request.POST.get('Phone','')
			Message=request.POST.get('Message','')
			contact_obj=Contact(Name=Name, Email=Email, Phone= Phone, Message=Message)
			contact_obj.save()

			return render (request, 'myprofile/home.html')

	else:
		form = ContactForm()

	return render(request, 'myprofile/home.html',{'form':form})




