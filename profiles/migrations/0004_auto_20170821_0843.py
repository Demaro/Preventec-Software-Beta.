# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-21 13:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_profile_unidad_asignada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='años_exp',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='especialidad',
        ),
    ]
