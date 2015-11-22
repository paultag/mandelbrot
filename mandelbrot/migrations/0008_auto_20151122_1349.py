# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandelbrot', '0007_auto_20151107_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='githubteam',
            name='roles',
        ),
        migrations.RemoveField(
            model_name='onboardingstep',
            name='step',
        ),
        migrations.RemoveField(
            model_name='onboardingstep',
            name='who',
        ),
        migrations.RemoveField(
            model_name='slackchannel',
            name='roles',
        ),
        migrations.RemoveField(
            model_name='step',
            name='roles',
        ),
        migrations.RemoveField(
            model_name='expert',
            name='steps',
        ),
        migrations.DeleteModel(
            name='GithubTeam',
        ),
        migrations.DeleteModel(
            name='OnboardingStep',
        ),
        migrations.DeleteModel(
            name='SlackChannel',
        ),
        migrations.DeleteModel(
            name='Step',
        ),
    ]
