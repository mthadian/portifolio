from django.db import models

# Create your models here.
class Experience(models.Model):
	Period=models.CharField(max_length=15)
	Institution=models.CharField(max_length=30)
	Title=models.CharField(max_length=20)
	Description=models.CharField(max_length=2000)
	
	def __str__(self):
		return self.Institution

	class Meta:
		verbose_name_plural='Experience'