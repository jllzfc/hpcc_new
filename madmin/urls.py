# -*- coding:utf8 -*-
from functools import wraps

from django.conf.urls import patterns, url

import madmin.views
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponseRedirect, HttpResponse
import json
import madmin.api

urlpatterns = patterns('',
                       url(r'^api/(?P<apiname>\S+)$', 'madmin.urls.request_handle_api'),
                       url(r'^(?P<viewname_with_id>\S+)/(?P<id>\d+)$', 'madmin.urls.request_handle_view_id'),
                       url(r'^(?P<viewname>\S+)$', 'madmin.urls.request_handle_view'),
                       url(r'^login$', madmin.views.login),
                       url(r'', madmin.views.index),
                       )


def required_login(func):
    def __func(request, *args, **kwargs):
        session = request.session.get('user_id')
        if (session):
            return func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/madmin/login')
    return __func


@csrf_exempt
# @required_login
def request_handle_view(request, viewname):
    view_render = getattr(madmin.views, viewname)(request)
    return view_render

@csrf_exempt
# @required_login
def request_handle_view_id(request, viewname_with_id, id):
    view_render = getattr(madmin.views, viewname_with_id)(request, id)
    return view_render

@csrf_exempt
def request_handle_api(request, apiname):
    try:
        result = {}
        if (request.method == 'POST' or request.method == 'GET'):
            result['msg'] = ''
            kwargs = request.POST or request.GET
            dic = {}
            for key in kwargs:
                dic.update({key: str(kwargs[key])})
            result['code'] = 1
            result.update(getattr(madmin.api, apiname)(request, **dic))
    except Exception as e:
        result = {'msg': str(e)}
        result['code'] = -1
    return HttpResponse(json.dumps(result), content_type='application/json')



