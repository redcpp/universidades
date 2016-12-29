from django.test import TestCase
from django.utils import timezone
from .models import Carrera, Universidad, Estado, Busqueda

class BusquedaTest(TestCase):
	def setUp(self):
		aguascalientes = Estado.objects.create(nombre='Aguascalientes', municipios=11)
		Busqueda.objects.create(estado=aguascalientes, query='Medicina', root='Medic', fecha=timezone.now())

	def test_busqueda_estado_db(self):
		aguascalientes = Estado.objects.last()
		ultima_busqueda = Busqueda.objects.last()
		self.assertEqual(ultima_busqueda.query, 'Medicina')
		self.assertEqual(ultima_busqueda.root, 'Medic')
		self.assertEqual(ultima_busqueda.estado, aguascalientes)

class EstadoTest(TestCase):
	def setUp(self):
		Estado.objects.create(nombre='Aguascalientes', municipios=11)

	def test_estado_db(self):
		aguascalientes = Estado.objects.get(nombre='Aguascalientes')
		self.assertEqual(aguascalientes.nombre, 'Aguascalientes')
		self.assertEqual(aguascalientes.municipios, 11)

class UniversidadTest(TestCase):
	def setUp(self):
		aguascalientes = Estado.objects.create(nombre='Aguascalientes')
		Universidad.objects.create(
			estado=aguascalientes,
			nombre='Universidad Autónoma de Aguascalientes',
			tipo='Pública',
			sitio_web='uag.mx'
		)
		Universidad.objects.create(
			estado=aguascalientes,
			nombre='Universidad Patito de Aguascalientes',
			tipo='Privada'
		)

	def test_universidad_db(self):
		autonoma = Universidad.objects.get(sitio_web='uag.mx')
		patito = Universidad.objects.get(nombre='Universidad Patito de Aguascalientes')
		self.assertEqual(autonoma.estado.nombre, 'Aguascalientes')
		self.assertEqual(patito.estado.nombre, 'Aguascalientes')
		self.assertEqual(autonoma.tipo, 'Pública')
		self.assertEqual(patito.tipo, 'Privada')
		self.assertEqual(autonoma.nombre, 'Universidad Autónoma de Aguascalientes')
		self.assertEqual(patito.nombre, 'Universidad Patito de Aguascalientes')

class CarreraTest(TestCase):
	def setUp(self):
		aguascalientes = Estado.objects.create(nombre='Aguascalientes')
		uag = Universidad.objects.create(
			estado= aguascalientes,
			nombre='Universidad Autónoma de Aguascalientes',
			tipo='Pública',
			sitio_web='uag.mx'
		)
		Carrera.objects.create(universidad=uag, nombre='Ingenieria software', grado='Licenciatura')

	def test_carrera_db(self):
		ing_software = Carrera.objects.get(nombre='Ingenieria software')
		self.assertEqual(ing_software.universidad.sitio_web, 'uag.mx')
		self.assertEqual(ing_software.grado, 'Licenciatura')