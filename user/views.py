from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.mixins import UserPassesTestMixin,PermissionRequiredMixin
from django.views.generic import View
from .models import LibraryUser
from django.http import HttpResponse
import os

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            #os.system('clear')
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

class UserTestView(PermissionRequiredMixin,View):
    template_name = "author_list.html"
    permission_required = 'can_add_book'
    permission_denied_message = 'can not enter'
    # def test_func(self):
    #     #os.system('clear')
    #     if self.request.user.has_perm("can_add_book"):
    #         return True
    #     perms = self.request.user.user_permissions
    #     print(perms)
    #     return False
    def get(self,request,*args,**kwargs):
        print("worked")
        html = '<html lang="en"><body>worked.</body></html>'
        return HttpResponse(html)
    