from django.urls import path

from . import views



urlpatterns = [
   

    path('', views.head , name = "head-post")
]