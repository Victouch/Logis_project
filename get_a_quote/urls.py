from django.urls import path
from . import views

app_name = "get_a_quote"

urlpatterns = [
    path("quote/", views.get_a_quote, name="get_a_quote")
]