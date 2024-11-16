from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.

def user(request):
    context = {}
    return render(request, "user/sign_in.html", context)

def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account successfully created")

            return redirect('user')
    context = {'form':form}
    return render(request, "user/register.html", context)
