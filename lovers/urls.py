#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-08 14:49
# @Author  : opsonly
# @Site    : 
# @File    : urls.py
# @Software: PyCharm


from django.urls import path,re_path
from . import views
app_name = 'lovers'

urlpatterns = [
    path('list',views.lovelist,name='lovelist'),
    path('insert',views.songcomment,name='insert'),
    path('songer/<str:ser>', views.songlist, name='songer'),
    path('comment/<int:sid>/<str:songname>',views.songcomments,name='comment'),

]