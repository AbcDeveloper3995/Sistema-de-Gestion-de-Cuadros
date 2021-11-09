from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from SGPC.settings import MEDIA_URL, STATIC_URL


class UsuarioManager(BaseUserManager):

    def _create_user(self, username, email, name, last_name, password, is_staff, is_superuser, **extra_fields):
        usuario =self.model(
            username=username,
            email=email,
            name=name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(using=self.db)
        return usuario

    def create_user(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name, last_name, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, True, True, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='Nombre de usuario', max_length=255, unique=True)
    email = models.EmailField(verbose_name='Correo', max_length=255, unique=True)
    name = models.CharField(verbose_name='Nombre', max_length=255, blank=True, null=True)
    last_name = models.CharField(verbose_name='Apellidos', max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='user/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UsuarioManager()

    class Meta:
        db_table = 'Usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']

    def get_img(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'propios/img/empty.png')

    def natural_key(self):
        return (self.username)

    def __str__(self):
        return f'{self.name}{self.last_name}'
