#-*- coding:utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render

from main.models import User

def global_setting(request):
    session = request.session.get('user_id')
    if session:
        user=User.objects.filter(id=session).first()
        if user:
            return {'admin_user': user}
    return {}

def login(request):
    return render(request,'madmin/login.html',{'title':u'登录'})

from main.models import News
def index(request):
    # session = request.session.get('user_id')
    # if (session):
        newss = News.objects.all()
        return render(request, 'madmin/news_list.html', {'title': u'新闻管理', 'newss': newss})
    # else:
    #     return HttpResponseRedirect('/madmin/login')

