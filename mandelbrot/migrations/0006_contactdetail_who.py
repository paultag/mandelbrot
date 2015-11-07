# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0005_auto_20151107_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdetail',
            name='who',
            field=models.ForeignKey(to='mandelbrot.Expert', related_name='contact_details', default='paul.tagliamonte'),
            preserve_default=False,
        ),
    ]
