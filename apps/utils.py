from apps.cuadro.models import Cargo, Cuadro


def disabledCargoComoVacante():
    try:
        cuadro = Cuadro.objects.last()
        cargo = Cargo.objects.get(id=cuadro.fk_cargo.id)
        cargo.vacante = False
        cargo.save()
        return True
    except:
        return False

def enableCargoComoVacante(cuadro):
    try:
        cargo = Cargo.objects.get(id=cuadro.fk_cargo.id)
        if cargo.estado == True:
            cargo.vacante = True
            cargo.save()
            return True
    except:
        return False


# FUNCION PARA OBTENER LOS CUADROS TENIENDO EN CUENTA LOS PERMISOS DE USUARIOS.
def getCuadros(user):
    if user.has_perm('usuario.administrador') or user.has_perm('usuario.oficinaCentral'):
        query = Cuadro.objects.all().order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
    elif user.has_perm('usuario.21'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=21).order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
    elif user.has_perm('usuario.22'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=22).order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
    elif user.has_perm('usuario.23'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=23).order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
    elif user.has_perm('usuario.24'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=24).order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
    elif user.has_perm('usuario.25'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=25).order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
    elif user.has_perm('usuario.26'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=26).order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
    elif user.has_perm('usuario.27'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=27).order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
    elif user.has_perm('usuario.28'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=28).order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
    elif user.has_perm('usuario.29'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=29).order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
    elif user.has_perm('usuario.30'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=30).order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
    elif user.has_perm('usuario.31'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=31).order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
    elif user.has_perm('usuario.32'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=32).order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
    elif user.has_perm('usuario.33'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=33).order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
    elif user.has_perm('usuario.34'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=34).order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
    elif user.has_perm('usuario.35'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=35).order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
    elif user.has_perm('usuario.40'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=40).order_by('fk_cargo__fk_clasificador_cargo_cuadro__codigo')
        return query
