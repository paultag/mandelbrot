# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0010_office_tips'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='tips',
            field=models.TextField(blank=True),
        ),
    ]