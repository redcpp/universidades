from django.contrib import admin
from django.db.models import Count
from .models import Carrera, Universidad, Estado, Busqueda

class CarreraInline(admin.TabularInline):
	model = Carrera

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'universidad', 'grado')
	list_filter = ('universidad__estado__nombre', 'grado')
	search_fields = ('nombre',)

@admin.register(Universidad)
class UniversidadAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'show_carreras_count', 'estado', 'tipo')
	list_filter = ('estado__nombre', 'tipo')
	search_fields = ('nombre',)
	inlines = [
		CarreraInline,
	]
	def get_queryset(self, request):
		return Universidad.objects.annotate(carreras_count=Count('carreras'))
	def show_carreras_count(self, inst):
		return inst.carreras_count
	show_carreras_count.admin_order_field = 'carreras_count'

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
	list_display = ('pk', 'nombre', 'municipios', 'imagen')

@admin.register(Busqueda)
class BusquedaAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'query', 'root', 'estado', 'num_resultados')
	list_filter = ('estado', 'root')