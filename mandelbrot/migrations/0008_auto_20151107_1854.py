# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0007_auto_20151107_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='buddy',
            field=models.ForeignKey(to='mandelbrot.Expert', null=True, related_name='buddies'),
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='type',
            field=models.CharField(max_length=128, choices=[('email', 'E-Mail'), ('phone', 'Phone'), ('fax', 'Fax'), ('twitter', 'Twitter')]),
        ),
    ]
