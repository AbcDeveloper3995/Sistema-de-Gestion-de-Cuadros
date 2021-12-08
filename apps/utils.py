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



''' FUNCIONES AUXILIARES PARA OBTENER LA DATA DE LOS GRAFICOS SEGUN EL USUARIO EN SESION'''

# FUNCIONES PARA OBTENER LA DATA A MOSTRAR EN EL GRAFICO DE CANTIDAD DE CARGOS POR GENERO
def cantidadPorGenero(user):
    if user.has_perm('usuario.administrador') or user.has_perm('usuario.oficinaCentral'):
        data = []
        try:
            cantMasculinos = Cuadro.objects.filter(sexo='M').count()
            cantFemeninos = Cuadro.objects.filter(sexo='F').count()
            data.append(cantMasculinos)
            data.append(cantFemeninos)
        except:
            pass
        return data
    elif user.has_perm('usuario.21'):
        return getQuerysetDeCantidadPorGenero(21)
    elif user.has_perm('usuario.22'):
        return getQuerysetDeCantidadPorGenero(22)
    elif user.has_perm('usuario.23'):
        return getQuerysetDeCantidadPorGenero(23)
    elif user.has_perm('usuario.24'):
        return getQuerysetDeCantidadPorGenero(24)
    elif user.has_perm('usuario.25'):
        return getQuerysetDeCantidadPorGenero(25)
    elif user.has_perm('usuario.26'):
        return getQuerysetDeCantidadPorGenero(26)
    elif user.has_perm('usuario.27'):
        return getQuerysetDeCantidadPorGenero(27)
    elif user.has_perm('usuario.28'):
        return getQuerysetDeCantidadPorGenero(28)
    elif user.has_perm('usuario.29'):
        return getQuerysetDeCantidadPorGenero(29)
    elif user.has_perm('usuario.30'):
        return getQuerysetDeCantidadPorGenero(30)
    elif user.has_perm('usuario.31'):
        return getQuerysetDeCantidadPorGenero(31)
    elif user.has_perm('usuario.32'):
        return getQuerysetDeCantidadPorGenero(32)
    elif user.has_perm('usuario.33'):
        return getQuerysetDeCantidadPorGenero(33)
    elif user.has_perm('usuario.34'):
        return getQuerysetDeCantidadPorGenero(34)
    elif user.has_perm('usuario.35'):
        return getQuerysetDeCantidadPorGenero(35)
    elif user.has_perm('usuario.40'):
        return getQuerysetDeCantidadPorGenero(40)

def getQuerysetDeCantidadPorGenero(codigoDPA):
    data = []
    try:
        cantMasculinos = Cuadro.objects.filter(sexo='M', fk_cargo__provincia__codigo__exact=codigoDPA).count()
        cantFemeninos = Cuadro.objects.filter(sexo='F', fk_cargo__provincia__codigo__exact=codigoDPA).count()
        data.append(cantMasculinos)
        data.append(cantFemeninos)
    except:
        pass
    return data


