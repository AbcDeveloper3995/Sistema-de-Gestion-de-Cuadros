from django.forms import *
from apps.cuadro.models import *
from apps.usuario.models import Usuario


class cargoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['provincia'].queryset = clasificadorDPA.objects.filter(codigo__range=(21, 40))
        self.fields['municipio'].queryset = clasificadorDPA.objects.exclude(codigo__range=(21, 40))

    class Meta:
        model = Cargo
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el nombre del cargo'}),
            'nivel_subordinacion': Select(attrs={'class': 'form-control select2', 'id':'campoNivelSubordinacion'}),
            'provincia': Select(attrs={'class': 'form-control select2', 'id':'campoProvincia'}),
            'municipio': Select(attrs={'class': 'form-control select2', 'id':'campoMunicipio'}),
            'vacante': CheckboxInput(attrs={'class':'border-checkbox', 'type': 'checkbox', 'id':'vacante'}),
            'estado': CheckboxInput(attrs={'class':'border-checkbox', 'type': 'checkbox', 'id':'estadoCargo'})
        }

    def clean(self):
        cleaned = super().clean()
        nombre = cleaned['nombre']
        nivelSubordinacion = cleaned['nivel_subordinacion']
        provincia = cleaned['provincia']
        municipio = cleaned['municipio']
        if nivelSubordinacion == 'OC' and Cargo.objects.filter(nombre=nombre, nivel_subordinacion=nivelSubordinacion).exists():
            self._errors['error'] = self._errors.get('error', self.error_class())
            self._errors['error'].append('El cargo a registrar ya existe a ese nivel.')
            return cleaned
        elif nivelSubordinacion == 'P' and Cargo.objects.filter(nombre=nombre, nivel_subordinacion=nivelSubordinacion, provincia=provincia).exists():
            self._errors['error'] = self._errors.get('error', self.error_class())
            self._errors['error'].append('En la provincia ya existe ese cargo.')
            return cleaned
        elif nivelSubordinacion == 'P' and Cargo.objects.filter(nombre=nombre, nivel_subordinacion=nivelSubordinacion, provincia=provincia, municipio=municipio).exists():
            self._errors['error'] = self._errors.get('error', self.error_class())
            self._errors['error'].append('Ya existe ese cargo en el municipio.')
            return cleaned


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
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)
        self.showCargoSegunUsuario()
        self.fields['fk_especialidad'].queryset = Especialidad.objects.filter(estado=True)
        if self.instance.pk and self.instance.fk_cargo:
            del self.fields['fk_cargo']

    class Meta:
        model = Cuadro
        fields = '__all__'
        widgets = {
            'fk_cargo': Select(attrs={'class': 'form-control select2', 'id':'fk_cargo'}),
            'fk_especialidad': Select(attrs={'class': 'form-control select2', 'id': 'fk_especialidad'}),
            'categoria': Select(attrs={'class': 'form-control select2'}),
            'nombre': TextInput(attrs={'class':'form-control','placeholder':'Ingrese un nombre'}),
            'apellidos': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese apellidos'}),
            'ci': NumberInput(attrs={'class':'form-control','id':'campoCI','placeholder':'Ingrese carnet de identidad'}),
            'anos_experiencia_direccion': NumberInput(attrs={'class': 'form-control styleInput', 'id': 'ci',
                                     'placeholder': 'Ingrese cantidad de años en direccion'}),
            'anos_experiencia_rama': NumberInput(attrs={'class': 'form-control styleInput', 'id': 'ci',
                                     'placeholder': 'Ingrese cantidad de años en la rama'}),
            'militancia': Select(attrs={'class': 'form-control select2'}),
            'sexo': Select(attrs={'class': 'form-control select2'}),
            'color': Select(attrs={'class': 'form-control select2'}),
            'edad': NumberInput(attrs={'class': 'form-control styleInput', 'id': 'campoEdad', 'readonly':True,}),
            'estado': CheckboxInput(attrs={'class': 'border-checkbox', 'type': 'checkbox', 'id': 'estadoCuadro'})

        }

    def showCargoSegunUsuario(self):
        if self.request.user.has_perm('usuario.administrador'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(estado=True)
        elif self.request.user.has_perm('usuario.oficinaCentral'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(nivel_subordinacion__exact='OC', estado=True)
        elif self.request.user.has_perm('usuario.21'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(provincia__codigo__exact=21, estado=True)
        elif self.request.user.has_perm('usuario.22'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(provincia__codigo__exact=22, estado=True)
        elif self.request.user.has_perm('usuario.23'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(provincia__codigo__exact=23, estado=True)
        elif self.request.user.has_perm('usuario.24'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(provincia__codigo__exact=24, estado=True)
        elif self.request.user.has_perm('usuario.25'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(provincia__codigo__exact=25, estado=True)
        elif self.request.user.has_perm('usuario.26'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(provincia__codigo__exact=26, estado=True)
        elif self.request.user.has_perm('usuario.27'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(provincia__codigo__exact=27, estado=True)
        elif self.request.user.has_perm('usuario.28'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(provincia__codigo__exact=28, estado=True)
        elif self.request.user.has_perm('usuario.29'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(provincia__codigo__exact=29, estado=True)
        elif self.request.user.has_perm('usuario.30'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(provincia__codigo__exact=30, estado=True)
        elif self.request.user.has_perm('usuario.31'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(provincia__codigo__exact=31, estado=True)
        elif self.request.user.has_perm('usuario.32'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(provincia__codigo__exact=32, estado=True)
        elif self.request.user.has_perm('usuario.33'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(provincia__codigo__exact=33, estado=True)
        elif self.request.user.has_perm('usuario.34'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(provincia__codigo__exact=34, estado=True)
        elif self.request.user.has_perm('usuario.35'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(provincia__codigo__exact=35, estado=True)
        elif self.request.user.has_perm('usuario.40'):
            self.fields['fk_cargo'].queryset = Cargo.objects.filter(provincia__codigo__exact=40, estado=True)