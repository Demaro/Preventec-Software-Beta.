# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-01 03:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20170821_1053'),
        ('modulos', '0019_remove_documento_archivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='documento',
            old_name='update',
            new_name='fecha',
        ),
        migrations.RemoveField(
            model_name='documento',
            name='nombre',
        ),
        migrations.AddField(
            model_name='documento',
            name='depto',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='documento',
            name='duracion',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='documento',
            name='subtitulo1',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='documento',
            name='subtitulo2',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='documento',
            name='titulo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='documento',
            name='user1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='documento',
            name='user2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='template',
            name='tipo',
            field=models.ManyToManyField(blank=True, null=True, related_name='documento', to='modulos.Documento'),
        ),
    ]
