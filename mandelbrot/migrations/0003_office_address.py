# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0002_office'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='address',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
