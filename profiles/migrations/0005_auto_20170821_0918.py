# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-21 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20170821_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='digitalid',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='height_field',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='width_field',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
