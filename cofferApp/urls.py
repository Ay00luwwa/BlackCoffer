from django.contrib import admin
from django.urls import path
from cofferApp import views

urlpatterns = [
    path("", views.index, name='index'),
]