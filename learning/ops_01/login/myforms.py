# -*- coding:utf-8 -*-
from django import forms

# 登录表单
class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control",
                                                                       "placeholder": "请输入用户名",
                                                                       "autofocus": "autofocus",
                                                                       "maxlength": "20",
                                                                       "id": "username",
                                                                       "type": "text"}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                           "placeholder": "请输入密码",
                                                                           "autofocus": "autofocus",
                                                                           "maxlength": "20",
                                                                           "id": "password"}))



# 注册表单
class RegisterFroms(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control",
                                                                       "placeholder": "请输入用户名",
                                                                       "autofocus": "autofocus",
                                                                       "maxlength": "20",
                                                                       "id": "username",
                                                                       "type": "text"}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                            "placeholder": "请输入密码",
                                                                            "autofocus": "autofocus",
                                                                            "maxlength": "20",
                                                                            "id": "password",
                                                                            "type": "password"}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                            "placeholder": "再输一次密码",
                                                                            "autofocus": "autofocus",
                                                                            "maxlength": "20",
                                                                            "id": "password",
                                                                            "type": "password"}))
    code = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control",
                                                                   "placeholder": "输入验证码",
                                                                   "autofocus": "autofocus",
                                                                   "maxlength": "20",
                                                                   "id": "code",
                                                                   "type": "text"}))
