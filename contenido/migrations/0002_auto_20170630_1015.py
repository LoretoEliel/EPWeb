# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-30 14:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenido', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=150, null=True)),
                ('descripcion', models.TextField(blank=True, max_length=5000, null=True)),
                ('libro', models.URLField(blank=True, default='', max_length=2000, null=True)),
                ('categoria', models.CharField(blank=True, max_length=150, null=True)),
                ('subida', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='subir_info',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='subir_info',
        ),
    ]