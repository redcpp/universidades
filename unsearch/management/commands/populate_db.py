from django.core.management.base import BaseCommand
from unsearch.models import Carrera, Universidad, Estado

from bs4 import BeautifulSoup
import requests
import re

lista_estados = ['Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche', 'Coahuila', 'Colima', 'Chiapas', 'Chihuahua', 'Distrito Federal', 'Durango', 'Guanajuato', 'Guerrero', 'Hidalgo', 'Jalisco', 'Estado de México', 'Michoacán', 'Morelos', 'Nayarit', 'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro', 'Quintana Roo', 'San Luis Potosí', 'Sinaloa', 'Sonora', 'Tabasco', 'Tamaulipas', 'Tlaxcala', 'Veracruz', 'Yucatán', 'Zacatecas']
# Falta El DF(8) y Puebla(20)

def normalize_encoding(string):
	return string.encode('iso-8859-1').decode('utf-8')

class Command(BaseCommand):
	args = '<foo bar ...>'
	help = 'We will scrap studyinmexico.sep.gob.mx/'

	def _get_data(self):
		for id_estado in [20]:
			# Insertamos el estado a base de datos
			_current_estado = Estado.objects.create(nombre=lista_estados[id_estado])
			print(_current_estado)
			print('-'*100)

			estado_url = 'http://www.studyinmexico.sep.gob.mx/subsistemas.php?edo=' + str(id_estado+1)
			estado_page = requests.get(estado_url, verify=False)
			estado_soup = BeautifulSoup(estado_page.text, 'html5lib')

			''' Para cada tipo (publica, privada, etc) '''
			for tipo in estado_soup.find_all('a', id='botoncito_azul'):
				tipo_url = 'http://www.studyinmexico.sep.gob.mx/' + tipo.get('href')
				tipo_page = requests.get(tipo_url, verify=False)
				tipo_soup = BeautifulSoup(tipo_page.text, 'html5lib')

				_current_tipo = normalize_encoding(tipo_soup.find('p', class_='tex_nombre_instituto').contents[0])
				print(_current_tipo)
				print('-'*25)

				''' Para cada universidad '''
				for universidad in tipo_soup.select('#btn_marco_uni > a'):
					universidad_link = universidad.get('href')
					universidad_url = 'http://www.studyinmexico.sep.gob.mx/' + universidad_link
					universidad_page = requests.get(universidad_url, verify=False)
					universidad_soup = BeautifulSoup(universidad_page.text, 'html5lib')
					sitio_web = 0

					# Insertamos la universidad a base de datos
					_current_universidad = Universidad.objects.create(
						estado=_current_estado,
						nombre=normalize_encoding(universidad_soup.find('p', class_='tex_nombre_estado').contents[0]),
						tipo=_current_tipo
					)
					print(' '*5, _current_universidad)

					''' Para cada grado de estudios '''
					for grado in universidad_soup.find_all('a', id='botoncito_mediano'):
						grado_link = grado.get('href')
						grado_url = 'http://www.studyinmexico.sep.gob.mx/' + grado_link
						grado_page = requests.get(grado_url, verify=False)
						grado_soup = BeautifulSoup(grado_page.text, 'html5lib')

						if not sitio_web:
							sitio_web = 1
							_current_universidad.sitio_web = grado_soup.find('a', class_='tex_mediano_btn').get('href')
							_current_universidad.save()
							print(' '*5,_current_universidad.sitio_web)

						_current_grado = normalize_encoding((grado_soup.find('div', class_='texto_uam_bold_gris').contents[3])[17:])

						'''Buscar las carreras del grado de estudios en que nos encontramos'''
						for carrera in grado_soup.find_all('p', class_='texto_gris_btn_a'):
							# Insertamos carrera a base de datos
							Carrera.objects.create(universidad=_current_universidad, nombre=carrera.contents[0], grado=_current_grado)

	def handle(self, *args, **options):
		self._get_data()