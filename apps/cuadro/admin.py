from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from apps.cuadro.models import *


class clasificador_DPA_Resource(resources.ModelResource):
    class Meta:
        model = clasificadorDPA

class clasificador_DPA_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ('codigo', 'descripcion')
    resource_class = clasificador_DPA_Resource


class clasificador_Cargo_Cuadro_Resource(resources.ModelResource):
    class Meta:
        model = ClasificadorCargoCuadro

class clasificador_Cargo_Cuadro_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['codigo']
    list_display = ('codigo', 'descripcion')
    resource_class = clasificador_Cargo_Cuadro_Resource

class cuadro_Resource(resources.ModelResource):
    class Meta:
        model = Cuadro

class cuadro_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['ci']
    list_display = ('nombre', 'ci', 'fecha_alta')
    resource_class = cuadro_Resource

admin.site.register(Cargo)
admin.site.register(clasificadorDPA, clasificador_DPA_Admin)
admin.site.register(Especialidad)
admin.site.register(Cuadro, cuadro_Admin)
admin.site.register(ClasificadorCargoCuadro, clasificador_Cargo_Cuadro_Admin)