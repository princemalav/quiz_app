# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render , reverse , get_object_or_404
from django.shortcuts import HttpResponse , HttpResponseRedirect
from .forms import UserRegistrationfrom
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required
from quiz_app.models import Sample , Quizquestion

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

@login_required
def question_view(request):
    product = Quizquestion.objects.all()
    correct_ans = Quizquestion.objects.get(id=2)
    my_dic = {'question':product}
    if request.method == 'POST':
        user_answer = request.POST.get('option')
        print(user_answer)
        if user_answer == correct_ans.answer:

            my_dict = {'message':'Congratulation, your answer is right',
            'right_ans':correct_ans.answer,
            'user_ans':user_answer,
            'question':product}
            return render(request,'quiz_app/question.html',context=my_dict)
        else:
            my_dict = {'message':'Oops!, your answer is Wrong',
            'right_ans':correct_ans.answer,
            'user_ans':user_answer,
            'question':product}
            return render(request,'quiz_app/question.html',context=my_dict)

    return render(request,'quiz_app/question.html',context=my_dic)

def sample(request):
    product = Sample.objects.all()
    my_dict = {'objects':product}
    return render(request,'sample.html',context=my_dict)

def about(request):
    return render(request,'quiz_app/about.html')

def contact(request):
    return render(request,'quiz_app/contact.html')

def question_detail_view(request,pk=1 , *args , **kwargs):
    product = Quizquestion.objects.get(id=pk)
    my_dict = {'question': product}
    print(product.q_name)
    print(product.id)
    return render(request,'quiz_app/detail_question.html',context=my_dict)
