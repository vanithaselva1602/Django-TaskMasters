
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
def home(request):
    return render(request, 'tasks/home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created. Please login.")
        return redirect('login')
    

    return render(request, 'tasks/signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('task_list')
        else:
             messages.error(request, "Invalid username or password")
    return render(request, 'tasks/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def task_list(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == "POST":
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            assigned_to=request.user
            
        )
        return redirect('task_list')
    return render(request, 'tasks/create-task.html')

def task_detail(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required(login_url='login')
def update_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == "POST":
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return redirect('task_list')

    return render(request, 'tasks/update-task.html', {'task': task})




