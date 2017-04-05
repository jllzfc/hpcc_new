# -*- coding:utf-8 -*-

from django.shortcuts import render

# Create your views here.

from models import News

def news_list(request):
    newss=News.objects.all()
    return render(request, 'main/news_list.html',{'title':u'新闻列表','newss':newss})

def news_detail(request,id):
    news=News.objects.get(id=id)
    return render(request,'main/news_detail.html',{'title':news.title,'news':news})

