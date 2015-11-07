# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0008_auto_20151107_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('mission', models.TextField()),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMember',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('project', models.ForeignKey(to='mandelbrot.Project', related_name='memberships')),
                ('who', models.ForeignKey(to='mandelbrot.Expert', related_name='memberships')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='experts',
            field=models.ManyToManyField(to='mandelbrot.Expert', through='mandelbrot.ProjectMember'),
        ),
        migrations.AddField(
            model_name='expert',
            name='projects',
            field=models.ManyToManyField(to='mandelbrot.Project', through='mandelbrot.ProjectMember'),
        ),
    ]
