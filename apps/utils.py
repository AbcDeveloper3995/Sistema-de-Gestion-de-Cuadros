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