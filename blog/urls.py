#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-01 19:34
# @Author  : opsonly
# @Site    : 
# @File    : urls.py
# @Software: PyCharm


from django.urls import path,re_path
from . import views
app_name = 'blog'

urlpatterns = [
    path('detail/<int:id>',views.blogDetail,name='detail'),
    path('tag/<str:tag>',views.taglist,name='tag'),
]