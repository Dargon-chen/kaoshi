import hashlib
import os
import uuid

from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

# 首页
from app.models import User, Mei


def index(request):
    token = request.session.get('token')
    meit = Mei.objects.filter(flag=1)
    meif = Mei.objects.get(flag=2)
    meigoods = Mei.objects.filter(flag=3)
    mant = Mei.objects.filter(flag=4)
    manfl = Mei.objects.get(name='nl')
    manfr = Mei.objects.get(name='nr')
    mangoods = Mei.objects.filter(flag=6)
    data = {
        'usertels': '登陆',
        'logs': '注册',
        'meit':meit,
        'meif':meif,
        'meigoods':meigoods,
        'mant':mant,
        'manfl':manfl,
        'manfr':manfr,
        'mangoods':mangoods,

    }
    if token:
        user = User.objects.get(usertoken=token)
        data['usertels']=user.usertel
        data['logs']='注销'
        print(user.usertel)
        return render(request,'index.html',context=data)



    return render(request,'index.html',context=data)

def register(request):
    token = request.session.get('token')
    if token:
        return redirect('app:logout')
    if request.method=='POST':
        user = User()
        user.usertel = request.POST.get('tel')
        # user.userpassword = str(genter_passwd(request.POST.get('password')))
        print(genter_passwd(request.POST.get('password')))
        print(genter_passwd(request.POST.get('password')))
        user.userpassword = request.POST.get('password')
        user.useremail = request.POST.get('email')
        user.usertoken = str(uuid.uuid5(uuid.uuid4(),'register'))
        user.save()
        print(user.usertel)
        request.session['token'] = user.usertoken
        return redirect('app:index')
    elif request.method=='GET':
        return render(request,'register.html')



def quit(request):
    logout(request)
    return redirect('app:index')

def login(request):
    if request.method=='POST':
        usertel = request.POST.get('tel')
        # password = str(genter_passwd(request.POST.get('password')))
        password = request.POST.get('password')

        data = {
            'usertels': '登陆',
            'logs': '注册'

        }
        users = User.objects.filter(usertel = usertel)
        user = users[0]

        if user:
            print(usertel)
            print(user.usertel)
            print(user.userpassword)
            print(password)
            if password == user.userpassword:
                print(1)
                data['usertels']=user.usertel
                data['logs']='注销'
                request.session['token']=user.usertoken
                return render(request,'index.html',context=data)
            return render(request,'login.html')
    else:

        return render(request,'login.html')

def genter_passwd(passwd):
    sha = hashlib.md5()
    sha.update(passwd.encode('utf-8'))
    return sha.hexdigest







