# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='news',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='news',
            name='slug',
        ),
        migrations.AddField(
            model_name='news',
            name='actical',
            field=DjangoUeditor.models.UEditorField(default='haha'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='picture',
            field=models.ImageField(default='haha', upload_to=b''),
            preserve_default=False,
        ),
    ]
