from django.shortcuts import render,redirect
from django.http import HttpResponse
from pro_11.models import people
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
import os
# Create your views here.
def fun(request):
    if request.method=='POST':
        a=request.POST['name']
        b=request.POST['age']
        c=request.FILES['photo']
        d=request.POST['username']
        f=request.POST['password']
        q=people(name=a,age=b,photo=c,username=d,password=f)
        q.save()
        z = User(username=d)
        z.set_password(f)
        z.save()
        print(a,b,c,d,f)
        return HttpResponse('data successfully saved')
    return render(request,'main.html')

def fun_1(request):
    return render(request,'home.html')

def people_views(request):
    q=people.objects.all()
    return render(request,'views.html',{'p':q})

def people_edit(request,id1):
    p_id1=id1
    q=people.objects.get(id=id1)
    if request.method=='POST':
        q.name=request.POST['name']
        q.age=request.POST['age']
        if len(request.FILES)!=0:
            if len(q.photo)>0:
                os.remove(q.photo.path)
                q.photo=request['photo']

        q.username=request.POST['username']
        q.password=request.POST['password']
        q.save()
        return HttpResponse('data successfully updated')
    return render(request,'views.html',{'r':q})

def people_delete(request,id1):
    p_id=id1
    q=people.objects.get(id=id1)
    q.delete()
    return HttpResponse('data successfully deleted')


def search(request):
    if request.method=='POST':
        a=request.POST['username']
        b=request.POST['password']
        q=people.objects.filter(username=a)
        return render(request,'search.html',{'s':q})
    return render(request,'search.html')

def login(request):
    if request.method=='POST':
        a=request.POST['username']
        b=request.POST['password']
        q=authenticate(username=a,password=b)
        request.session['user_id']=a
        if q is not None and q.is_superuser == 1:
            return redirect(admin_home)
        else:
            m = people.objects.get(username=a)
            if m.password == b:
                if q is not None and q.is_superuser == 0:
                    return redirect(user_home)
    return render(request,'login.html')
def user_home(request):
    return render(request,'user_home.html')

def admin_home(request):
    return render(request,'admin_home.html')

def logt(request):
    logout(request)
    return HttpResponse('logout')



