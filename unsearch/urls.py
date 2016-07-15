from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^estado/(?P<pk>[0-9]+)/$', views.estado, name='estado'),
	url(r'^estado/(?P<pk>[0-9]+)/buscar/$', views.estado_buscar, name='estado_buscar'),
	url(r'^universidad/(?P<pk>[0-9]+)/$', views.universidad, name='universidad'),
	url(r'^buscador_nacional/$', views.buscador_nacional, name='buscador_nacional'),
	url(r'^test/$', views.test, name='test'),
	url(r'^contacto/$', views.contacto, name='contacto'),
]