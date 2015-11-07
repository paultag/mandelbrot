# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0003_office_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type', models.CharField(choices=[('email', 'emaill')], max_length=128)),
            ],
        ),
    ]
