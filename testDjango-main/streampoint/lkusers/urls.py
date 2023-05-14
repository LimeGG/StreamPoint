from django.urls import path, re_path, include
from . import views


urlpatterns = [
    #path('', views.index),
    path("", views.show_profile, name="Profile"),
    path("check/cookies/", views.MyView, name="cookies"),
    path("myshop", views.show_shopstreamer, name="myshopp"),
    path("addproduct", views.addproduct, name="addproduct"),
    path("myshop/delete/<int:pk>", views.deleteproduct, name="delete-product"),
    # path("api/points/create/", views.UserApi.as_view()),
    # path("api/autentifikate/", views.AuthTokenView.as_view(), name="autorize")

]

