from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            messages.info(request,  "Incorrect username or password")

    context = {}
    return render(request, "user/sign_in.html", context)

def logout_user(request):
    logout(request)
    return redirect('/user/sign_in/')

def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account successfully created")

            return redirect('/user/sign_in/')
    context = {'form':form}
    return render(request, "user/register.html", context)
