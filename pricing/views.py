from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/user/sign_in/')
def pricing(request):
    return render(request, "pricing/pricing.html")