# FUNCIONES PARA OBTENER LA DATA A MOSTRAR EN EL GRAFICO DE CANTIDAD DE CARGOS POR CATEGORIA
def cantidadPorCategoria(user):
    if user.has_perm('usuario.administrador') or user.has_perm('usuario.oficinaCentral'):
        data = []
        try:
            cantDirectivoSuerior = Cuadro.objects.filter(categoria__exact='DS').count()
            cantDirectivoIntermedio = Cuadro.objects.filter(categoria__exact='DI').count()
            cantEjecutivo = Cuadro.objects.filter(categoria__exact='E').count()
            data.append(cantDirectivoSuerior)
            data.append(cantDirectivoIntermedio)
            data.append(cantEjecutivo)
        except:
            pass
        return data
    elif user.has_perm('usuario.21'):
        return getQuerysetDeCantidadPorCategoria(21)
    elif user.has_perm('usuario.22'):
        return getQuerysetDeCantidadPorCategoria(22)
    elif user.has_perm('usuario.23'):
        return getQuerysetDeCantidadPorCategoria(23)
    elif user.has_perm('usuario.24'):
        return getQuerysetDeCantidadPorCategoria(24)
    elif user.has_perm('usuario.25'):
        return getQuerysetDeCantidadPorCategoria(25)
    elif user.has_perm('usuario.26'):
        return getQuerysetDeCantidadPorCategoria(26)
    elif user.has_perm('usuario.27'):
        return getQuerysetDeCantidadPorCategoria(27)
    elif user.has_perm('usuario.28'):
        return getQuerysetDeCantidadPorCategoria(28)
    elif user.has_perm('usuario.29'):
        return getQuerysetDeCantidadPorCategoria(29)
    elif user.has_perm('usuario.30'):
        return getQuerysetDeCantidadPorCategoria(30)
    elif user.has_perm('usuario.31'):
        return getQuerysetDeCantidadPorCategoria(31)
    elif user.has_perm('usuario.32'):
        return getQuerysetDeCantidadPorCategoria(32)
    elif user.has_perm('usuario.33'):
        return getQuerysetDeCantidadPorCategoria(33)
    elif user.has_perm('usuario.34'):
        return getQuerysetDeCantidadPorCategoria(34)
    elif user.has_perm('usuario.35'):
        return getQuerysetDeCantidadPorCategoria(35)
    elif user.has_perm('usuario.40'):
        return getQuerysetDeCantidadPorCategoria(40)

def getQuerysetDeCantidadPorCategoria(codigoDPA):
    data = []
    try:
        cantDirectivoSuerior = Cuadro.objects.filter(categoria__exact='DS', fk_cargo__provincia__codigo__exact=codigoDPA).count()
        cantDirectivoIntermedio = Cuadro.objects.filter(categoria__exact='DI', fk_cargo__provincia__codigo__exact=codigoDPA).count()
        cantEjecutivo = Cuadro.objects.filter(categoria__exact='E', fk_cargo__provincia__codigo__exact=codigoDPA).count()
        data.append(cantDirectivoSuerior)
        data.append(cantDirectivoIntermedio)
        data.append(cantEjecutivo)
    except:
        pass
    return data


# FUNCIONES PARA OBTENER LA DATA A MOSTRAR EN EL GRAFICO DE PORCENTAJE SEGUN LA MILITANCIA
def porcentajeSegunMilitancia(user):
    if user.has_perm('usuario.administrador') or user.has_perm('usuario.oficinaCentral'):
        data = []
        try:
            cantMilitantesPCC = Cuadro.objects.filter(militancia='PCC').count()
            cantMilitantesUJC = Cuadro.objects.filter(militancia='UJC').count()
            cantNoMilitantes = Cuadro.objects.filter(militancia=None).count()
            data = [{'name': 'PCC', 'y': cantMilitantesPCC}, {'name': 'UJC', 'y': cantMilitantesUJC}, {'name': 'No militantes', 'y': cantNoMilitantes}]
        except:
            pass
        return data
    elif user.has_perm('usuario.21'):
        return getQuerysetDePorcentajeSegunMilitancia(21)
    elif user.has_perm('usuario.22'):
        return getQuerysetDePorcentajeSegunMilitancia(22)
    elif user.has_perm('usuario.23'):
        return getQuerysetDePorcentajeSegunMilitancia(23)
    elif user.has_perm('usuario.24'):
        return getQuerysetDePorcentajeSegunMilitancia(24)
    elif user.has_perm('usuario.25'):
        return getQuerysetDePorcentajeSegunMilitancia(25)
    elif user.has_perm('usuario.26'):
        return getQuerysetDePorcentajeSegunMilitancia(26)
    elif user.has_perm('usuario.27'):
        return getQuerysetDePorcentajeSegunMilitancia(27)
    elif user.has_perm('usuario.28'):
        return getQuerysetDePorcentajeSegunMilitancia(28)
    elif user.has_perm('usuario.29'):
        return getQuerysetDePorcentajeSegunMilitancia(29)
    elif user.has_perm('usuario.30'):
        return getQuerysetDePorcentajeSegunMilitancia(30)
    elif user.has_perm('usuario.31'):
        return getQuerysetDePorcentajeSegunMilitancia(31)
    elif user.has_perm('usuario.32'):
        return getQuerysetDePorcentajeSegunMilitancia(32)
    elif user.has_perm('usuario.33'):
        return getQuerysetDePorcentajeSegunMilitancia(33)
    elif user.has_perm('usuario.34'):
        return getQuerysetDePorcentajeSegunMilitancia(34)
    elif user.has_perm('usuario.35'):
        return getQuerysetDePorcentajeSegunMilitancia(35)
    elif user.has_perm('usuario.40'):
        return getQuerysetDePorcentajeSegunMilitancia(40)

