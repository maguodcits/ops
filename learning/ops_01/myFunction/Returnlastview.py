from django.shortcuts import render
from urllib.parse import urlencode

def return_last_view(request):
    fullpath=request.get_full_path(request)
    mypath=urlencode({'',fullpath})[1:]
    return  mypath