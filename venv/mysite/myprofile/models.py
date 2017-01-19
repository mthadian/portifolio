from django.db import models

class Intro(models.Model):
	Name=models.CharField(max_length=70)
	Mobile1=models.CharField(max_length=15)
	Mobile=models.CharField(max_length=15)
	email=models.CharField(max_length=30)

	def __str__(self):
		return self.Name
	class Meta:
		verbose_name_plural='Introduction'

class WhatIDo(models.Model):
	whyMe=models.TextField()
	whatDo=models.TextField()
	mission=models.TextField()

	def __str__(self):
		return self.whyMe

	class Meta:
		verbose_name_plural="What I Do"

class ImagesPortifolio(models.Model):
	project=models.CharField(max_length=150)
	image=models.FileField()
	description=models.TextField(max_length=500)

	def __str__(self):
		return self.project

	class Meta:
		verbose_name_plural="Portifolio"

class Clients(models.Model):
	No_Client=models.CharField(max_length=5)
	No_Projects=models.CharField(max_length=5)
	No_Exp=models.CharField(max_length=5)
	Ongoing=models.CharField(max_length=5)

	def __str__(self):
		return self.No_Client

	class Meta:
			verbose_name_plural="Clients"

