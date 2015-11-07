# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0003_expert_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.CharField(serialize=False, max_length=128, primary_key=True)),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Badges',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('awarded_on', models.DateField()),
                ('awarded_by', models.ForeignKey(related_name='badges_given', to='mandelbrot.Expert')),
                ('badge', models.ForeignKey(related_name='recipiants', to='mandelbrot.Badge')),
                ('who', models.ForeignKey(related_name='badges', to='mandelbrot.Expert')),
            ],
        ),
    ]
