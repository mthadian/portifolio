from django.db import models

# Create your models here.
class Contact(models.Model):
	Name=models.CharField(max_length=100)
	Email=models.CharField(max_length=100)
	Phone=models.CharField(max_length=30)
	Message=models.TextField()
	#activate=models.BooleanField(initial=False)

	def __str__(self):
		return self.Name

	class Meta:
		verbose_name_plural='Contact Me'

