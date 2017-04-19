#-*- coding:utf8 -*-
from functools import wraps

from django.conf.urls import patterns, url

import main.views
from django.views.decorators.csrf import csrf_exempt
import json
from django.http.response import HttpResponse, HttpResponseRedirect

from main import views

urlpatterns = patterns('',
                       # url(r'^login$',main.views.login),
                       url(r'^(?P<viewname_with_id>\S+)/(?P<id>\d+)$', 'main.urls.request_handle_view_id'),
                       url(r'^(?P<viewname>\S+)$', 'main.urls.request_handle_view'),
                       # url(r'', main.views.index),
                       )
@csrf_exempt
def request_handle_view(request, viewname):
    view_render = getattr(main.views, viewname)(request)
    return view_render


@csrf_exempt
def request_handle_view_id(request, viewname_with_id, id):
    view_render = getattr(main.views, viewname_with_id)(request, id)
    return view_render


