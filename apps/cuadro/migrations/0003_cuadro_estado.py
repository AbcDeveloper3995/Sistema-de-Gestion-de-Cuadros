# Generated by Django 3.0.10 on 2021-11-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuadro', '0002_auto_20211116_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuadro',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
