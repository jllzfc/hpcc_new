"""hpcc_new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
import os
import settings
from django.contrib import admin
import main.urls,madmin.urls
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/', include(main.urls)),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^madmin/',include(madmin.urls)),
    url(r'^login',TemplateView.as_view(template_name='madmin/login.html')),
]

urlpatterns += patterns('',
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': os.path.join(settings.BASE_DIR, 'media'), 'show_indexes': settings.DEBUG}),
                        )

urlpatterns += patterns('',
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': os.path.join(settings.BASE_DIR, 'static'), 'show_indexes': settings.DEBUG}),
                        )
