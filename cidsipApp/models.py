from django.db import models

class Proyecto(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre


class Computadora(models.Model):
	nombre = models.CharField(max_length=50)
	mac = models.CharField(max_length=50)
	ip = models.CharField(max_length=50)
	proyecto = models.ForeignKey(Proyecto, on_delete = models.CASCADE, blank = True)

	def __str__(self):
		return self.nombre
