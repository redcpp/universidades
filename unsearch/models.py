from django.db import models

class Estado(models.Model):
	nombre = models.CharField(max_length=50)
	imagen = models.ImageField(null=True, blank=True)
	municipios = models.IntegerField(default=0)

	class Meta:
		verbose_name = "Estado"
		verbose_name_plural = "Estados"

	def __str__(self):
		return self.nombre

class Universidad(models.Model):
	estado = models.ForeignKey('unsearch.Estado', related_name='universidades')
	nombre = models.CharField(max_length=150)
	tipo = models.CharField(max_length=50) # Privada, publica, etc
	sitio_web = models.CharField(max_length=75, blank=True, null=True)

	class Meta:
		verbose_name = "Universidad"
		verbose_name_plural = "Universidades"

	def __str__(self):
		return self.nombre

class Carrera(models.Model):
	universidad = models.ForeignKey('unsearch.Universidad', related_name='carreras')
	nombre = models.CharField(max_length=100)
	grado = models.CharField(max_length=50) # Licenciatura, especialdad, etc

	class Meta:
		verbose_name = "Carrera"
		verbose_name_plural = "Carreras"

	def __str__(self):
		return self.nombre