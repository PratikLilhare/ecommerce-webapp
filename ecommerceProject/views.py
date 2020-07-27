from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        pwd = request.POST['pass']
        email = request.POST['email']
        mob = request.POST['mobile']
        utype = request.POST['utype']

        u = User(first_name=fname,last_name=lname,username=uname,password=make_password(pwd),email=email)
        u.save()

        up = UserProfile(user=u ,phone = mob, usertype=utype)
        up.save()

        return redirect("/login/")

    return render(request,"signup.html")


def login_call(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pwd = request.POST['pwd']

        u = authenticate(username = uname,password = pwd)
        if u:
            login(request,u)
            up = UserProfile.objects.get(user__username = request.user)
            if up.usertype == "buyer":
                return redirect("/buyer/")
            elif up.usertype == "seller":
                return redirect("/seller/")
            
        else:
            return HttpResponse("<h1>wrong credentials</h1>")

    else:
        return render(request,"login.html")

@login_required
def logout_call(request):
    logout(request)
    return redirect("/login/")

def welcome(request,id):
    up = UserProfile.objects.all()
    return render(request,"welcome.html",{'user':up})
