from django.urls import path

from user import views

urlpatterns = [
    path("register/", views.UserRegister.as_view(), name="register"),
]
