from django.contrib import admin
from django.urls import path,include
from django.views import defaults
from . import views
from website import urls
urlpatterns = [
    path('',views.dashboard,name="Dashboard"),
    path('pages/',views.passing_url),
    path('pages/forms/',views.basic_element,name="Basic ELement"),
    path('pages/course',views.course_form,name="Course Form"),
    path('logout/',views.logout),
]