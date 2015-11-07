# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0006_contactdetail_who'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expert',
            old_name='foiable_email',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='expert',
            name='va_email',
        ),
    ]
