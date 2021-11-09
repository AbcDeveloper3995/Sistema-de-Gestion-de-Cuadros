from django.db import models
from django.forms import model_to_dict

CHOICE_CATEGORIA = (
    ('DS', 'Directivo Superior'),
    ('DI', 'Directivo Intermedio'),
    ('E', 'Ejecutivo')
)

CHOICE_MILITANCIA = (
    ('PCC', 'PCC'),
    ('UJC', 'UJC')
)
CHOICE_SEXO = (
    ('F', 'Femenino'),
    ('M', 'Masculino')
)

CHOICE_COLOR = (
    ('B', 'Blanca'),
    ('M', 'Mulata'),
    ('N', 'Negra')
)

class Cargo(models.Model):
    nombre = models.CharField(verbose_name='Nombre del cargo', max_length=255, unique=True, blank=False, null=False)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'Cargos'
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return str(self.nombre)

class Especialidad(models.Model):
    nombre = models.CharField(verbose_name='Nombre de la especialidad', max_length=255, unique=True, blank=False, null=False)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'Especialidad'
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return str(self.nombre)

class Cuadro(models.Model):
    fk_cargo = models.OneToOneField(Cargo, verbose_name='Cargo', blank=True, null=True, on_delete=models.CASCADE)
    fk_especialidad = models.ForeignKey(Especialidad, verbose_name='Especialidad', blank=True, null=True, on_delete=models.CASCADE)
    categoria = models.CharField(verbose_name='Categoria', max_length=200, choices=CHOICE_CATEGORIA)
    nombre = models.CharField(verbose_name='Nombre', max_length=255, blank=True, null=True)
    ci = models.PositiveIntegerField(verbose_name='Carnet de Identidad', unique=True)
    anos_experiencia_direccion = models.PositiveIntegerField(verbose_name='Años de experiencia Direccion')
    anos_experiencia_rama = models.PositiveIntegerField(verbose_name='Años de experiencia Rama')
    militancia = models.CharField(verbose_name='Militancia', max_length=50, choices=CHOICE_MILITANCIA)
    sexo = models.CharField(verbose_name='Sexo', max_length=50, choices=CHOICE_SEXO)
    color = models.CharField(verbose_name='Color', max_length=50, choices=CHOICE_COLOR)
    edad = models.PositiveIntegerField(verbose_name='Edad')


    class Meta:
        db_table = 'Cuadros'
        verbose_name = 'Cuadro'
        verbose_name_plural = 'Cuadros'

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return 'Cuadro: {0}-{1}, {2}'.format(self.nombre, self.ci, self.fk_cargo)

