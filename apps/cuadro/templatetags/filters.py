from django import template

from apps.cuadro.models import *

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

