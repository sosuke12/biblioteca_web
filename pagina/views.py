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
        if formulario.is_valid():
            usuario = None
            try:
                usuario= User.objects.get(username=formulario.cleaned_data['DNI'])
            except Exception, e:
                print e
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

        ctx = {
            'error': 'No se ha suministrado informacion'
        }
        return render(request, 'registro.html', ctx)


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


class AcercaDeNosotrosView(base.View):

    def get(self, request, *args, **kwargs):
        ctx = {

        }
        return render(request, 'acerca_de_nosotros.html', ctx)


        # class LoginView(base.View):
        #
        #     def get(self, request, *args, **kwargs):
        #         """
        #         :param request:
        #         :param args:
        #         :param kwargs:
        #         :return:retorna el temaplate con la informacion del usuario logueado o retorna el template  de logueo
        #         """
        #         form = LoginForm()
        #         ctx = {'formulario': form}
        #         print form.as_p()
        #         return render(request, 'pagina/desktop/index.html', ctx)
        #
        #     def post(self, request, *args, **kwargs):
        #         """
        #         :param request: username y un password
        #         :param args:
        #         :param kwargs:
        #         :return: retorna el template del index de un usuario logueado o retorna un template de error de logueo
        #         """
        #         user = json.loads(request.body)  # Se debe decodificar haciendo uso de la clase json, ya que  es informacion
        #         # suministrada  por un javascript.
        #         form = LoginForm()
        #         mensaje = "formulario invalido"
        #         if form.is_valid():
        #             username = form.cleaned_data['username']
        #             password = form.cleaned_data['password']
        #
        #             try:
        #                 username = Cuenta.objects.get(usuario=Usuario.objects.get(correo=username)).username
        #             except Exception, e:
        #                 pass
        #
        #             usuario = authenticate(username=username, password=password)
        #             if usuario is not None and usuario.is_active:
        #                 login(request, usuario)
        #                 return HttpResponse("sucess")
        #             else:
        #                 mensaje = "usuario y/o password incorrecto"
        #         return HttpResponseServerError(mensaje)
        #
        #     def delete(self, request, *args, **kwargs):
        #         logout(request)
        #         return HttpResponse('sucess')