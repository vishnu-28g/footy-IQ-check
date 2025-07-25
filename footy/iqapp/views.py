from django.shortcuts import render,redirect
from .models import beginner,intermediate,pro
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    # posts=section.objects.all()
    return render(request,'welcome.html')

def index(request):
    return render(request,'index.html')
    
def begin(request):
    posts=beginner.objects.all()
    return render(request,'index.html',{'posts':posts})

    
def inter(request):
    posts=intermediate.objects.all()
    return render(request,'index.html',{'posts':posts})

    
def pr(request):
    pr=pro.objects.all()
    return render(request,'index.html',{'posts':pr})

    



