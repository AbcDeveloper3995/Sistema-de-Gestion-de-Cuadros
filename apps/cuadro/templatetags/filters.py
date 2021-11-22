from django import template

from apps.cuadro.models import *
from apps.usuario.models import Usuario

register = template.Library()


# FILTRO PARA OBTENER EL TOTAL DE CUADROS.
@register.filter(name='totalCuadro')
def totalCuadro(user):
    query = Cuadro.objects.all().count()
    return query


# FILTRO PARA OBTENER EL TOTAL DE ESPECIALIDADES.
@register.filter(name='totalEspecialidad')
def totalEspecialidad(user):
    query = Especialidad.objects.all().count()
    return query


# FILTRO PARA OBTENER EL TOTAL DE CARGOS.
@register.filter(name='totalCargo')
def totalCargo(user):
    query = Cargo.objects.all().count()
    return query


# FILTRO PARA SABER SI EXISTEN CARGOS VACANTES.
@register.filter(name='existenVacantes')
def existenVacantes(user):
    query = Cargo.objects.filter(vacante=True).count()
    if query == 0:
        return False
    return True

# FILTRO PARA OBTENER EL TOTAL DE USUARIOS.
@register.filter(name='totalUsuarios')
def totalUsuarios(user):
    query = Usuario.objects.all().count()
    return query

