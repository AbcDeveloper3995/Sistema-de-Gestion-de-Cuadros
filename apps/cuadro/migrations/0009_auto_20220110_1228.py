# Generated by Django 3.0.10 on 2022-01-10 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuadro', '0008_auto_20220104_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True, verbose_name='Codigo')),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Movimiento',
                'verbose_name_plural': 'Movimientos',
                'db_table': 'Movimiento',
                'ordering': ['codigo'],
            },
        ),
        migrations.AddField(
            model_name='cuadro',
            name='fecha_alta',
            field=models.DateField(auto_now=True, verbose_name='Fecha de Alta'),
        ),
        migrations.AddField(
            model_name='cuadro',
            name='fecha_baja',
            field=models.DateField(auto_now=True, null=True, verbose_name='Fecha de Baja'),
        ),
        migrations.AddField(
            model_name='cuadro',
            name='modalidad_promocion',
            field=models.CharField(blank=True, choices=[('', '--------'), ('11', 'Que procede de la reserva'), ('12', 'Mujeres promovidas en el periodo'), ('13', 'Negros y mulatos promovidos en el periodo')], max_length=100, null=True, verbose_name='Modalidad del movimiento por Promocion'),
        ),
        migrations.AddField(
            model_name='cuadro',
            name='modalidad_sustitucion',
            field=models.CharField(blank=True, choices=[('', '--------'), ('101', 'Ubicado en otro cargo de inferior jerarquia y diferente categoria ocupacional'), ('102', 'Cese de su relacion de trabajo')], max_length=100, null=True, verbose_name='Modalidad del movimiento por Sustitucion'),
        ),
        migrations.AddField(
            model_name='cuadro',
            name='tiempo_en_cargo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tiempo en el cargo'),
        ),
        migrations.AlterField(
            model_name='cuadro',
            name='categoria',
            field=models.CharField(blank=True, choices=[('', '--------'), ('DS', 'Directivo Superior'), ('DI', 'Directivo Intermedio'), ('E', 'Ejecutivo')], max_length=50, null=True, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='cuadro',
            name='categoria_cientifica',
            field=models.CharField(blank=True, choices=[('', '--------'), ('Dr.Cs', 'Doctor en Ciencias'), ('MC.s', 'Máster en Ciencias')], max_length=20, null=True, verbose_name='Categoria Cientifica'),
        ),
        migrations.AlterField(
            model_name='cuadro',
            name='color',
            field=models.CharField(blank=True, choices=[('', '--------'), ('B', 'Blanca'), ('M', 'Mulata'), ('N', 'Negra')], max_length=50, null=True, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='cuadro',
            name='escolaridad',
            field=models.CharField(blank=True, choices=[('', '--------'), ('9noGrado', '9no Grado'), ('12moGrado', '12mo Grado'), ('Tec.Med.', 'Tecnico Medio'), ('Tec.Med.Sup.', 'Tecnico Medio Superior'), ('Universitario', 'Universitario')], max_length=20, null=True, verbose_name='Escolaridad'),
        ),
        migrations.AlterField(
            model_name='cuadro',
            name='sexo',
            field=models.CharField(blank=True, choices=[('', '--------'), ('F', 'Femenino'), ('M', 'Masculino')], max_length=50, null=True, verbose_name='Sexo'),
        ),
        migrations.AddField(
            model_name='cuadro',
            name='fk_movimiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cuadro.Movimiento', verbose_name='Movimiento'),
        ),
    ]