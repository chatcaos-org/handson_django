# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-18 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='auto_ajuda', max_length=20),
        ),
    ]