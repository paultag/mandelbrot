# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0009_auto_20151107_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='photo_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='projectmember',
            name='end_date',
            field=models.DateField(blank=True, default='1886-01-01'),
            preserve_default=False,
        ),
    ]
