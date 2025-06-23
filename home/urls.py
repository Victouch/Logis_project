from django.urls import path
from . import views

app_name="home"

urlpatterns = [
    path('', views.home, name="home"),         # for https://yourapp.herokuapp.com/
    path('home/', views.home, name="home_alt") # optional: keeps /home/ working
]


