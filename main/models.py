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
    picture=models.ImageField()
    actical=UEditorField('内容',height=100,width=500,toolbars=u'mini',blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def tojson(self):
        return {'title':self.title,'created_date':self.created_date,'author':self.author,'picture':self.picture,'actical':self.actical}

    def __unicode__(self):
        return self.title

    class Mate:
        verbose_name_plural = 'news'
        ordering = ['-created_date', 'title']


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_image',blank = True)

    def __unicode__(self):
        return self.user.username


