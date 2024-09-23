from django.shortcuts import render

# Create your views here.

def user(request):
    return render(request, "user/sign_in.html")

def register(request):
    return render(request, "user/register.html")