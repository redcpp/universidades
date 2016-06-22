from django.shortcuts import render, get_object_or_404
from .models import Estado, Universidad, Carrera
from django.db.models import Count
from django.db.models import Q, F
from django.shortcuts import redirect

def home(request):
	return render(request,'unsearch/index.html')

def estado(request, pk):
	estado = get_object_or_404(Estado, pk=pk)
	num_carreras = Carrera.objects.filter(universidad__estado__pk=pk).count
	universidades = Universidad.objects.filter(estado__pk=pk)
	return render(request,'unsearch/estado.html', {'estado':estado, 'carreras':num_carreras, 'universidades':universidades})

def estado_buscar(request, pk):
	if request.method == 'POST':
		_s = request.POST.get('busqueda')
		if _s == '':
			return redirect('unsearch:estado', pk=pk)
		estado = get_object_or_404(Estado, pk=pk)
		num_carreras = Carrera.objects.filter(universidad__estado__pk=pk).count		
		universidades = Universidad.objects.distinct().filter(Q(estado__pk=pk) & Q(carreras__nombre__icontains=_s)).annotate(matches=F('carreras__nombre'))
		return render(request,'unsearch/busqueda_estado.html', {'estado':estado, 'carreras':num_carreras, 'universidades':universidades, 'busqueda':_s})
	else:
		return redirect('unsearch:estado', pk=pk)

def universidad(request, pk):
	universidad = get_object_or_404(Universidad, pk=pk)
	carreras = Carrera.objects.filter(universidad__pk=pk)
	return render(request,'unsearch/universidad.html', {'carreras':carreras, 'universidad':universidad})

def contacto(request):
	return render(request, 'unsearch/contacto.html')