# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db import models
import datetime
from DjangoUeditor.models import UEditorField


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=datetime.datetime.now)
    author = models.CharField(max_length=50, null=True)
    picture = models.CharField(max_length=1000)
    actical = UEditorField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def tojson(self):
        return {'title': self.title, 'created_date': str(self.created_date.time()), 'author': self.author,
                'picture': self.picture, 'actical': self.actical}

    def __unicode__(self):
        return self.title

    class Mate:
        verbose_name_plural = 'news'
        ordering = ['-created_date', 'title']

    def get_month(self):
        return self.created_date.month

    def get_class_flag(self):
        if self.id == News.objects.order_by('-id').first().id:
            return True
        next_news = self.get_next_by_created_date()
        if self.get_month() == next_news.get_month():
            return False
        else:
            return True


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_image', blank=True)

    def __unicode__(self):
        return self.user.username
