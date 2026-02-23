from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import * 
from django.contrib.auth.mixins import PermissionRequiredMixin
import os 
from django.views import View

@login_required(login_url='login')
def index(request):
    num_books = Book.objects.all().count() #Book is imported from models
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits',0)
    num_visits += 1
    request.session['num_visits'] = num_visits
    context = {
        "num_books" : num_books,
        "num_instances" : num_instances,
        "num_instances_available" : num_instances_available,
        "num_authors" : num_authors,
        "num_visits" : num_visits
                }
    print(num_visits)
    return render(request,'catalog/index.html',context=context)


@login_required(login_url='login')        
def booklist(request):
    bookl = Book.objects.all()
    context = {
        "book_list" : bookl,
    }
    return render(request,'catalog/book_list.html',context)

@login_required(login_url='login')
def book_detail(request,pk):
    book = Book.objects.all().get(id=pk) #filter wont work here it returns a list
    #print(book)
    context = {
        "book" : book,
    }
    return render(request,'catalog/book_detail.html',context)

@login_required(login_url='login')
def authorlist(request):
    os.system('clear')
    authorl = Author.objects.all()
    print(authorl)
    context = {
        "author_list" : authorl
    }
    return render(request,'catalog/author_list.html',context)


@login_required(login_url='login')
def author_detail(request,pk):
    author = Author.objects.all().get(id=pk) #filter wont work here it returns a list
    #print(book)
    context = {
        "author" : author,
    }
    return render(request,'catalog/author_detail.html',context)

class TestingView(PermissionRequiredMixin,View):
    permission_required = 'can_add_book'
    print("worked")