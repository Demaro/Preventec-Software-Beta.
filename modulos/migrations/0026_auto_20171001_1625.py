# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-01 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0025_documento_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='descripcion',
            field=models.TextField(default='hola'),
            preserve_default=False,
        ),
    ]
