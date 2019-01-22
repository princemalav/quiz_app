# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render , reverse
from django.shortcuts import HttpResponse , HttpResponseRedirect
from .forms import UserRegistrationfrom
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepageview(request):
    my_dic = {'insert':'Hello'}
    return render(request,'quiz_app/homepage.html',context=my_dic)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserRegistrationfrom(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserRegistrationfrom()
    return render(request,'quiz_app/register.html',{'user_form':user_form,
                                                    'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('quiz_app:homepage'))
            else:
                return HttpResponse('account not active')
        else:
            return HttpResponse('invalid login details')
    else:
        return render(request,'quiz_app/login.html')



    return render(request,'quiz_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('quiz_app:homepage'))
