# Generated by Django 5.0.7 on 2024-08-11 02:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0001_initial'),
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='nivel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='juego.nivel'),
            preserve_default=False,
        ),
    ]
