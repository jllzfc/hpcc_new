# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170325_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='actical',
        ),
        migrations.RemoveField(
            model_name='news',
            name='picture',
        ),
        migrations.AddField(
            model_name='news',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='detail',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default='haha', unique=True),
            preserve_default=False,
        ),
    ]
