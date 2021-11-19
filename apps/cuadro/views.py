import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, TemplateView

from apps.cuadro.forms import *
from apps.cuadro.models import *
from apps.utils import disabledCargoComoVacante, enableCargoComoVacante


# PROCEDIMIENTO PARA LISTAR CUADROS.
class listarCuadroView(LoginRequiredMixin, ListView):
    template_name = 'cuadro/listar/listarCuadros.html'
    model = Cuadro
    context_object_name = 'cuadros'

    def get_queryset(self):
        query = Cuadro.objects.all()
        hora = datetime.datetime.today().hour
        minutos = datetime.datetime.today().minute
        if int(hora) == 8 and int(minutos) == 30:
            self.actualizarEdad(query)
        else:
            print('No es la hora fijada para la actualizacion de la edad')
        return query

    def actualizarEdad(self, listadoCuadros):
        diaActual = datetime.datetime.today().day
        mesActual = datetime.datetime.today().month
        for i in listadoCuadros:
            diaCI = str(i.ci)[4:6]
            mesCI = str(i.ci)[2:4]
            if int(diaCI) == int(diaActual) and int(mesCI) == int(mesActual):
                i.edad += 1
                i.save()

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

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(self.request, 'Cuadro creado correctamente.')
            form.save()
            disabledCargoComoVacante()
        else:
            messages.error(self.request, form.errors)
        return redirect('cuadro:listarCuadro')

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
            query = get_object_or_404(Cuadro, id=request.GET['id'])
            enableCargoComoVacante(query)
            messages.success(self.request, 'El cuadro ' + query.nombre + ' se ha eliminado correctamente.')
            query.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


# PROCEDIMIENTO PARA ELIMINAR TODOS LOS CUADROS.
class eliminarCuadroAllView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        data = {}
        try:
            data['message'] = 'Los cuadros se ha eliminado correctamente.'
            query = Cuadro.objects.all()
            for i in query:
                enableCargoComoVacante(i)
                i.delete()
            messages.success(self.request, 'Todos los cuadros han sido eliminados correctamente.')
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


# PROCEDIMIENTO PARA LISTAR CARGOS.
class listarCargoView(LoginRequiredMixin, ListView):
    template_name = 'cuadro/listar/listarCargos.html'
    model = Cargo

    def get_queryset(self):
        return Cargo.objects.all()

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
            query = get_object_or_404(Cargo, id=request.GET['id'])
            query.estado = False
            messages.success(self.request, 'El cargo de ' + query.nombre + ' se ha eliminado correctamente.')
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
            query = get_object_or_404(Especialidad, id=request.GET['id'])
            query.estado = False
            messages.success(self.request, 'La especialidad ' + query.nombre + ' se ha eliminado correctamente.')
            query.save()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

# PROCEDIMIENTO PARA ELIMINAR ESPECIALIDAD.
class isVacanteView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        data = {}
        try:
            query = get_object_or_404(Cargo, id=request.GET['cargo'])
            if query.vacante == False:
                data['message'] = 'Este cargo no esta vacante.'
                data['vacante'] = False
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