def getQuerysetDePorcentajeSegunMilitancia(codigoDPA):
    data = []
    try:
        cantMilitantesPCC = Cuadro.objects.filter(militancia='PCC', fk_cargo__provincia__codigo__exact=codigoDPA).count()
        cantMilitantesUJC = Cuadro.objects.filter(militancia='UJC', fk_cargo__provincia__codigo__exact=codigoDPA).count()
        cantNoMilitantes = Cuadro.objects.filter(militancia=None, fk_cargo__provincia__codigo__exact=codigoDPA).count()
        data = [{'name': 'PCC', 'y': cantMilitantesPCC}, {'name': 'UJC', 'y': cantMilitantesUJC},{'name': 'No militantes', 'y': cantNoMilitantes}]
    except:
        pass
    return data


# FUNCIONES PARA OBTENER LA DATA A MOSTRAR EN EL GRAFICO DE CANTIDAD DE CARGOS POR COLOR
def cantidadPorColor(user):
    if user.has_perm('usuario.administrador') or user.has_perm('usuario.oficinaCentral'):
        data = []
        try:
            cantBlancos = Cuadro.objects.filter(color='B').count()
            cantMestizos = Cuadro.objects.filter(color='M').count()
            cantNegros = Cuadro.objects.filter(color='N').count()
            data.append(cantBlancos)
            data.append(cantMestizos)
            data.append(cantNegros)
        except:
            pass
        return data
    elif user.has_perm('usuario.21'):
        return getQuerysetDeCantidadPorColor(21)
    elif user.has_perm('usuario.22'):
        return getQuerysetDeCantidadPorColor(22)
    elif user.has_perm('usuario.23'):
        return getQuerysetDeCantidadPorColor(23)
    elif user.has_perm('usuario.24'):
        return getQuerysetDeCantidadPorColor(24)
    elif user.has_perm('usuario.25'):
        return getQuerysetDeCantidadPorColor(25)
    elif user.has_perm('usuario.26'):
        return getQuerysetDeCantidadPorColor(26)
    elif user.has_perm('usuario.27'):
        return getQuerysetDeCantidadPorColor(27)
    elif user.has_perm('usuario.28'):
        return getQuerysetDeCantidadPorColor(28)
    elif user.has_perm('usuario.29'):
        return getQuerysetDeCantidadPorColor(29)
    elif user.has_perm('usuario.30'):
        return getQuerysetDeCantidadPorColor(30)
    elif user.has_perm('usuario.31'):
        return getQuerysetDeCantidadPorColor(31)
    elif user.has_perm('usuario.32'):
        return getQuerysetDeCantidadPorColor(32)
    elif user.has_perm('usuario.33'):
        return getQuerysetDeCantidadPorColor(33)
    elif user.has_perm('usuario.34'):
        return getQuerysetDeCantidadPorColor(34)
    elif user.has_perm('usuario.35'):
        return getQuerysetDeCantidadPorColor(35)
    elif user.has_perm('usuario.40'):
        return getQuerysetDeCantidadPorColor(40)

def getQuerysetDeCantidadPorColor(codigoDPA):
    data = []
    try:
        cantBlancos = Cuadro.objects.filter(color='B', fk_cargo__provincia__codigo__exact=codigoDPA).count()
        cantMestizos = Cuadro.objects.filter(color='M', fk_cargo__provincia__codigo__exact=codigoDPA).count()
        cantNegros = Cuadro.objects.filter(color='N', fk_cargo__provincia__codigo__exact=codigoDPA).count()
        data.append(cantBlancos)
        data.append(cantMestizos)
        data.append(cantNegros)
    except:
        pass
    return data


