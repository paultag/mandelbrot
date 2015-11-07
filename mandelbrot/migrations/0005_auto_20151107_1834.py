# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0004_contactdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdetail',
            name='label',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='note',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='value',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='type',
            field=models.CharField(max_length=128, choices=[('email', 'E-Mail'), ('phone', 'Phone')]),
        ),
    ]
