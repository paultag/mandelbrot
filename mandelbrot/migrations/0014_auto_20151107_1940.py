# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0013_auto_20151107_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='public',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='offices',
            field=models.ManyToManyField(blank=True, to='mandelbrot.Office', related_name='projects'),
        ),
    ]
