from django.contrib import admin
from django.urls import path,include
from django.views import defaults
from . import views

urlpatterns = [
    path('',views.dashboard,name="Dashboard"),
    path('pages/forms/',views.basic_element,name="Basic ELement"),
    path('logout/',views.logout),
]