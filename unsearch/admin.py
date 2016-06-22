from django.contrib import admin
from .models import Carrera, Universidad, Estado

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'universidad', 'grado')
	list_filter = ('universidad__estado__nombre', 'grado', 'universidad')

@admin.register(Universidad)
class UniversidadCarrera(admin.ModelAdmin):
	list_display = ('nombre', 'tipo', 'estado')
	list_filter = ('estado__nombre', 'tipo')

class EstadoAdmin(admin.ModelAdmin):
	list_display = ('pk', 'nombre', 'imagen')

admin.site.register(Estado, EstadoAdmin)