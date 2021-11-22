from django.contrib.auth.models import Group
from django.forms import *

from apps.usuario.models import Usuario


class usuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['groups'].queryset = Group.objects.all().order_by('id')


    class Meta:
        model = Usuario
        fields = ['name', 'last_name', 'username', 'password', 'email', 'image', 'groups']
        exclude = [ 'user_permission', 'last_login', 'date_joined', 'is_staff', 'is_superuser']
        widgets = {
            'name': TextInput(attrs={'class':'form-control',
                                       'placeholder':'Ingrese un nombre'}),
            'last_name': TextInput(attrs={'class':'form-control',
                                       'placeholder':'Ingrese los apellidos'}),
            'username': TextInput(attrs={'class':'form-control',
                                       'placeholder':'Ingrese un nombre de usuario '}),
            'password': PasswordInput(render_value=True, attrs={'class':'form-control',
                                       'placeholder':'Ingrese una contraseña'}),
            'email': EmailInput(attrs={'class':'form-control',
                                       'placeholder':'Ingrese una direcion de correo'}),

            'groups': SelectMultiple(attrs={'class': 'form-control select2'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                grupos = self.cleaned_data['groups']
                password = self.cleaned_data['password']
                usuario = form.save(commit=False)
                if usuario.pk == None:
                    usuario.set_password(password)
                else:
                    usuario = Usuario.objects.get(pk=usuario.pk)
                    if usuario.password != password:
                        usuario.set_password(password)
                usuario.save()
                usuario.groups.clear()
                for grupo in grupos:
                    usuario.groups.add(grupo)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class usuarioProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Usuario
        fields = ['name', 'last_name', 'username', 'password', 'email', 'image']
        exclude = [ 'user_permission', 'last_login', 'date_joined', 'is_staff', 'is_superuser', 'groups']
        widgets = {
            'name': TextInput(attrs={'class':'form-control',
                                       'placeholder':'Ingrese su nombre'}),
            'last_name': TextInput(attrs={'class':'form-control',
                                       'placeholder':'Ingrese sus apellidos'}),
            'username': TextInput(attrs={'class':'form-control',
                                       'placeholder':'Ingrese un nombre de usuario'}),
            'password': PasswordInput(render_value=True, attrs={'class':'form-control',
                                       'placeholder':'Ingrese su contraseña'}),
            'email': EmailInput(attrs={'class':'form-control',
                                       'placeholder':'Ingrese su direccion de correo'}),
            'groups': SelectMultiple(attrs={'class':'form-control select2'}),
        }
