from django.http import HttpResponse
from django.shortcuts import render,redirect
from app1.models import tbl_user,cake_tbl
from django.contrib.auth import authenticate
from django. contrib.auth.models import User
def index(request):
    return render(request,'index.html')
def createac1(request):
    return render(request,'createaccount.html')
def createac2(request):
    a=User()
    b=tbl_user()
    a.first_name=request.POST.get('name')
    a.last_name=request.POST.get('lastname')
    a.email=request.POST.get('email')
    password=request.POST.get('password')
    a.username=request.POST.get('username')
    a.set_password(password)
    b.name=request.POST.get('name')
    b.age=request.POST.get('age')
    b.gender=request.POST.get('gender')
    b.phone=request.POST.get('phone')
    b.address=request.POST.get('address')
    b.username=request.POST.get('username')
    b.save()
    a.save()
   
    return redirect('/')
def login1(request):
    a=request.POST.get('username')
    b=request.POST.get('password')
    data=authenticate(username=a,password=b)
    if data is not None and data.is_superuser==1:
        return redirect('/admin1/')
    elif data is not None and data.is_superuser==0:
        return redirect('/user1/')
    else:
        return HttpResponse('invalid login')
    
def admin1(request):
    return render(request,'admin.html')
def user1(request):
    return render(request,'user.html')
def addcake1(request):
    return render(request,'addcake1.html')
def addcake2(request):
    b=cake_tbl()
    b.cakename=request.POST.get('cakename')
    b.price=request.POST.get('price')
    b.save()
    return redirect('/admin1/')
def viewcaketbl(request):
    x=cake_tbl.objects.all()
    return  render(request,'viewcaketbl.html',{'data':x})
def delete1(request,id):
    x=cake_tbl.objects.get(id=id)
    x.delete()
    return redirect('/viewcaketbl/')
def update1(request,id):
    b=cake_tbl.objects.get(id=id)
    return render(request,'updatecaketbl.html',{'data':b})
def updatecake(request,id):
    b=cake_tbl.objects.get(id=id)
    b.cakename=request.POST.get('cakename')
    b.price=request.POST.get('price')
    b.save()
    return redirect('/viewcaketbl/')
def viewuser(request):
    a=tbl_user.objects.all()
    return render(request,'viewuser.html',{'data':a})
def logout(request):
    return render(request,'index.html')

# Create your views here.
