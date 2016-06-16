from django.shortcuts import render, get_object_or_404
from .models import Estado, Universidad, Carrera
from django.db.models import Count

def home(request):
	return render(request,'unsearch/index.html')

def estado(request, pk):
	estado = get_object_or_404(Estado, pk=pk)
	carreras = Carrera.objects.filter(universidad__estado__pk=pk).count
	universidades = Universidad.objects.filter(estado__pk=pk)
	return render(request,'unsearch/estado.html', {'estado':estado, 'carreras':carreras, 'universidades':universidades})