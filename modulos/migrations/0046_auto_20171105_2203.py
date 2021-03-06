# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-06 03:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_profile_number'),
        ('modulos', '0045_carpeta_submodulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='carpeta',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='carpeta',
            name='fecha_termino',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='carpeta',
            name='user_asign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responsable', to='profiles.Profile'),
        ),
    ]
