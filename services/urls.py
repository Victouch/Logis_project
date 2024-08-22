from django.urls import path
from . import views

app_name = "services"

urlpatterns = [
    path("services/", views.services, name="services"),
    path("service-details/", views.service_details, name="service_details"),
]