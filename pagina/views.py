from django.views.generic import base
from django.shortcuts import render
from models import *

# Create your views here.

class IndexView(base.View):

    def get(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'index.html', ctx)


class LoginView(base.View):

    def get(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'login.html', ctx)

    def post(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'index.html', ctx)


class RegitrarseView(base.View):

    def get(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'registro.html', ctx)

    def post(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'index.html', ctx)


class LibroView(base.View):

    def get(self, request, *args, **kwargs):
        libros = Libro.objects.all()
        ctx = {
            'libros': libros
        }
        return render(request, 'libros.html', ctx)

    def post(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'index.html', ctx)


class DocumentalView(base.View):

    def get(self, request, *args, **kwargs):
        documentales = Documental.objects.all()
        ctx = {
            'documentales': documentales
        }
        return render(request, 'documentales.html', ctx)

    def post(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'index.html', ctx)


class LibroDigitalView(base.View):

    def get(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'libro_digital.html', ctx)

    def post(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'index.html', ctx)


class PeriodicoView(base.View):

    def get(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'periodicos.html', ctx)

    def post(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'index.html', ctx)


class PrestamoView(base.View):

    def get(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'prestamo.html', ctx)

    def post(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'index.html', ctx)


class MultaView(base.View):

    def get(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'multa.html', ctx)

    def post(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'index.html', ctx)

