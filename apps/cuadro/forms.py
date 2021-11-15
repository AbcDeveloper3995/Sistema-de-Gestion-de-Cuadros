from django.forms import *
from apps.cuadro.models import *


class cargoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['provincia'].queryset = clasificadorDPA.objects.filter(codigo__range=(21, 40))
        self.fields['municipio'].queryset = clasificadorDPA.objects.exclude(codigo__range=(21, 40))

    class Meta:
        model = Cargo
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'class':'form-control styleInput',
                                       'placeholder':'Ingrese el nombre del cargo'}),
            'nivel_subordinacion': Select(attrs={'class': 'form-control select2'}),
            'provincia': Select(attrs={'class': 'form-control select2'}),
            'municipio': Select(attrs={'class': 'form-control select2'}),
            'vacante': CheckboxInput(attrs={'class':'border-checkbox', 'type': 'checkbox', 'id':'vacante'}),
            'estado': CheckboxInput(attrs={'class':'border-checkbox', 'type': 'checkbox', 'id':'estadoCargo'})
        }


class especialidadForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Especialidad
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control styleInput',
                                       'placeholder': 'Ingrese el nombre de la especialidad'}),
            'estado': CheckboxInput(attrs={'class': 'border-checkbox', 'type': 'checkbox', 'id':'estadoEspecialidad'})
        }

class cuadroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fk_cargo'].queryset = Cargo.objects.filter(vacante=True, estado=True)
        self.fields['fk_especialidad'].queryset = Especialidad.objects.filter(estado=True)

    class Meta:
        model = Cuadro
        fields = '__all__'
        widgets = {
            'fk_cargo': Select(
                attrs={'class': 'form-control select2', 'id': 'fk_cargo'}),
            'fk_especialidad': Select(
                attrs={'class': 'form-control select2', 'id': 'fk_especialidad'}),
            'categoria': Select(attrs={'class': 'form-control select2'}),
            'nombre': TextInput(attrs={'class':'form-control styleInput',
                                       'placeholder':'Ingrese un nombre'}),
            'apellidos': TextInput(attrs={'class': 'form-control styleInput',
                                       'placeholder': 'Ingrese apellidos'}),
            'ci': NumberInput(attrs={'class':'form-control styleInput','id':'ci',
                                       'placeholder':'Ingrese carnet de identidad'}),
            'anos_experiencia_direccion': NumberInput(attrs={'class': 'form-control styleInput', 'id': 'ci',
                                     'placeholder': 'Ingrese cantidad de años en direccion'}),
            'anos_experiencia_rama': NumberInput(attrs={'class': 'form-control styleInput', 'id': 'ci',
                                     'placeholder': 'Ingrese cantidad de años en la rama'}),
            'militancia': Select(attrs={'class': 'form-control select2'}),
            'sexo': Select(attrs={'class': 'form-control select2'}),
            'color': Select(attrs={'class': 'form-control select2'}),
            'edad': NumberInput(attrs={'class': 'form-control styleInput', 'id': 'ci',
                                                        'placeholder': 'Ingrese la edad'}),

        }