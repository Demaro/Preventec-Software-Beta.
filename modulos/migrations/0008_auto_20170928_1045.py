# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-28 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0007_auto_20170928_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpeta',
            name='is_subcarpeta',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
