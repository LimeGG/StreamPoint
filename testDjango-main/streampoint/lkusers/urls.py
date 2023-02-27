from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index),
    path("", views.show_profile, name="Profile"),
    path("myshop", views.show_shopstreamer, name="myshopp"),
    path("addproduct", views.addproduct, name="addproduct"),
    path("myshop/delete/<int:pk>", views.deleteproduct, name="delete-product")
]