from django.db import models
from django.forms import model_to_dict

CHOICE_CATEGORIA = (
    ('', '--------'),
    ('DS', 'Directivo Superior'),
    ('DI', 'Directivo Intermedio'),
    ('E', 'Ejecutivo')
)

CHOICE_MILITANCIA = (
    ('', '--------'),
    ('PCC', 'PCC'),
    ('UJC', 'UJC')
)
CHOICE_SEXO = (
    ('', '--------'),
    ('F', 'Femenino'),
    ('M', 'Masculino')
)

CHOICE_COLOR = (
    ('', '--------'),
    ('B', 'Blanca'),
    ('M', 'Mulata'),
    ('N', 'Negra')
)

CHOICE_NIVEL_SUBORDINACION = (
    ('', '--------'),
    ('OC', 'Oficina Central'),
    ('P', 'Provincial'),
    ('M', 'Municipal')
)

class clasificadorDPA(models.Model):
    codigo = models.IntegerField(verbose_name='Codigo', unique=True,  blank=False, null=False)
    descripcion = models.CharField(verbose_name='Descripcion', max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'Clasificador_DPA'
        verbose_name = 'Clasificador_DPA'
        verbose_name_plural = 'Clasificador_DPA'
        ordering = ['codigo']

    def getCodigoDescricion(self):
        return '{0}--{1}'.format(str(self.codigo), self.descripcion)

    def __str__(self):
        return '{0}--{1}'.format(str(self.codigo), self.descripcion)

class ClasificadorCargoCuadro(models.Model):
    codigo = models.CharField(verbose_name='Codigo', max_length=3, unique=True,  blank=False, null=False)
    descripcion = models.CharField(verbose_name='Descripcion', max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'Clasificador_Cargo_Cuadro'
        verbose_name = 'Clasificador_Cargo_Cuadro'
        verbose_name_plural = 'Clasificador_Cargos_Cuadros'
        ordering = ['codigo']

    def getCodigoDescricion(self):
        return '{0}--{1}'.format(str(self.codigo), self.descripcion)

    def __str__(self):
        return '{0}--{1}'.format(str(self.codigo), self.descripcion)

class Cargo(models.Model):
    fk_clasificador_cargo_cuadro = models.ForeignKey(ClasificadorCargoCuadro, verbose_name='Nombre del Cargo', blank=True, null=True, on_delete=models.CASCADE)
    nivel_subordinacion = models.CharField(verbose_name='Nivel de subordinacion', max_length=50, choices=CHOICE_NIVEL_SUBORDINACION)
    provincia = models.ForeignKey(clasificadorDPA, verbose_name='Provincia', blank=True, null=True, related_name='provincia', on_delete=models.CASCADE)
    municipio = models.ForeignKey(clasificadorDPA, verbose_name='Municipio', blank=True, null=True, related_name='municipio', on_delete=models.CASCADE)
    vacante = models.BooleanField(default=True)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'Cargos'
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        if self.nivel_subordinacion == 'OC':
            return '{0}--{1}'.format(str(self.fk_clasificador_cargo_cuadro.descripcion), 'OFICINA CENTRAL')
        elif self.provincia != None and self.municipio == None:
            return '{0}--{1}'.format(str(self.fk_clasificador_cargo_cuadro.descripcion), self.provincia.descripcion)
        else:
            return '{0}--{1}--{2}'.format(str(self.fk_clasificador_cargo_cuadro.descripcion), self.provincia.descripcion, self.municipio.descripcion)

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
    fk_cargo = models.ForeignKey(Cargo, verbose_name='Cargo', blank=True, null=True, on_delete=models.CASCADE)
    fk_especialidad = models.ForeignKey(Especialidad, verbose_name='Especialidad', blank=True, null=True, on_delete=models.CASCADE)
    categoria = models.CharField(verbose_name='Categoria', max_length=200, choices=CHOICE_CATEGORIA)
    nombre = models.CharField(verbose_name='Nombre', max_length=255, blank=False, null=False)
    apellidos = models.CharField(verbose_name='Apellidos', max_length=255, blank=False, null=False)
    ci = models.BigIntegerField(verbose_name='Carnet de Identidad', blank=False, null=False)
    anos_experiencia_direccion = models.PositiveIntegerField(verbose_name='Años de experiencia Direccion', blank=True, null=True)
    anos_experiencia_rama = models.PositiveIntegerField(verbose_name='Años de experiencia Rama', blank=True, null=True)
    militancia = models.CharField(verbose_name='Militancia', max_length=50, choices=CHOICE_MILITANCIA, blank=True, null=True)
    sexo = models.CharField(verbose_name='Sexo', max_length=50, choices=CHOICE_SEXO)
    color = models.CharField(verbose_name='Color', max_length=50, choices=CHOICE_COLOR)
    edad = models.PositiveIntegerField(verbose_name='Edad')
    estado = models.BooleanField(default=True)


    class Meta:
        db_table = 'Cuadros'
        verbose_name = 'Cuadro'
        verbose_name_plural = 'Cuadros'

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def getFullName(self):
        return ' {0} {1}'.format(self.nombre, self.apellidos)

    def __str__(self):
        return 'Cuadro: {0}-{1}, {2}'.format(self.nombre, self.ci, self.fk_cargo)

