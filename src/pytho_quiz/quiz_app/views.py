# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def homepageview(request):
    my_dic = {'insert':'Hello'}
    return render(request,'quiz_app/homepage.html',context=my_dic)
