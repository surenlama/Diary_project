from django.shortcuts import render
from django.contrib.auth.models import User
from .models import memory
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login')
def add(request):
    if request.method== "POST":
       miny=request.POST['data']
       new=memory(content=miny,user=request.user)
       new.save()
       return render(request,'addmemory.html')
    else:
       return render(request,'addmemory.html')

@login_required(login_url='/accounts/login')
def show(request):
    memo=memory.objects.filter(user=request.user)
    return render(request, 'showdiary.html',{'show':memo})  
