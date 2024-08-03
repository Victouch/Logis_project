from django.shortcuts import render
from .models import Search

# Create your views here.

def home(request):

    if request.POST.get("search"):
        search = request.POST.get("search")
        searches = Search(searchs=search)
        searches.save()

    return render(request, "home/index.html")