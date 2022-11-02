from django.contrib import admin
from django.urls import path,include
from django.views import defaults
from . import views

urlpatterns = [
    path('',views.index,name="Dashboard"),
    path('dashboard/',views.index,name="Dashboard"),
]