from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth.hashers import make_password,check_password
import os

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            os.system('clear')
            # phash = make_password(password)
            # form.cleaned_data['password'] = phash
            print(password)
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request,f'Your acount has been created you can now log in')
            print("redirecting to home")
            return redirect('catalog:books')
    else:
        print("not sending post req")
        form = UserRegisterForm()
    return render(request,'user/register.html',{'form':form,'title':'register here!!'})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            form = login(request,user)
            messages.success(request,f"welcome {username} ")
            return redirect('home')
        else:
            messages.info(request,f'account does not exist please sign in')
    else: 
        form = AuthenticationForm()
    return render(request,'user/login.html',{'form':form,'title':'log in'})

def loguout(request):
    logout(request)
    return redirect('home')