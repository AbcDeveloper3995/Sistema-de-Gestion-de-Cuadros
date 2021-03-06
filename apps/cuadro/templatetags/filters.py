import datetime

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


# FILTRO PARA OBTENER EL TOTAL DE USUARIOS.
@register.filter(name='totalUsuarios')
def totalUsuarios(user):
    query = Usuario.objects.all().count()
    return query

# FILTRO PARA OBTENER EL TIEMPO EN CARGO DE UN CUADRO.

@register.filter(name='tiempoEnCargo')
def tiempoEnCargo(Cuadro):
    fechaActual = datetime.datetime.today().date()
    if Cuadro.fecha_baja == None:
        tiempoEnCargo = fechaActual - Cuadro.fecha_alta
        return calcularTiempo(Cuadro, tiempoEnCargo)
    else:
        tiempoEnCargo = Cuadro.fecha_baja - Cuadro.fecha_alta
        return calcularTiempo(Cuadro, tiempoEnCargo)


def calcularTiempo(Cuadro, tiempo):
    anoEnCargo = tiempo.days // 365
    mesesEnCargo = tiempo.days % 365 // 30
    Cuadro.tiempo_en_cargo = anoEnCargo
    Cuadro.save()
    return '{} años y {} meses'.format(anoEnCargo, mesesEnCargo)


