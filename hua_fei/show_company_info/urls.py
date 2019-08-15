# -*- coding: utf-8 -*-

# @Time : 2019/8/15 19:57 
# @Author : WYT 
# @Site :  
# @File : urls.py 
# @Software: PyCharm

from django.conf.urls import url


from . import views

urlpatterns = [
    # url('', views.),
    url(r'^index.html/', views.index),
]