from django import template

register = template.Library()

@register.filter(name='get_property')
def get_property(obj, property):
	return getattr(obj, property)

@register.filter(name='ordenar_matches')
def ordenar_matches(lista):
	for l in lista:
		l['lenght'] = len(l['list'])
	return sorted(lista, key=lambda k: k['lenght'])