# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-18 15:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('temas', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Autor')),
            ],
        ),
    ]
