from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^estado/(?P<pk>[0-9]+)/$', views.estado, name='estado'),
	url(r'^universidad/(?P<pk>[0-9]+)/$', views.universidad, name='universidad'),
]