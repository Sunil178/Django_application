from django.db import models

# Create your models here.

class Students(models.Model):
	enrollment = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
