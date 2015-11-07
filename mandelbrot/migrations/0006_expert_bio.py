# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0005_auto_20151107_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='bio',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
