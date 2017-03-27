from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name=u'昵称',default='用户')
    birday = models.DateField(verbose_name=u'生日',null=True,blank=True)
    gender = models.CharField(choices=(('male',u'男'),('female',u'女')),default=('male',u'男'))
    address = models.CharField(max_length=100)