from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index),
    path("", views.show_profile,name="Profile"),
]