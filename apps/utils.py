from apps.cuadro.models import Cargo, Cuadro


def disabledCargoComoVacante():
    cuadro = Cuadro.objects.last()
    cargo = Cargo.objects.get(id=cuadro.fk_cargo.id)
    cargo.vacante = False
    cargo.save()

def enableCargoComoVacante(cuadro):
    cargo = Cargo.objects.get(id=cuadro.fk_cargo.id)
    cargo.vacante = True
    cargo.save()


# FUNCION PARA OBTENER LOS CUADROS TENIENDO EN CUENTA LOS PERMISOS DE USUARIOS.
def getCuadros(user):
    if user.has_perm('usuario.administrador') or user.has_perm('usuario.oficinaCentral'):
        query = Cuadro.objects.all()
        return query
    elif user.has_perm('usuario.21'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=21)
        return query
    elif user.has_perm('usuario.22'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=22)
        return query
    elif user.has_perm('usuario.23'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=23)
        return query
    elif user.has_perm('usuario.24'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=24)
        return query
    elif user.has_perm('usuario.25'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=25)
        return query
    elif user.has_perm('usuario.26'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=26)
        return query
    elif user.has_perm('usuario.27'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=27)
        return query
    elif user.has_perm('usuario.28'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=28)
        return query
    elif user.has_perm('usuario.29'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=29)
        return query
    elif user.has_perm('usuario.30'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=30)
        return query
    elif user.has_perm('usuario.31'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=31)
        return query
    elif user.has_perm('usuario.32'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=32)
        return query
    elif user.has_perm('usuario.33'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=33)
        return query
    elif user.has_perm('usuario.34'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=34)
        return query
    elif user.has_perm('usuario.35'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=35)
        return query
    elif user.has_perm('usuario.40'):
        query = Cuadro.objects.filter(fk_cargo__provincia__codigo__exact=40)
        return query
