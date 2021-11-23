from django.urls import path
from apps.cuadro.views import *

app_name = 'cuadro'

urlpatterns = [
    # CUADRO
    path('listarCuadro', listarCuadroView.as_view(), name='listarCuadro'),
    path('crearCuadro/', crearCuadroView.as_view(), name='crearCuadro'),
    path('modificarCuadro/<int:pk>/', modificarCuadroView.as_view(), name='modificarCuadro'),
    path('eliminarCuadro/<int:pk>/', eliminarCuadroView.as_view(), name='eliminarCuadro'),
    path('eliminarTodos/', eliminarCuadroAllView.as_view(), name='eliminarTodos'),
    path('isVacante/', isVacanteView.as_view(), name='isVacante'),
    path('desactivarCuadro/<int:pk>/', desactivarCuadroView.as_view(), name='desactivarCuadro'),
    path('getMunicipios/', getMunicipiosView.as_view(), name='getMunicipios'),

# CARGO
    path('listarCargo', listarCargoView.as_view(), name='listarCargo'),
    path('crearCargo/', crearCargoView.as_view(), name='crearCargo'),
    path('modificarCargo/<int:pk>/', modificarCargoView.as_view(), name='modificarCargo'),
    path('eliminarCargo/<int:pk>/', eliminarCargoView.as_view(), name='eliminarCargo'),
    path('desactivarCargo/<int:pk>/', desactivarCargoView.as_view(), name='desactivarCargo'),

# ESPECIALIDAD
    path('listarEspecialidad', listarEspecialidadView.as_view(), name='listarEspecialidad'),
    path('crearEspecialidad/', crearEspecialidadView.as_view(), name='crearEspecialidad'),
    path('modificarEspecialidad/<int:pk>/', modificarEspecialidadView.as_view(), name='modificarEspecialidad'),
    path('eliminarEspecialidad/<int:pk>/', eliminarEspecialidadView.as_view(), name='eliminarEspecialidad'),
]
