from django.shortcuts import render
from .models import *
from streamers.models import AllStreamers

def stream(request):
    jpg = AllStreamers.objects.all()
    return render(request, 'shop/streamers.html', {'jpg': jpg})


def show_shop(request, streamer_id):
    product = AddProduct.objects.filter(streamer_id=streamer_id)
    name = product[0]
    return render(request, "shop/shop.html", {"product": product, "streamer": streamer_id, "name": name})
