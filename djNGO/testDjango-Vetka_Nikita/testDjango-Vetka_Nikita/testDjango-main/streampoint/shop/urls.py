from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:streamer_id>', views.show_shop,name="Shopstreamer")
]