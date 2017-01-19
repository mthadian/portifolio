from django.db import models

# Create your models here.
class Education(models.Model):
	Duration=models.CharField(max_length=20)
	Degree=models.CharField(max_length=50)
	Institution=models.CharField(max_length=50)
	Description=models.CharField(max_length=2000)

	def __str__(self):
		return self.Institution

	class Meta:
		verbose_name_plural='Education'
