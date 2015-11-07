# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0011_auto_20151107_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='offices',
            field=models.ManyToManyField(related_name='projects', to='mandelbrot.Office'),
        ),
    ]
