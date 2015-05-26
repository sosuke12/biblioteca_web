"""biblioteca_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from pagina import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', views.IndexView.as_view(), name='index_url'),
    url(r'^login/?$', views.LoginView.as_view(), name='login_url'),
    url(r'^listar/libros/?$', views.LibroView.as_view(), name='libro_url'),
    url(r'^listar/documentales/?$', views.DocumentalView.as_view(), name='documental_url'),
    url(r'^listar/libros_digitales/?$', views.LibroDigitalView.as_view(), name='libro_digital_url'),
    url(r'^listar/periodicos/?$', views.PeriodicoView.as_view(), name='periodico_url'),
    url(r'^registrarse/?$', views.RegitrarseView.as_view(), name='registro_url'),
    url(r'^multa/?$', views.MultaView.as_view(), name='registro_url'),
    url(r'^prestamo/?$', views.PrestamoView.as_view(), name='registro_url'),
]
