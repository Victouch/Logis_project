from django.shortcuts import render
from .models import Search

# Create your views here.

def home(request):

    if request.method == "POST" and request.POST.get("search"):
        search = request.POST.get("search")
        searches = Search(search=search)
        searches.save()
        

    return render(request, "home/index.html")