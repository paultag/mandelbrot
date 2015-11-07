# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0010_auto_20151107_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmember',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
