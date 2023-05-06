from django.urls import path
from . import views


urlpatterns = [
    path('', views.reg_user, name="Regist"),
    path('login/', views.login, name='Login'),

]