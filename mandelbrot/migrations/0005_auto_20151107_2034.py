# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0004_badge_badges'),
    ]

    operations = [
        migrations.CreateModel(
            name='BadgeAward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('awarded_on', models.DateField()),
                ('awarded_by', models.ForeignKey(related_name='badges_given', to='mandelbrot.Expert')),
                ('badge', models.ForeignKey(related_name='recipiants', to='mandelbrot.Badge')),
                ('who', models.ForeignKey(related_name='badges', to='mandelbrot.Expert')),
            ],
        ),
        migrations.RemoveField(
            model_name='badges',
            name='awarded_by',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='badge',
        ),
        migrations.RemoveField(
            model_name='badges',
            name='who',
        ),
        migrations.DeleteModel(
            name='Badges',
        ),
    ]
