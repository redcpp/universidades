from django.shortcuts import render, get_object_or_404
from .models import Estado, Universidad, Carrera, Busqueda
from django.db.models import Count
from django.db.models import Q, F
from django.shortcuts import redirect
from nltk.stem.snowball import SnowballStemmer
from django.utils import timezone

stemmer = SnowballStemmer("spanish")

def registro_de_busquedas(busqueda, raiz, estado, num_universidades):
	Busqueda.objects.create(estado=estado, query=busqueda, root=raiz, fecha=timezone.now(), num_resultados=num_universidades)

def home(request):
	carreras = Carrera.objects.count()
	universidades = Universidad.objects.count()
	return render(request,'unsearch/index.html', {'universidades':universidades, 'carreras':carreras})

def estado(request, pk):
	estado = get_object_or_404(Estado, pk=pk)
	num_carreras = Carrera.objects.filter(universidad__estado__pk=pk).count
	universidades = Universidad.objects.filter(estado__pk=pk)
	return render(request,'unsearch/estado.html', {'estado':estado, 'carreras':num_carreras, 'universidades':universidades})

def estado_buscar(request, pk):
	if request.method == 'POST':
		_s = request.POST.get('busqueda').strip()
		if _s == '':
			return redirect('unsearch:estado', pk=pk)
		estado = get_object_or_404(Estado, pk=pk)
		root = stemmer.stem(_s)
		carreras = Carrera.objects.distinct().filter( Q(universidad__estado__pk=pk) & (Q(nombre__icontains=root) | Q(nombre__icontains=_s)) ) #.annotate(matches=F('carreras__nombre'))
		# registro_de_busquedas(_s, root, estado, len(carreras))
		return render(request,'unsearch/busqueda_estado.html', {'estado':estado, 'carreras':carreras, 'busqueda':_s, 'num_resultados':len(carreras)})
	else:
		return redirect('unsearch:estado', pk=pk)

def universidad(request, pk):
	universidad = get_object_or_404(Universidad, pk=pk)
	carreras = Carrera.objects.filter(universidad__pk=pk).order_by('grado')
	return render(request,'unsearch/universidad.html', {'carreras':carreras, 'universidad':universidad})

def contacto(request):
	return render(request, 'unsearch/contacto.html')

def buscador_nacional(request):
	if request.method == 'POST':
		_s = request.POST.get('busqueda').strip()
		if _s == '':
			return redirect('unsearch:home')
		root = stemmer.stem(_s)
		carreras = Carrera.objects.distinct().filter( Q(nombre__icontains=root) | Q(nombre__icontains=_s) ).order_by('universidad__estado__nombre')
		tipos = sorted([x['universidad__tipo'] for x in carreras.order_by('universidad__tipo').values('universidad__tipo')])
		# registro_de_busquedas(_s, root, estado, len(carreras))
		return render(request,'unsearch/busqueda_nacional.html', {'carreras':carreras, 'busqueda':_s, 'tipos':tipos, 'num_resultados':len(carreras)})
	else:
		return redirect('unsearch:home')