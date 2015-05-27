from django.views.generic import base
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from models import *
from forms import *
from django.contrib.auth.models import User
import hashlib

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

        formulario = FormularioLogin(request.POST)

        mensaje = ''

        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']

            try:
                username = User.objects.get(usuario=Usuario.objects.get(correo=username)).username
            except Exception, e:
                pass

            usuario = authenticate(username=username, password=password)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return render(request, 'index.html', {})
            else:
                mensaje = "usuario y/o password incorrecto"

        ctx = {
            'mensaje_login_error': mensaje
        }
        return render(request, 'index.html', ctx)

class LogOutView(base.View):

    def post(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'index.html', {})

class RegitrarseView(base.View):

    def get(self, request, *args, **kwargs):
        ctx = {
            'formulario': FormularioRegistro()
        }
        return render(request, 'registro.html', ctx)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        formulario = FormularioRegistro(request.POST)
        print formulario.is_valid()
        if formulario.is_valid():
            usuario = None
            try:
                usuario= User.objects.get(username=formulario.cleaned_data['DNI'])
            except Exception, e:
                pass
            if not usuario:
                cleaned_data = formulario.cleaned_data
                try:
                    usuario = Usuario.objects.create(dni=cleaned_data['DNI'], nombre=cleaned_data['Nombre'],
                                                     correo=cleaned_data['Correo'])
                except Exception, e:
                    try:
                        Usuario.objects.get(correo=cleaned_data['Correo'])
                        ctx = {
                            'error': 'El correo ya ha sido registrado anteriormente'
                        }
                        return render(request, 'registro.html', ctx)
                    except Exception, e:
                        ctx = {
                            'error': 'El DNI ya ha sido registrado anteriormente'
                        }
                        return render(request, 'registro.html', ctx)

                md = hashlib.md5()
                md.update(str(cleaned_data['DNI']))
                codigo = md.hexdigest()[:9]
                carnet = Carnet.objects.create(codigo=codigo, usuario_id_usuario=usuario)
                carnet.save()
                usuario.carnet = carnet
                usuario.save()
                ctx = {
                    'registrado': True,
                    'codigo': codigo
                }

                user = User.objects.create_user(cleaned_data['DNI'], cleaned_data['Correo'], codigo)

                return render(request, 'registro.html', ctx)
            else:
                ctx = {
                    'error': 'El DNI ya ha sido registrado anteriormente'
                }
                return render(request, 'registro.html', ctx)

        ctx = {
            'error': 'No se ha suministrado informacion'
        }
        return render(request, 'registro.html', ctx)


class LibroView(base.View):

    def get(self, request, *args, **kwargs):
        libros = Libro.objects.all()

        get_keys = request.GET.keys()

        input_values = {
            'tema': '',
            'autor': '',
            'libro': ''
        }

        queries = [libros.query]

        if 'autor' in get_keys:
            libros = libros.filter(pk__in=Autor.objects.filter(nombre__icontains=request.GET['autor']).values('libros'))
            input_values['autor'] = request.GET['autor']
            queries.append(libros.query)

        if 'tema' in get_keys:
            libros = libros.filter(pk__in=Tema.objects.filter(nombre__icontains=request.GET['tema']).values('libros'))
            input_values['tema'] = request.GET['tema']
            queries.append(libros.query)

        if 'libro' in get_keys:
            libros = libros.filter(titulo__icontains=request.GET['libro'])
            input_values['libro'] = request.GET['libro']
            queries.append(libros.query)

        ctx = {
            'libros': libros,
            'input_values': input_values,
            'queries': []
        }
        return render(request, 'libros.html', ctx)

    def post(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'index.html', ctx)


class DocumentalView(base.View):

    def get(self, request, *args, **kwargs):
        documentales = Documental.objects.all()

        queries = [documentales.query]

        get_keys = request.GET.keys()

        input_values = {
            'tema': '',
            'titulo': ''
        }

        if 'tema' in get_keys:
            documentales = documentales.filter(
                pk__in=Tema.objects.filter(nombre__icontains=request.GET['tema']).values('documentales')
            )
            input_values['tema'] = request.GET['tema']
            queries.append(documentales.query)

        if 'titulo' in get_keys:
            documentales = documentales.filter(titulo__icontains=request.GET['titulo'])
            input_values['titulo'] = request.GET['titulo']
            queries.append(documentales.query)

        ctx = {
            'documentales': documentales,
            'input_values': input_values,
            'queries': []
        }
        return render(request, 'documentales.html', ctx)

    def post(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'index.html', ctx)


class LibroDigitalView(base.View):

    def get(self, request, *args, **kwargs):
        libros_digitales = LibroDigital.objects.all()

        get_keys = request.GET.keys()

        queries = [libros_digitales.query]

        input_values = {
            'autor': '',
            'titulo': ''
        }

        if 'autor' in get_keys:
            libros_digitales = libros_digitales.filter(pk__in=Autor.objects.filter(nombre__icontains=request.GET['autor']).values('libros_digitales'))
            input_values['autor'] = request.GET['autor']
            queries.append(libros_digitales.query)

        if 'titulo' in get_keys:
            libros_digitales = libros_digitales.filter(titulo__icontains=request.GET['titulo'])
            input_values['titulo'] = request.GET['titulo']
            queries.append(libros_digitales.query)

        ctx = {
            'libros_digitales': libros_digitales,
            'input_values': input_values,
            'queries': []
        }
        return render(request, 'libro_digital.html', ctx)

    def post(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'index.html', ctx)


class PeriodicoView(base.View):

    def get(self, request, *args, **kwargs):
        periodicos = Periodicos.objects.all()

        get_keys = request.GET.keys()

        input_values = {
            'nombre': ''
        }

        queries = [periodicos.query]

        if 'nombre' in get_keys:
            periodicos = periodicos.filter(nombre__icontains=request.GET['nombre'])
            input_values['nombre'] = request.GET['nombre']
            queries.append(periodicos.query)

        ctx = {
            'periodicos': periodicos,
            'input_values': input_values,
            'queries': []
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


class AcercaDeNosotrosView(base.View):

    def get(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'acerca_de_nosotros.html', ctx)