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
    ('UAS', 'Unidad de Aseguramiento y Servicios'),
    ('P', 'Provincial'),
    ('M', 'Municipal')
)

CHOICE_CATEGORIA_CIENTIFICA = (
    ('', '--------'),
    ('Dr.Cs', 'Doctor en Ciencias'),
    ('MC.s', 'Máster en Ciencias')
)

CHOICE_MODALIDAD_PROMOCION = (
    ('11', 'Que procede de la reserva'),
    ('12', 'Mujeres promovidas en el periodo'),
    ('13', 'Negros y mulatos promovidos en el periodo')
)

CHOICE_MODALIDAD_SUSTITUCION = (
    ('101', 'Ubicado en otro cargo de inferior jerarquia y diferente categoria ocupacional'),
    ('102', 'Cese de su relacion de trabajo')
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

class Movimiento(models.Model):
    codigo = models.IntegerField(verbose_name='Codigo', unique=True,  blank=False, null=False)
    descripcion = models.CharField(verbose_name='Descripcion', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Movimiento'
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'
        ordering = ['codigo']

    def __str__(self):
        return '{0}--{1}'.format(str(self.codigo), self.descripcion)

class ModalidadPromocion(models.Model):
    codigo = models.IntegerField(verbose_name='Codigo', unique=True,  blank=False, null=False)
    descripcion = models.CharField(verbose_name='Descripcion', max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'Modalidad Promocion'
        verbose_name = 'Modalidad Promocion'
        verbose_name_plural = 'Modalidad Promocion'
        ordering = ['codigo']

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
    observaciones = models.CharField(verbose_name='Observaciones', max_length=255, blank=True, null=True)
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
        elif self.nivel_subordinacion == 'UAS':
            return '{0}--{1}'.format(str(self.fk_clasificador_cargo_cuadro.descripcion), 'Unidad de Aseguramiento y Servicios')
        elif self.provincia != None and self.municipio == None:
            return '{0}--{1}'.format(str(self.fk_clasificador_cargo_cuadro.descripcion), self.provincia.descripcion)
        else:
            return '{0}--{1}--{2}'.format(str(self.fk_clasificador_cargo_cuadro.descripcion), self.provincia.descripcion, self.municipio.descripcion)

class Especialidad(models.Model):
    codigo = models.CharField(verbose_name='Codigo', max_length=6, unique=True,  blank=True, null=True)
    descripcion = models.CharField(verbose_name='Descripcion', max_length=150, blank=True, null=True)
    nivel = models.CharField(verbose_name='Nivel Escolar', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Especialidad'
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return '{0}--{1}'.format(str(self.codigo), self.descripcion)


class Cuadro(models.Model):
    fk_cargo = models.ForeignKey(Cargo, verbose_name='Cargo', blank=True, null=True, on_delete=models.CASCADE)
    fk_especialidad = models.ForeignKey(Especialidad, verbose_name='Especialidad', blank=True, null=True, on_delete=models.CASCADE)
    fk_movimiento = models.ForeignKey(Movimiento, verbose_name='Movimiento', blank=True, null=True, on_delete=models.CASCADE)
    categoria = models.CharField(verbose_name='Categoria', max_length=50, blank=True, null=True, choices=CHOICE_CATEGORIA)
    escolaridad = models.CharField(verbose_name='Escolaridad', max_length=20, blank=True, null=True)
    categoria_cientifica = models.CharField(verbose_name='Categoria Cientifica', max_length=20, blank=True, null=True, choices=CHOICE_CATEGORIA_CIENTIFICA)
    nombre = models.CharField(verbose_name='Nombre', max_length=255, blank=False, null=False)
    apellidos = models.CharField(verbose_name='Apellidos', max_length=255, blank=False, null=False)
    ci = models.BigIntegerField(verbose_name='Carnet de Identidad', blank=False, null=False)
    anos_experiencia_direccion = models.PositiveIntegerField(verbose_name='Años de experiencia Direccion', blank=True, null=True)
    anos_experiencia_rama = models.PositiveIntegerField(verbose_name='Años de experiencia Rama', blank=True, null=True)
    militancia = models.CharField(verbose_name='Militancia', max_length=50, blank=True, null=True, choices=CHOICE_MILITANCIA)
    sexo = models.CharField(verbose_name='Sexo', max_length=50, blank=True, null=True, choices=CHOICE_SEXO)
    color = models.CharField(verbose_name='Color', max_length=50, blank=True, null=True, choices=CHOICE_COLOR)
    modalidad_promocion = models.ManyToManyField(ModalidadPromocion, verbose_name='Modalidad del movimiento por Promocion',blank=True, null=True)
    modalidad_sustitucion = models.CharField(verbose_name='Modalidad del movimiento por Sustitucion', max_length=100, blank=True, null=True, choices=CHOICE_MODALIDAD_SUSTITUCION)
    edad = models.PositiveIntegerField(verbose_name='Edad')
    fecha_alta = models.DateField(verbose_name='Fecha de Alta')
    fecha_baja = models.DateField(verbose_name='Fecha de Baja', blank=True, null=True)
    tiempo_en_cargo = models.CharField(verbose_name='Tiempo en el cargo(años)', blank=True, null=True, max_length=50)
    observaciones = models.CharField(verbose_name='Observaciones', max_length=255, blank=True, null=True)
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

