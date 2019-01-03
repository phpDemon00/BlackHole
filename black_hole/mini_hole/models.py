from django.db import models

# Create your models here.

class Mini_hole(models.Model):
	name = models.CharField(max_length=64)
	surname = models.CharField(max_length=64)
	salary = models.CharField(max_length=14)