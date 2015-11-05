# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.CharField(serialize=False, primary_key=True, max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('va_email', models.EmailField(max_length=254)),
                ('foiable_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='GithubTeam',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('org', models.CharField(max_length=128)),
                ('team', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='OnboardingStep',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('done', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('icon', models.CharField(max_length=32, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SlackChannel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('team', models.CharField(max_length=128)),
                ('channel', models.CharField(max_length=128)),
                ('roles', models.ManyToManyField(related_name='slacks', to='mandelbrot.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=256)),
                ('action', models.CharField(max_length=256, blank=True)),
                ('roles', models.ManyToManyField(related_name='steps', to='mandelbrot.Role')),
            ],
        ),
        migrations.AddField(
            model_name='onboardingstep',
            name='step',
            field=models.ForeignKey(related_name='onboardings', to='mandelbrot.Step'),
        ),
        migrations.AddField(
            model_name='onboardingstep',
            name='who',
            field=models.ForeignKey(related_name='onboardings', to='mandelbrot.Expert'),
        ),
        migrations.AddField(
            model_name='githubteam',
            name='roles',
            field=models.ManyToManyField(related_name='githubs', to='mandelbrot.Role'),
        ),
        migrations.AddField(
            model_name='expert',
            name='roles',
            field=models.ManyToManyField(related_name='experts', to='mandelbrot.Role'),
        ),
        migrations.AddField(
            model_name='expert',
            name='steps',
            field=models.ManyToManyField(to='mandelbrot.Step', through='mandelbrot.OnboardingStep'),
        ),
    ]
