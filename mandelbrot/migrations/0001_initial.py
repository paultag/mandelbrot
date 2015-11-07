# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type', models.CharField(choices=[('email', 'E-Mail'), ('phone', 'Phone'), ('fax', 'Fax'), ('twitter', 'Twitter')], max_length=128)),
                ('label', models.CharField(max_length=128)),
                ('value', models.CharField(max_length=128)),
                ('note', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.CharField(serialize=False, primary_key=True, max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('photo_url', models.URLField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('public', models.BooleanField()),
                ('buddy', models.ForeignKey(related_name='buddies', null=True, to='mandelbrot.Expert')),
            ],
        ),
        migrations.CreateModel(
            name='GithubTeam',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('org', models.CharField(max_length=128)),
                ('team', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.CharField(serialize=False, primary_key=True, max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('latitude', models.CharField(max_length=128)),
                ('longitude', models.CharField(max_length=128)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OnboardingStep',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('done', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.CharField(serialize=False, primary_key=True, max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('mission', models.TextField()),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMember',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True, blank=True)),
                ('project', models.ForeignKey(related_name='memberships', to='mandelbrot.Project')),
                ('who', models.ForeignKey(related_name='memberships', to='mandelbrot.Expert')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('icon', models.CharField(blank=True, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='SlackChannel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('team', models.CharField(max_length=128)),
                ('channel', models.CharField(max_length=128)),
                ('roles', models.ManyToManyField(related_name='slacks', to='mandelbrot.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('description', models.CharField(max_length=256)),
                ('action', models.CharField(blank=True, max_length=256)),
                ('roles', models.ManyToManyField(related_name='steps', to='mandelbrot.Role')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='experts',
            field=models.ManyToManyField(through='mandelbrot.ProjectMember', to='mandelbrot.Expert'),
        ),
        migrations.AddField(
            model_name='project',
            name='offices',
            field=models.ManyToManyField(related_name='projects', blank=True, to='mandelbrot.Office'),
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
            name='projects',
            field=models.ManyToManyField(through='mandelbrot.ProjectMember', to='mandelbrot.Project'),
        ),
        migrations.AddField(
            model_name='expert',
            name='roles',
            field=models.ManyToManyField(related_name='experts', to='mandelbrot.Role'),
        ),
        migrations.AddField(
            model_name='expert',
            name='steps',
            field=models.ManyToManyField(through='mandelbrot.OnboardingStep', to='mandelbrot.Step'),
        ),
        migrations.AddField(
            model_name='contactdetail',
            name='who',
            field=models.ForeignKey(related_name='contact_details', to='mandelbrot.Expert'),
        ),
    ]
