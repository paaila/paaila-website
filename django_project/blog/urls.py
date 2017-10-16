"""Paaila URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.http import HttpResponse
from . import views

urlpatterns = [
    url(r'^$', views.BlogListView.as_view(), name="post_list"),
    url(r'^post/new/$', views.post_new, name="post_new"),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/$', views.BlogDetailView.as_view(), name='post_detail'),
    # url(r'^post/([0-9]{4})/([0-9]{2})/([0-9]{2})/(?P<pk>\d+)$', views.BlogDetailView.as_view(), name='post_detail'),

]

