from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def index(request):
    return render(request,'index.html',{})
def login(request):
    return render(request,'index.html',{})
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password ==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                userLogin = authenticate(username=username,password=password)
               # login(request,userLogin)
                return redirect('/')
        else:
            messages.info(request,'password not matching')
            return redirect('signup')
    else:
        return render(request,'signup.html')
def logout(request):
    pass