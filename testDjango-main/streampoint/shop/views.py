from django.shortcuts import render
from .models import *
from streamers.models import AllStreamers
from lkusers.models import HisStreamers


def stream(request):
    jpg = AllStreamers.objects.all()
    return render(request, 'shop/streamers.html', {'jpg': jpg})


def show_shop(request, streamer_id):
    user_id = request.user.id
    points1 = HisStreamers.objects.filter(streamers_id=streamer_id, user_id=user_id)
    product = AddProduct.objects.filter(streamer_id=streamer_id)
    name = product[0]
    points = points1[0]
    print(points)
    return render(request, "shop/shop.html",
                  {"product": product, "streamer": streamer_id, "name": name, "points": points})



