from django.db import models


class Computadora(models.Model):
	nombre = models.CharField(max_length=50)
	mac = models.CharField(max_length=50)
	ip = models.CharField(max_length=50)