from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method=="POST":
         if request.POST['password']==request.POST['passwordagain']:
             try:
                 user=User.objects.get(username=request.POST['username'])
                 return render(request,'register.html',{'error':"Username Already Exists:"})   
             except User.DoesNotExist:
                 user=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
                 return render(request,'home.html')
         else:
             return render(request,'register.html',{'error':"Password doesn't match"})   
    else:
        return render(request,'register.html')    

def login(request):
    if request.method=="POST":
       name=request.POST['username']
       pwd=request.POST['password']
       user=auth.authenticate(username=name,password=pwd)
       if user is not None:
           auth.login(request,user)
           return render(request,'showdiary.html')
       else:
           return render(request,'home.html',{'error':"Invalid username or pasword"})
    else:
       return render(request,'home.html')


def logout(request):
   auth.logout(request)
   return render(request,'home.html')        



