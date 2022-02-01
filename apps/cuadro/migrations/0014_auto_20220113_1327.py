# Generated by Django 3.0.10 on 2022-01-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuadro', '0013_auto_20220110_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuadro',
            name='fecha_baja',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Baja'),
        ),
        migrations.AlterField(
            model_name='cuadro',
            name='modalidad_promocion',
            field=models.CharField(blank=True, choices=[(11, 'Que procede de la reserva'), (12, 'Mujeres promovidas en el periodo'), (13, 'Negros y mulatos promovidos en el periodo')], max_length=100, null=True, verbose_name='Modalidad del movimiento por Promocion'),
        ),
        migrations.AlterField(
            model_name='cuadro',
            name='modalidad_sustitucion',
            field=models.CharField(blank=True, choices=[(101, 'Ubicado en otro cargo de inferior jerarquia y diferente categoria ocupacional'), (102, 'Cese de su relacion de trabajo')], max_length=100, null=True, verbose_name='Modalidad del movimiento por Sustitucion'),
        ),
    ]