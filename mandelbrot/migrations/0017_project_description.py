# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0016_auto_20160130_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
