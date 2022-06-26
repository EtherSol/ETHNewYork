from django.http import HttpResponse
from django.shortcuts import render 

def home_view(request,*args, **kwargs):
    return render(request,"home.html",{})

def info_view(request,*args, **kwargs):
    return render(request,"info.html",{})