# from django.shortcuts import render
# from .models import Search

# # Create your views here.

# def home(request):

#     if request.method == "POST" and request.POST.get("search"):
#         search = request.POST.get("search")
#         searches = Search(search=search)
#         searches.save()
        

#     return render(request, "home/index.html")

from django.shortcuts import render
from .models import Search
from services.models import Service  # Import the model you want to search
from django.db.models import Q

def home(request):
    query = request.GET.get("search")
    results = []

    if query:
        # Save the search to your Search model
        Search.objects.create(search=query)

        # Perform the actual search (adjust fields to match your model)
        results = Service.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        print("Query:", query)
        print("Results:", results)

    return render(request, "home/index.html", {
        "results": results,
        "query": query,
    })
