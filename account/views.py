from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm 
from django.contrib.auth import authenticate, login, logout , get_user_model
from django.contrib.auth.models import AbstractUser , User
from django.views.generic import ListView
from .models import Task
from .forms import Taskform
def index(request):
    return render(request, 'account/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect ('index')
    else:
        form = UserCreationForm()

    context = {'form' : form} 
    return render(request, 'registration/ register.html', context)#coolsite/account/templates/registration/ register.html


def loginsee (request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect ('index')
    else:
        form = AuthenticationForm()

    return render (request, 'registration/login.html',{'form':form})
def user_list(request):
    all_users = get_user_model().objects.all()
    context = {
        "allusers":all_users
    }
    return render (request, "account/user_list.html",context)

def Blog_view(request):
    tasks = Task.objects.all()
    return render (request, "account/blog.html", {'tasks' : tasks})

def blog_create(request):
    error = ''
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.author2 = request.user.username
            form.save()
            return redirect ('blog')
        else:
            error = 'FORM BLOG IF INVALID'

    form = Taskform()
    contextblog = {
        'form' : form,
        "error": error
    }
    return render (request, "account/blog_create.html",contextblog)