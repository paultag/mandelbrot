# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-04 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0025_auto_20160204_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdetail',
            name='type',
            field=models.CharField(choices=[('email', 'E-Mail'), ('phone', 'Phone'), ('fax', 'Fax'), ('twitter', 'Twitter'), ('github', 'GitHub'), ('yo', 'Yo'), ('website', 'Cyber Website')], max_length=128),
        ),
    ]
