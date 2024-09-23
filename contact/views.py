from django.shortcuts import render
from .models import Contact

# Create your views here.

def contact(request):
    if request.method == 'POST':
        if request.POST.get("name") and request.POST.get("email") and request.POST.get("subject") and request.POST.get("message"):
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message") 
            c_contact = Contact(your_name=name, your_email=email, subject=subject, message=message)
            c_contact.save()

    return render(request, "contact/contact.html")