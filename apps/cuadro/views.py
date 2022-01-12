import datetime

from tablib import Dataset

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, TemplateView

from apps.cuadro.forms import *
from apps.cuadro.models import *
from apps.utils import disabledCargoComoVacante, enableCargoComoVacante, getCuadros


# PROCEDIMIENTO PARA LISTAR CUADROS.
class listarCuadroView(LoginRequiredMixin, ListView):
    template_name = 'cuadro/listar/listarCuadros.html'
    model = Cuadro
    context_object_name = 'cuadros'

    def get_queryset(self):
        query = getCuadros(self.request.user)
        self.actualizarEdad(query)
        return query

    def actualizarEdad(self, listadoCuadros):
        anoActual = datetime.datetime.today().year
        fragmentoAmoActual = str(anoActual)[2:4]
        for i in listadoCuadros:
            diaCI = str(i.ci)[4:6]
            mesCI = str(i.ci)[2:4]
            anoCI = str(i.ci)[0:2]
            if int(anoCI) > int(fragmentoAmoActual):
                anoCI = str('19' + anoCI)
                self.calcularEdad(diaCI, mesCI, anoCI, i)
            else:
                anoCI = int('20' + anoCI)
                self.calcularEdad(diaCI, mesCI, anoCI, i)

    def calcularEdad(self, dia, mes, ano, cuadro):
        fechaNacimiento = str(dia + '/' + mes + '/' + ano)
        fechaNacimiento = datetime.datetime.strptime(fechaNacimiento, "%d/%m/%Y").date()
        fechaActual = datetime.datetime.today().date()
        if fechaNacimiento <= fechaActual:
            day = fechaActual - fechaNacimiento
            edad = day.days // 365
            cuadro.edad = edad
            cuadro.save()

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

    def get_form_kwargs(self):
        kwargs = super(crearCuadroView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

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
        context['action'] = 'crear'
        return context


# PROCEDIMIENTO PARA MODIFICAR CUADROS.
class modificarCuadroView(LoginRequiredMixin, UpdateView):
    model = Cuadro
    form_class = cuadroForm
    template_name = 'cuadro/crear/crearCuadros.html'
    success_url = reverse_lazy('cuadro:listarCuadro')

    def get_form_kwargs(self):
        kwargs = super(modificarCuadroView, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

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
        return Cargo.objects.all().order_by('fk_clasificador_cargo_cuadro__codigo')

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

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(self.request, 'Cargo creado correctamente.')
            form.save()
        else:
            messages.error(self.request, form.errors)
        return redirect('cuadro:listarCargo')

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

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

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
            messages.success(self.request,
                             'El cargo de ' + query.fk_clasificador_cargo_cuadro.descripcion + ' se ha eliminado correctamente.')
            query.delete()
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


# PROCEDIMIENTO PARA DESACTIVAR CARGO.
'''Si un cargo es desactivado deja de ser vacante y ademas el cuadro que este ocupando dicho cargo se desactiva automaticamente'''


class desactivarCargoView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        data = {}
        idCargo = request.GET['id']
        try:
            query = get_object_or_404(Cargo, id=idCargo)
            cuadro = Cuadro.objects.get(fk_cargo__id=idCargo)
            if query and cuadro:
                messages.success(self.request,
                                 'El cargo ' + query.fk_clasificador_cargo_cuadro.descripcion + ' y el cuadro ' + cuadro.getFullName() + ' pasaron a ser inactivos.')
                query.estado = False
                query.vacante = False
                cuadro.estado = False
                query.save()
                cuadro.save()
            else:
                data['error'] = 'Ha ocurrido un error.'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


# PROCEDIMIENTO PARA DESACTIVAR CARGO.
'''Si un cargo es activado, pasa ha estar vacante tambien'''


class activarCargoView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        data = {}
        idCargo = request.GET['id']
        try:
            query = get_object_or_404(Cargo, id=idCargo)
            if query:
                messages.success(self.request,
                                 'El cargo ' + query.fk_clasificador_cargo_cuadro.descripcion + ' se activo correctamente.')
                query.estado = True
                query.vacante = True
                query.save()
            else:
                data['error'] = 'Ha ocurrido un error.'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


# PROCEDIMIENTO PARA DESACTIVAR CARGO.
'''Si un cuadro es desactivado, el cargo que este ocupando pasa a ser vacante'''


class desactivarCuadroView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        data = {}
        idCuadro = request.GET['id']
        try:
            query = get_object_or_404(Cuadro, id=idCuadro)
            if query:
                enableCargoComoVacante(query)
                messages.success(self.request, 'El cuadro ' + query.getFullName() + ' quedo inactivo.')
                query.estado = False
                query.save()
            else:
                data['error'] = 'Ha ocurrido un error.'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


# PROCEDIMIENTO PARA OBTENER LOS MUNICIPIOS DE UNA PROVINCIA.
class getMunicipiosView(LoginRequiredMixin, TemplateView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        codigoProvincia = clasificadorDPA.objects.get(id=request.POST['id']).codigo
        action = request.POST['action']
        try:
            if action == 'getMunicipios':
                data = [{'id': '', 'text': '------'}]
                for i in clasificadorDPA.objects.filter(codigo__startswith=codigoProvincia).exclude(
                        codigo__exact=codigoProvincia):
                    data.append({'id': i.id, 'text': i.getCodigoDescricion()})
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


# PROCEDIMIENTO PARA LISTAR NOMENCLADOR DE CARGOS.
class listarNomencladorCargosView(LoginRequiredMixin, ListView):
    template_name = 'cuadro/listar/listarNomencladorCargos.html'
    model = ClasificadorCargoCuadro

    def get_queryset(self):
        return ClasificadorCargoCuadro.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nomencladorCargos'] = self.get_queryset()
        context['titulo'] = 'Nomencladdor de Cargos'
        context['tituloPestaña'] = 'SGPC | Cuadros'
        return context


# PROCEDIMIENTO PARA CREAR NOMENCLADOR DE CARGOS.
class crearNomencladorCargosView(LoginRequiredMixin, CreateView):
    template_name = 'cuadro/crear/crearNomencladorCargos.html'
    model = ClasificadorCargoCuadro
    form_class = nomencladorCargosForm
    success_url = reverse_lazy('cuadro:listarNomencladorCargos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creacion de un Nomenclador de Cargos'
        context['tituloPestaña'] = 'SGPC | Cuadros'
        return context


# PROCEDIMIENTO PARA MODIFICAR NOMENCLADOR CARGO.
class modificarNomencladorCargosView(LoginRequiredMixin, UpdateView):
    model = ClasificadorCargoCuadro
    form_class = nomencladorCargosForm
    template_name = 'cuadro/crear/crearNomencladorCargos.html'
    success_url = reverse_lazy('cuadro:listarNomencladorCargos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edicion de un Nomenclador'
        context['tituloPestaña'] = 'SGPC | Cuadros'
        return context


# PROCEDIMIENTO PARA IMPORTAR  LOS NOMENCLADORES DE CARGOS
class importarNomencladorCargosView(LoginRequiredMixin, TemplateView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        file = request.FILES['datosNomencladorCargos']
        dataset = Dataset()
        try:
            if not file.name.endswith('xlsx'):
                data['error'] = 'El formato del documento no es valido.'
            else:
                naeImportado = dataset.load(file.read(), format='xlsx')
                for i in naeImportado:
                    nae = ClasificadorCargoCuadro(
                        i[0], i[0], i[1]
                    )
                    nae.save()
                data['exito'] = 'Los Nomencladores de cargos se han importado correctamente.'
        except Exception as e:
            data['error'] = 'Ha ocurrido un error fatal al importar. Contacte con el administrador'
        return JsonResponse(data, safe=False)


# PROCEDIMIENTO PARA LISTAR MOVIMIENTOS.
class listarMovimientosView(LoginRequiredMixin, ListView):
    template_name = 'cuadro/listar/listarMovimientos.html'
    model = Movimiento

    def get_queryset(self):
        return Movimiento.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movimientos'] = self.get_queryset()
        context['titulo'] = 'Listado de Movimientos'
        context['tituloPestaña'] = 'SGPC | Movimientos'
        return context


# PROCEDIMIENTO PARA CREAR MOVIMIENTOS.
class crearMovimientosView(LoginRequiredMixin, CreateView):
    template_name = 'cuadro/crear/crearMovimientos.html'
    model = Movimiento
    form_class = movimientoForm
    success_url = reverse_lazy('cuadro:listarMovimientos')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(self.request, 'Movimiento creado correctamente.')
            form.save()
        else:
            messages.error(self.request, form.errors)
        return redirect('cuadro:listarMovimientos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Creacion de Movimientos'
        context['tituloPestaña'] = 'SGPC | Movimientos'
        return context


# PROCEDIMIENTO PARA MODIFICAR MOVIMIENTOS.
class modificarMovimientosView(LoginRequiredMixin, UpdateView):
    model = Movimiento
    form_class = movimientoForm
    template_name = 'cuadro/crear/crearMovimientos.html'
    success_url = reverse_lazy('cuadro:listarMovimientos')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Edicion de Movimientos'
        context['tituloPestaña'] = 'SGPC | Movimientos'
        return context


# PROCEDIMIENTO PARA ELIMINAR MOVIMIENTOS.
class eliminarMovimientosView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        data = {}
        try:
            query = get_object_or_404(Movimiento, id=request.GET['id'])
            messages.success(self.request,
                             'El movimiento se ha eliminado correctamente')
            query.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

# PROCEDIMIENTO PARA VERIFICAR SI EL CUADRO A CREAR NO ESTE ACTIVO CON OTRO CARGO.
class isActivoView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        data = {}
        try:
            query = get_object_or_404(Cuadro, ci=request.GET['ci'])
            if query and query.estado == True:
                data['message'] = 'Este cuadro esta activo en otro cargo.'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
