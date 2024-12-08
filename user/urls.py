from django.urls import path
from. import views

app_name = "user"

urlpatterns = [
    path("sign_in/", views.sign_in, name="sign_in"),
    path("register/", views.register, name="register"),
    path('logout/', views.logout_user, name="logout"),
]
