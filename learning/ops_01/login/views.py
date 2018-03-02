from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from login import myforms
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# 登录页面的方法
def login(request):
    login_froms = myforms.LoginForm
    if request.method=='POST':
        #取出post的值
        lf=login_froms(request.POST)
        #判断是否存在
        if lf.is_valid():
            #取出对应的用户名和密码
            username=lf.cleaned_data['username']
            password=lf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user=authenticate(username=username,password=password)
            # 如果账号密码正确则登录
            if user:
                auth.login(request,user)
                # 保存到session中
                request.session['username'] = username
                return HttpResponseRedirect('mainpage/index/')
            #如果不存在则报错
            elif user is None:
                error_msg='用户名或密码错误！'
                return render(request, 'login/login.html', {'error_msg': error_msg,'login_froms': login_froms})
    return render(request, 'login/login.html', {'login_froms': login_froms})


# 注册页面的方法
#@csrf_exempt
def register(request):
    registerfroms = myforms.RegisterFroms
    if request.method == 'POST' and request.POST.getlist('register'):
        rf = registerfroms(request.POST)
        if rf.is_valid():
            if rf.cleaned_data['code'] == '123':
                if rf.cleaned_data['password2'] == rf.cleaned_data['password1']:
                    username = rf.cleaned_data['username']
                    password = rf.cleaned_data['password1']
                    user=auth.authenticate(username = username,password = password)
                    if user:
                        error_msg="用户已存在！"
                        return render(request, 'login/register.html', {'registerfroms': registerfroms,"error_msg":error_msg})
                    else:
                        # 添加到数据库（还可以加一些字段的处理）
                        user = User.objects.create_user(username=username, password=password)
                        user.save()
                        # 添加到session
                        request.session['username'] = username
                        # 调用auth登录
                        auth.login(request, user)
                        # 重定向到首页
                        return HttpResponseRedirect('/')
                else:
                    error_msg = '两次密码输入不一致!'
                    return render(request, 'login/register.html',
                                  {'registerfroms': registerfroms, "error_msg": error_msg})
    return render(request, 'login/register.html', {'registerfroms': registerfroms})

def index(request):
    #判断是否登录，如果没有登录则转向到登录界面
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        # 从session中取出用户名
        username=request.session.get('username','anybody')
        return render(request, 'mainpage/index.html',{'username':username})

def logout(request):
    #注销用户，删除session中的username
    auth.logout(request)
    return render(request,'login/logout.html')
