# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-12 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20171011_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='comite_par',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='subcta',
            field=models.BooleanField(default=False),
        ),
    ]