# FUNCIONES PARA OBTENER LA DATA A MOSTRAR EN EL GRAFICO DE CANTIDAD DE CARGOS POR EDAD
def cantidadPorEdad(user):
    if user.has_perm('usuario.administrador') or user.has_perm('usuario.oficinaCentral'):
        data = []
        try:
            cuadrosMenorA40 = Cuadro.objects.filter(edad__lte=40).count()
            cuadrosDe41A50 = Cuadro.objects.filter(edad__range=(41, 50)).count()
            cuadrosDe51A60 = Cuadro.objects.filter(edad__range=(51, 60)).count()
            cuadrosDe61A70 = Cuadro.objects.filter(edad__range=(61, 70)).count()
            cuadrosMayorA70 = Cuadro.objects.filter(edad__gte=70).count()
            data.append(cuadrosMenorA40)
            data.append(cuadrosDe41A50)
            data.append(cuadrosDe51A60)
            data.append(cuadrosDe61A70)
            data.append(cuadrosMayorA70)
        except:
            pass
        return data
    elif user.has_perm('usuario.21'):
        return getQuerysetDeCantidadPorEdad(21)
    elif user.has_perm('usuario.22'):
        return getQuerysetDeCantidadPorEdad(22)
    elif user.has_perm('usuario.23'):
        return getQuerysetDeCantidadPorEdad(23)
    elif user.has_perm('usuario.24'):
        return getQuerysetDeCantidadPorEdad(24)
    elif user.has_perm('usuario.25'):
        return getQuerysetDeCantidadPorEdad(25)
    elif user.has_perm('usuario.26'):
        return getQuerysetDeCantidadPorEdad(26)
    elif user.has_perm('usuario.27'):
        return getQuerysetDeCantidadPorEdad(27)
    elif user.has_perm('usuario.28'):
        return getQuerysetDeCantidadPorEdad(28)
    elif user.has_perm('usuario.29'):
        return getQuerysetDeCantidadPorEdad(29)
    elif user.has_perm('usuario.30'):
        return getQuerysetDeCantidadPorEdad(30)
    elif user.has_perm('usuario.31'):
        return getQuerysetDeCantidadPorEdad(31)
    elif user.has_perm('usuario.32'):
        return getQuerysetDeCantidadPorEdad(32)
    elif user.has_perm('usuario.33'):
        return getQuerysetDeCantidadPorEdad(33)
    elif user.has_perm('usuario.34'):
        return getQuerysetDeCantidadPorEdad(34)
    elif user.has_perm('usuario.35'):
        return getQuerysetDeCantidadPorEdad(35)
    elif user.has_perm('usuario.40'):
        return getQuerysetDeCantidadPorEdad(40)

def getQuerysetDeCantidadPorEdad(codigoDPA):
    data = []
    try:
        cuadrosMenorA40 = Cuadro.objects.filter(edad__lte=40, fk_cargo__provincia__codigo__exact=codigoDPA).count()
        cuadrosDe41A50 = Cuadro.objects.filter(edad__range=(41, 50), fk_cargo__provincia__codigo__exact=codigoDPA).count()
        cuadrosDe51A60 = Cuadro.objects.filter(edad__range=(51, 60), fk_cargo__provincia__codigo__exact=codigoDPA).count()
        cuadrosDe61A70 = Cuadro.objects.filter(edad__range=(61, 70), fk_cargo__provincia__codigo__exact=codigoDPA).count()
        cuadrosMayorA70 = Cuadro.objects.filter(edad__gte=70, fk_cargo__provincia__codigo__exact=codigoDPA).count()
        data.append(cuadrosMenorA40)
        data.append(cuadrosDe41A50)
        data.append(cuadrosDe51A60)
        data.append(cuadrosDe61A70)
        data.append(cuadrosMayorA70)
    except:
        pass
    return data
