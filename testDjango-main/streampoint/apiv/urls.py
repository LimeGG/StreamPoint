from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path("points/create/", views.UserApi.as_view()),
    path("get/token/", views.TokenApi.as_view()),
    path("check/token", views.ValidateTokenApi.as_view())
]

