# Generated by Django 3.0.10 on 2021-12-03 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuadro', '0006_auto_20211130_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clasificadorcargocuadro',
            name='codigo',
            field=models.CharField(max_length=3, unique=True, verbose_name='Codigo'),
        ),
    ]