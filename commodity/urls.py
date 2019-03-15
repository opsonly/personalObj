#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-03-01 15:07
# @Author  : opsonly
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.urls import path,re_path
from . import views
app_name = 'commodity'

urlpatterns = [
    path('ditylist',views.index,name='ditylist'),
    path('commolist',views.commonlist,name='commolist'),
    path('shoplist/<int:id>',views.shoplist,name='shoplist'),
]