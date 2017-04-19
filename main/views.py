# -*- coding:utf-8 -*-

from django.shortcuts import render

# Create your views here.
from main.utils import gen_pager
from models import News

def news_list(self,request):
    from main.templatetags import irfilters
    kw = request.GET.get('kw', '')
    query = News.objects.filter()
    if kw:
        query = query.filter(title__icontains=kw)
    pager = gen_pager(query, param=request.GET, size=12)
    items = [x for x in pager['items']]
    pager['items'] = items
    grouplist = irfilters.groupbydate(items, 'published')
    return self.render_to_response(request, 'main/news_list.html',
                                    {'newslist': items, 'grouplist': grouplist, 'pager': pager, 'kw': kw})

def news_detail(request,id):
    news=News.objects.get(id=id)
    return render(request,'main/news_detail.html',{'title':news.title,'news':news})



