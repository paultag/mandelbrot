# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0012_project_offices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.CharField(primary_key=True, serialize=False, max_length=128),
        ),
    ]
