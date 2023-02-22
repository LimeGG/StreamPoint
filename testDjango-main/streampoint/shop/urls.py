from django.urls import path
from . import views

urlpatterns = [
    path('', views.stream, name ="Shop"),
    path('<int:streamer_id>', views.show_shop,name="Shopstreamer")
]