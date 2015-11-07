# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0002_auto_20151107_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='title',
            field=models.CharField(default='Digital Services Expert', max_length=128),
            preserve_default=False,
        ),
    ]
