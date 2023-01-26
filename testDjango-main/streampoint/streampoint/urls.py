from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('lkusers/', include('lkusers.urls')),
    path('registration/', include('registration.urls')),
    path('shop/', include('shop.urls')),
    path('streamers/', include('streamers.urls'))
]
