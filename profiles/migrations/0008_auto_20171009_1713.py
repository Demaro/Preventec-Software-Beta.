# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-09 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20171009_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contrato',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='legales_asoc',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]