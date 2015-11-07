# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='buddy',
            field=models.ForeignKey(to='mandelbrot.Expert', null=True, related_name='buddies', blank=True),
        ),
    ]
