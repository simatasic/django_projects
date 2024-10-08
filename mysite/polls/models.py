from django.db import models

class User(models.Model):
	name=models.CharField(max_lenghtt=20)
	email=models.CharField(max_lenght=128)
# Create your models here.
