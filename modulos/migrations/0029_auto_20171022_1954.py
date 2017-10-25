# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-23 00:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0028_auto_20171022_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='user1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='profiles.Profile'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='user2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='profiles.Profile'),
        ),
    ]