# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 20:59
# @Author  : MLee
# @File    : task.py
from . import views

try:
    from django.conf.urls import url
except ImportError:
    from django.urls import url

urlpatterns = [
    url('^add/', views.add_subscriber),
]
