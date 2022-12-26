from django.urls import path,include
from . import views
# import blog

urlpatterns = [
    path('',views.index),
    path('register/',views.register)
]