from django.shortcuts import render
from .models import Quote

# Create your views here.

def get_a_quote(request):
    if request.method =='POST':
        if request.POST.get("departure") and request.POST.get("delivery") and request.POST.get("weight") and request.POST.get("dimensions") and request.POST.get("name") and request.POST.get("email") and request.POST.get("phone") and request.POST.get("message"):
            departure = request.POST.get("departure")
            delivery = request.POST.get("delivery")
            weight = request.POST.get("weight")
            dimensions = request.POST.get("dimensions")
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            message = request.POST.get("message")
            g_get_a_quote = Quote(city_of_departure=departure, delivery_city=delivery, total_weight=weight, dimension=dimensions, your_name=name, your_email=email, phone=phone, message=message)
            g_get_a_quote.save()

    return render(request, "get_a_quote/get-a-quote.html")