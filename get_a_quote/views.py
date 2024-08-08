from django.shortcuts import render

# Create your views here.

def get_a_quote(request):
    return render(request, "get_a_quote/get-a-quote.html")