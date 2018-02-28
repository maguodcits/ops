from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from login import myforms
from login.models import UserInput
from django.contrib import messages
from django import forms


# Create your views here.
# 登录页面的方法
def login(request):
    login_froms = myforms.LoginForm
    if request.method == 'POST':
        if request.POST.getlist('register'):
            return HttpResponseRedirect('/register/')  # 跳转到注册页面
        else:
            #登录判断，开发期间先不写
            return HttpResponseRedirect('mainpage/index/')
    return render(request, 'login/login.html', {'login_froms': login_froms})


# 注册页面的方法
def register(request):
    registerfroms = myforms.RegisterFroms
    if request.method == 'POST' and request.POST.getlist('register'):
        rf = registerfroms(request.POST)
        if rf.is_valid():
            if rf.cleaned_data['code'] == '123':
                if rf.cleaned_data['password2'] == rf.cleaned_data['password1']:
                    username = rf.cleaned_data['username']
                    password = rf.cleaned_data['password1']
                    user = UserInput.objects.filter(username=username)
                    if user:
                        error_msg="用户已存在！"
                        return render(request, 'login/register.html', {'registerfroms': registerfroms,"error_msg":error_msg})
                    elif len(user) == 0:
                        ui = UserInput()
                        ui.username = username
                        ui.password = password
                        ui.save()
                        messages.success(request, '注册成功!')
                else:
                    error_msg = '两次密码输入不一致!'
                    return render(request, 'login/register.html',
                                  {'registerfroms': registerfroms, "error_msg": error_msg})
    # elif request.method == 'POST' and request.POST.getlist('return'):
    #     return HttpResponseRedirect('/login/')
    return render(request, 'login/register.html', {'registerfroms': registerfroms})

def index(request):
    return render(request, 'mainpage/index.html')