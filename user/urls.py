from django.urls import path
from. import views

app_name = "user"

urlpatterns = [
    path("user/", views.sign_in, name="sign_in"),
    path("register/", views.register, name="register")
]
