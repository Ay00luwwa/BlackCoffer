from django.contrib import admin
from django.urls import path
from cofferApp import views
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name='index'),
     path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]