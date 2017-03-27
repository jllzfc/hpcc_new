# -*- coding:utf-8 -*-

import sys
from functools import wraps
import hashlib

import os

reload(sys)
sys.setdefaultencoding('utf8')


def asapi(all_null=True,args_list=[]):
    def _func(func):
        @wraps(func)
        def __func(request,*args,**kwargs):
            for arg in args_list:
                if not kwargs.has_key(arg):
                    return {'code': -1, 'msg': u'参数缺失:'+arg,'data':{}}
            if all_null:
                for key in kwargs:
                    if kwargs[key] == '':
                        return {'code':-1,'msg':key+u'不能为空','data':{}}
            return func(request, *args, **kwargs)
        return __func
    return _func


from main.models import News
def news_add(request,**kwargs):
    news=News(**kwargs)
    news.save()
    return {'news':news.tojson()}


def test(request,name):
    return {'name':name}
# from models import User
# @asapi(args_list=['id'])
# def user_delete(request,id,**kwargs):
#     user=User.objects.filter(id=id,**kwargs).first()
#     user.delete()
#     return {'user':user.tojson()}
#
# @asapi(all_null=True,args_list=['username','password'])
# def user_register(request,**kwargs):
#     u=User.objects.filter(username=kwargs['username'])
#     if u:
#         return {'code':-1,'msg':u'已经存在'+kwargs['username']+u'用户'}
#     user=User(**kwargs)
#     user.save()
#     m=hashlib.md5(str(user.id).encode("utf-8"))
#     user.token=m.hexdigest()
#     user.save()
#     return {'user':user.tojson()}
#
# @asapi(args_list=['id','username','password'])
# def user_edit(request,id,**kwargs):
#     user=User.objects.filter(id=id).first()
#     user=User(**kwargs)
#     user.save()
#     return {'code':1}
#
# @asapi(args_list=['username','password'])
# def login(request,**kwargs):
#     user=User.objects.filter(**kwargs).first()
#     request.session['user_id']=user.id
#     return {'user':user.tojson()}

# @asapi()
# def get_all_user(request,**kwargs):
#     users=User.objects.all()
#     list_user=[]
#     for u in users:
#         list_user.append(u.tojson())
#     return {'data':{'users':list_user}}
#
#
# def get_user(request,**kwargs):
#     user=User.objects.filter(**kwargs).first()
#     return {'code': 1, 'user': user.tojson()}
#
# def user_update_icon(request,id,icon):
#     user=User.objects.filter(id=id).first()
#     user.icon=icon;
#     user.save()
#     return {'code': 1, 'user': user.tojson()}
#
# from models import Grade
# def get_all_grade(request,**kwargs):
#     grades=Grade.objects.all()
#     list_grade=[]
#     for g in grades:
#         list_grade.append(g.tojson())
#     return {'data':{'grades':list_grade}}
#
# from models import Course
# def get_all_course(request,**kwargs):
#     courses=Course.objects.all()
#     list_courses=[]
#     for c in courses:
#         list_courses.append(c.tojson())
#     return {'data':{'courses':list_courses}}
#
# def get_all_course_by_grade(request,gradeid,**kwargs):
#     courses = Course.objects.filter(grade__id__exact=gradeid)
#     list_courses = []
#     for c in courses:
#         list_courses.append(c.tojson())
#     return {'data': {'courses': list_courses}}

from django import forms
class upload_form(forms.Form):
    file = forms.FileField()


import time
def upload(request,**kwargs):
    if request.method == "POST":
        uf = upload_form(request.POST, request.FILES)
        if uf.is_valid():
            file = uf.cleaned_data['file']
            filename=file.name.split('.')[0]+'_'+str(int(time.time()))+'.'+file.name.split('.')[1]
            f=open(os.path.join('media',filename),'wb')
            for chunk in file.chunks():
                f.write(chunk)
            f.close()
            return {'code':1,'url':'/media/'+filename}
        else:
            return {'code':-1}


