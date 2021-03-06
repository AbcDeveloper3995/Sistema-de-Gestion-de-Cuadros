import SGPC.settings as setting

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from apps.usuario.forms import usuarioForm, usuarioProfileForm
from apps.usuario.models import Usuario
from apps.utils import cantidadPorGenero, cantidadPorCategoria, cantidadSegunMilitancia, cantidadPorColor, \
    cantidadPorEdad, cantidadPorEscolaridad, cantidadPorTiempo


class Login(LoginView):
    template_name = 'usuario/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(setting.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tituloPestaña'] = 'SGPC | Inicio sesion'
        return context


class homeView(LoginRequiredMixin, TemplateView):
    template_name = 'comun/home.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'cantidadPorGenero':
                data = {
                    'name':'Cantidad',
                    'showInLegend': False,
                    'colorByPoint':True,
                    'data': cantidadPorGenero(self.request.user),
                }
            elif action == 'cantidaPorCategoria':
                data = {
                    'name':'Cantidad',
                    'showInLegend': False,
                    'colorByPoint':True,
                    'data': cantidadPorCategoria(self.request.user),
                }
            elif action == 'cantidadSegunMilitancia':
                data = {
                    'name': 'Cantidad',
                    'showInLegend': False,
                    'colorByPoint': True,
                    'data': cantidadSegunMilitancia(self.request.user),
                }
            elif action == 'cantidaPorColor':
                data = {
                    'name':'Cantidad',
                    'showInLegend': False,
                    'colorByPoint':True,
                    'data': cantidadPorColor(self.request.user),
                }
            elif action == 'cantidaPorEdad':
                data = {
                    'name':'Cantidad',
                    'showInLegend': False,
                    'colorByPoint':True,
                    'data': cantidadPorEdad(self.request.user),
                }
            elif action == 'cantidaPorEscolaridad':
                data = {
                    'name':'Cantidad',
                    'showInLegend': False,
                    'colorByPoint':True,
                    'data': cantidadPorEscolaridad(self.request.user),
                }
            elif action == 'cantidaPorTiempo':
                data = {
                    'name':'Cantidad',
                    'showInLegend': False,
                    'colorByPoint':True,
                    'data': cantidadPorTiempo(self.request.user),
                }
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tituloPestaña'] = 'SGPC | Inicio'
        return context

# PROCEDIMIENTO PARA LISTAR USUARIOS.
class listarUsuariosView(LoginRequiredMixin, ListView):
    template_name = 'usuario/listar.html'
    model = Usuario
    context_object_name = 'usuarios'

    def get_queryset(self):
        return Usuario.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Usuarios'
        context['tituloPestaña'] = 'SGPC | Usuarios'
        return context

# PROCEDIMIENTO PARA CREAR USUARIOS.
class crearUsuarioView(LoginRequiredMixin, CreateView):
    template_name = 'usuario/crear.html'
    model = Usuario
    form_class = usuarioForm
    success_url = reverse_lazy('usuario:listarUsuario')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(self.request, 'Usuario creado correctamente.')
            form.save()
        else:
            messages.error(self.request, form.errors)
        return redirect('usuario:listarUsuario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creacion de usuario'
        context['tituloPestaña'] = 'SGPC | Usuarios'
        context['action'] = 'crear'
        return context

# PROCEDIMIENTO PARA MODIFICAR USUARIOS.
class updateUsuarioView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = usuarioForm
    template_name = 'usuario/crear.html'
    success_url = reverse_lazy('usuario:listarUsuario')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(self.request, 'Usuario modificado correctamente.')
            form.save()
        else:
            messages.error(self.request, form.errors)
        return redirect('usuario:listarUsuario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edicion de usuario'
        context['tituloPestaña'] = 'SGPC | Usuarios'
        return context

# PROCEDIMIENTO PARA ELIMINAR USUARIOS.
class eliminarUsuarioView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        data = {}
        print(request.GET['id'])
        try:
            query = get_object_or_404(Usuario, id=request.GET['id'])
            messages.success(self.request, 'El usuario ' + query.name + ' se ha eliminado correctamente.')
            query.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

# PROCEDIMIENTO PARA QUE UN USUARIO MODIFIQUE SU PERFIL.
class updateUsuarioProfileView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = usuarioProfileForm
    template_name = 'usuario/usuarioProfile.html'
    success_url = reverse_lazy('usuario:home')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edicion de perfil'