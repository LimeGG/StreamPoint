from django.shortcuts import render
from .models import *


def index(request):
    return render(request, "main/index.html")


def show_shop(request, streamer_id):
    product = AddProduct.objects.filter(streamer_id=streamer_id)
    name = product[0]
    return render(request, "shop/shop.html", {"product": product, "streamer": streamer_id, "name": name})
