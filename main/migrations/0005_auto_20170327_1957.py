# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170326_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='actical',
            field=DjangoUeditor.models.UEditorField(verbose_name='\u5185\u5bb9', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='picture',
            field=models.CharField(max_length=1000),
        ),
    ]
