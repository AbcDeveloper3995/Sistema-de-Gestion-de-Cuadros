from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.db.models import Q

from apps.cuadro.forms import *
from apps.cuadro.models import *


# PROCEDIMIENTO PARA LISTAR CUADROS.
class listarCuadroView(LoginRequiredMixin, ListView):
    template_name = 'cuadro/listar/listarCuadros.html'
    model = Cuadro
    context_object_name = 'cuadros'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Cuadros'
        context['tituloPestaña'] = 'SGPC | Cuadros'
        return context


# PROCEDIMIENTO PARA CREAR CUADROS.
class crearCuadroView(LoginRequiredMixin, CreateView):
    template_name = 'cuadro/crear/crearCuadros.html'
    model = Cuadro
    form_class = cuadroForm
    success_url = reverse_lazy('cuadro:listarCuadro')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creacion de Cuadro'
        context['tituloPestaña'] = 'SGPC | Cuadro'
        return context

# PROCEDIMIENTO PARA MODIFICAR CUADROS.
class modificarCuadroView(LoginRequiredMixin, UpdateView):
    model = Cuadro
    form_class = cuadroForm
    template_name = 'cuadro/crear/crearCuadros.html'
    success_url = reverse_lazy('cuadro:listarCuadro')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edicion de Cuadro'
        context['tituloPestaña'] = 'SGPC | Cuadro'
        return context

# PROCEDIMIENTO PARA ELIMINAR CUADROS.
class eliminarCuadroView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        data = {}
        try:
            data['message'] = 'El cuadro se ha eliminado correctamente.'
            query = get_object_or_404(Cuadro, id=request.GET['id'])
            query.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


# PROCEDIMIENTO PARA LISTAR CARGOS.
class listarCargoView(LoginRequiredMixin, ListView):
    template_name = 'cuadro/listar/listarCargos.html'
    model = Cargo

    def get_queryset(self):
        return Cargo.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cargos'] = self.get_queryset()
        context['titulo'] = 'Listado de Cargos'
        context['tituloPestaña'] = 'SGPC | Cuadros'
        return context


# PROCEDIMIENTO PARA CREAR CARGOS.
class crearCargoView(LoginRequiredMixin, CreateView):
    template_name = 'cuadro/crear/crearCargo.html'
    model = Cargo
    form_class = cargoForm
    success_url = reverse_lazy('cuadro:listarCargo')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creacion de Cargo'
        context['tituloPestaña'] = 'SGPC | Cuadros'
        return context

# PROCEDIMIENTO PARA MODIFICAR CARGOS.
class modificarCargoView(LoginRequiredMixin, UpdateView):
    model = Cargo
    form_class = cargoForm
    template_name = 'cuadro/crear/crearCargo.html'
    success_url = reverse_lazy('cuadro:listarCargo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edicion de grupo de Cargo'
        context['tituloPestaña'] = 'SGPC | Cuadros'
        return context

# PROCEDIMIENTO PARA ELIMINAR CARGOS.
class eliminarCargoView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        data = {}
        try:
            data['message'] = 'El cargo se ha eliminado correctamente.'
            query = get_object_or_404(Cargo, id=request.GET['id'])
            query.estado = False
            query.save()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


# PROCEDIMIENTO PARA LISTAR ESPECIALIDAD.
class listarEspecialidadView(LoginRequiredMixin, ListView):
    template_name = 'cuadro/listar/listarEspecialidad.html'
    model = Especialidad

    def get_queryset(self):
        return Especialidad.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['especialidades'] = self.get_queryset()
        context['titulo'] = 'Listado de Especialidades'
        context['tituloPestaña'] = 'SGPC | Cuadros'
        return context


# PROCEDIMIENTO PARA CREAR ESPECIALIDAD.
class crearEspecialidadView(LoginRequiredMixin, CreateView):
    template_name = 'cuadro/crear/crearEspecialidad.html'
    model = Especialidad
    form_class = especialidadForm
    success_url = reverse_lazy('cuadro:listarEspecialidad')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creacion de una Especilidad'
        context['tituloPestaña'] = 'SGPC | Cuadros'
        return context

# PROCEDIMIENTO PARA MODIFICAR ESPECIALIDAD.
class modificarEspecialidadView(LoginRequiredMixin, UpdateView):
    model = Especialidad
    form_class = especialidadForm
    template_name = 'cuadro/crear/crearEspecialidad.html'
    success_url = reverse_lazy('cuadro:listarEspecialidad')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edicion de una Especialidad'
        context['tituloPestaña'] = 'SGPC | Cuadros'
        return context

# PROCEDIMIENTO PARA ELIMINAR ESPECIALIDAD.
class eliminarEspecialidadView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        data = {}
        try:
            data['message'] = 'El cargo se ha eliminado correctamente.'
            query = get_object_or_404(Especialidad, id=request.GET['id'])
            query.estado = False
            query.save()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

