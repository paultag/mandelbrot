# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0006_expert_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
