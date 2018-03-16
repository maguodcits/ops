from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from mainpage import  myforms
from .models import  PowerSetting
import os,platform

# Create your views here.
@login_required #判断是否登录，如果没有登录则转向到登录界面
def index(request):
    # 从session中取出用户名
    username=request.session.get('username','anybody')
    return render(request, 'mainpage/index.html',{'username':username})
#磁盘监控
@login_required
def Disk_monitoring(request):
    username = request.session.get('username', 'anybody')
    return render(request,'mainpage/Disk_monitoring.html',{'username':username})

#IO监控
@login_required
def IO_monitoring(request):
    username = request.session.get('username', 'anybody')
    return render(request,'mainpage/IO_monitoring.html',{'username':username})

#cpu监控
@login_required
def CPU_monitoring(request):
    username = request.session.get('username', 'anybody')
    return render(request,'mainpage/CPU_monitoring.html',{'username':username})


#内存监控
@login_required
def Memory_monitoring(request):
    username = request.session.get('username', 'anybody')
    return render(request,'mainpage/Memory_monitoring.html',{'username':username})




#服务器监控配置
@login_required
def Setting_Power(request):
    return_message=2
    settings=PowerSetting.objects.all()
    username = request.session.get('username', 'anybody')
    if request.method=='POST':
        IP=request.POST.get('text')
        #判断当前操作系统类型
        systemtype=platform.system()
        if systemtype=='Windows':
            backinfo = os.system('ping ' + IP)
            if backinfo==0:
                return_message= 0
                return render(request, 'mainpage/Profile.html',
                              {'username': username, 'settings': settings,'return_message':return_message})
            else:
                return_message = 1
                return render(request, 'mainpage/Profile.html',
                              {'username': username, 'settings': settings, 'return_message': return_message})
        elif systemtype=='Linux':
            pass
        else:
            pass
    return render(request,'mainpage/Profile.html',{'username':username,'settings':settings, 'return_message': return_message})




#增加服务器配置
def Setting_Dialog_Linux(request):
    settingForm=myforms.Power_setting
    if request.method=='POST':
        lf=settingForm(request.POST)
        if lf.is_valid():
            s=PowerSetting()
            s.powerName = request.POST['powerName']
            s.powerIP = request.POST['powerIP']
            s.powerNumber = request.POST['powerNumber']
            s.username_power = request.POST['username_power']
            s.password_power = request.POST['password_power']
            s.save()
            message='添加成功！'
            return render(request, 'mainpage/Setting_Dialog_Linux.html', {'settingForm': settingForm,'message':message})

    return render(request,'mainpage/Setting_Dialog_Linux.html',{'settingForm':settingForm})