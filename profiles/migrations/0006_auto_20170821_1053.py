# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-21 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20170821_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='tipo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='años_exp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='especialidad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiles.Especialidad'),
            preserve_default=False,
        ),
    ]
