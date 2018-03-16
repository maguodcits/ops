# -*- coding:utf-8 -*-
from django import forms

# 服务器监控配置form
class Power_setting(forms.Form):
    powerName = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control",
                                                                        "autofocus": "autofocus",
                                                                        "id": "powerName",
                                                                        "type": "text"}))
    powerIP = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control",
                                                                      "id": "powerName",
                                                                      "type": "text"}))
    powerNumber = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control",
                                                                          "id": "powerName",
                                                                          "type": "text"}))
    username_power = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control",
                                                                             "id": "powerName",
                                                                             "type": "text"}))
    password_power = forms.CharField(label='', widget=forms.TextInput(attrs={"class": "form-control",
                                                                             "id": "username",
                                                                             "type": "password"}))


